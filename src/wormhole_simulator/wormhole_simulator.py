# wormhole_simulator.py
"""
This is a minimal simulation bootstrapper that verifies core generators are working.
"""

from config import TOTAL_SIMULATED_NODES, RNG_SEED
from utils.node_generator import generate_nodes
from utils.file_generator import generate_files
from utils.sim_clock import SimClock

def main():
    # Step 1: Build list of node IDs
    node_ids = [f"node_{i}" for i in range(TOTAL_SIMULATED_NODES)]

    # Step 2: Generate files (with random recipients from node_ids)
    files = generate_files(node_ids, rng_seed=RNG_SEED)

    # Step 3: Generate nodes (with random file ownership)
    nodes = generate_nodes(files, rng_seed=RNG_SEED)

    # Step 4: Initialize the simulation clock
    clock = SimClock()

    # Step 5: Print summary
    print("=== Wormhole Simulation Initialized ===")
    print(f"Tick: {clock.current()}")
    print(f"Total Nodes: {len(nodes)}")
    print(f"Total Files: {len(files)}")
    print(f"Total Chunks: {sum(len(f.chunks) for f in files)}")

    print("\n--- Sample Node ---")
    print(nodes[0])

    print("\n--- Files Owned by Sample Node ---")
    for f in nodes[0].owned_files:
        print(f)

    print("\n--- Sample File ---")
    print(files[0])

    print("\n--- Chunks in Sample File ---")
    print(sorted(list(files[0].chunks))[:10])  # Print first 10 chunk IDs

if __name__ == "__main__":
    main()

