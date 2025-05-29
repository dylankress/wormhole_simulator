#node_generator.py
"""
This module is responsible for generating all nodes at the begining of the simulation.
"""

from typing import List
from sim_node import SimNode
from sim_file import SimFile
import random
from config import (
    UPLOAD_SPEED_RANGE_MBPS,
    DOWNLOAD_SPEED_RANGE_MBPS,
    UPTIME_SCORE_RANGE,
    STORAGE_RANGE_GB,
    SEND_LIMIT_RANGE_GB,
    FILE_SEND_FREQUENCY_RANGE,
    TOTAL_SIMULATED_NODES,
)

def generate_node(node_id: str, files: List[SimFile], rng: random.Random) -> SimNode:
    # Ensure deterministic chunk assignment
    sorted_files = sorted(files, key=lambda f: f.file_id)

    owned_files = rng.sample(sorted_files, k=rng.randint(0, min(5, len(sorted_files))))
    is_online = rng.random() < 0.7
    upload_speed = rng.uniform(*UPLOAD_SPEED_RANGE_MBPS)
    download_speed = rng.uniform(*DOWNLOAD_SPEED_RANGE_MBPS)
    uptime_score = rng.randint(*UPTIME_SCORE_RANGE)
    available_storage_space_gb = rng.randint(*STORAGE_RANGE_GB)
    available_file_send_limit_gb = rng.uniform(*SEND_LIMIT_RANGE_GB)
    file_send_frequency = rng.uniform(*FILE_SEND_FREQUENCY_RANGE)

    return SimNode(
        node_id=node_id,
        owned_files=owned_files,
        is_online=is_online,
        upload_speed=upload_speed,
        download_speed=download_speed,
        uptime_score=uptime_score,
        available_storage_space_gb=available_storage_space_gb,
        available_file_send_limit_gb=available_file_send_limit_gb,
        file_send_frequency=file_send_frequency,
    )

def generate_nodes(files: List[SimFile], rng_seed: int = 42) -> List[SimNode]:
    rng = random.Random(rng_seed)
    return [generate_node(f"node_{i}", files, rng) for i in range(TOTAL_SIMULATED_NODES)]
