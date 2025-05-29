# file_generator.py
"""
Generates all files for the simulation and breaks them into chunks based on config parameters.
"""

from typing import List
from sim_file import SimFile
import random
import math
from config import (
    FILE_SIZE_RANGE_GB,
    CHUNK_SIZE_MB,
)

def generate_file(file_id: str, recipient_node_id: str, rng: random.Random) -> SimFile:
    # Generate a file size in GB
    file_size_gb = rng.uniform(*FILE_SIZE_RANGE_GB)

    # Calculate number of chunks
    file_size_mb = file_size_gb * 1024
    num_chunks = math.ceil(file_size_mb / CHUNK_SIZE_MB)

    # Generate chunk IDs
    chunks = {f"{file_id}_chunk_{i}" for i in range(num_chunks)}

    return SimFile(
        file_id=file_id,
        file_size_gb=file_size_gb,
        file_recipient=recipient_node_id,
        chunks=chunks,
    )

