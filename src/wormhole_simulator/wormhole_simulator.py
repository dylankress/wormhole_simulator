# wormhole_simulator.py
"""
This is a minimal simulation bootstrapper that verifies core generators are working.
"""

from config import TOTAL_SIMULATED_NODES, RNG_SEED, NEW_FILE_CREATION_INTERVAL_MIN, SEND_LIMIT_RECOVERY_RATE_GB_PER_TICK
from utils.node_generator import generate_nodes
from utils.sim_clock import SimClock
from file_manager import FileManager
from utils.file_generator import generate_file
from node_manager import NodeManager

import random

TICKS_TO_RUN = 10000
PRINT_EVERY = 1  # how often to print tick summary
NEW_FILE_CREATION_INTERVAL_TICKS = NEW_FILE_CREATION_INTERVAL_MIN * 60

def main():
    rng = random.Random(RNG_SEED)
    file_counter = 0
    live_files = []
    # --- Initialization ---
    node_ids = [f"node_{i}" for i in range(TOTAL_SIMULATED_NODES)]
    nodes = generate_nodes([], rng_seed=RNG_SEED)
    node_manager = NodeManager(nodes)
    clock = SimClock()
    file_manager = FileManager()

    print("=== Wormhole Simulation Started ===")
    print(f"Running for {TICKS_TO_RUN} ticks...\n")

    # --- Tick Loop ---
    for _ in range(TICKS_TO_RUN):
        current_tick = clock.current()
        if current_tick % 300 == 0:
            node_manager.simulate_churn(rng)
            print(
                f"[Churn @ Tick {current_tick}] "
                f"Online Nodes: {len(node_manager.online_nodes)}, "
                f"Offline Nodes: {len(node_manager.offline_nodes)}"
            )

        # Node actions
        for node in nodes:
            if node.should_create_file(current_tick):
                file_id = f"file_{file_counter}"
                file_counter += 1
                new_file = generate_file(file_id, node.node_id, rng)
                node.owned_files.append(new_file)
                live_files.append(new_file)

            file = node.upload_file(rng, file_manager, clock.current())
            if file:
                file_manager.register_upload_request(file)

            node.recover_send_limit(SEND_LIMIT_RECOVERY_RATE_GB_PER_TICK)

        clock.advance()

    total_GB_uploaded = len(file_manager.awaiting_upload) * 10 / 1024

    total_earned_send_limit = sum(node.total_earned_send_limit_gb for node in nodes)

    total_failed_uploads = sum(node.failed_uploads for node in nodes)

    print("\n=== Simulation Finished ===")
    print(f"Total Ticks: {clock.current()}")
    print(f"Chunks awaiting upload: {len(file_manager.awaiting_upload)}")
    print(f"Files in map: {len(set(f.file_id for f in file_manager.chunk_to_file_map.values()))}")
    print(f"Total Data Uploaded: {total_GB_uploaded:.2f} GB")
    print(f"Total Failed Uploads: {total_failed_uploads}")
    print(f"Total Send Limit Earned: {total_earned_send_limit:.2f} GB")

if __name__ == "__main__":
    main()

