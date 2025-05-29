#sim_node.py
"""
This file defines the node class. It holds all the attributes, behaviors, and methods for a typical wormhole node.
All attributes will be passed via node_generator.py
"""

from typing import List
from sim_file import SimFile
import random

class SimNode:
    def __init__(
        self,
        node_id: str,
        owned_files: List[SimFile],
        is_online: bool,
        upload_speed: float,
        download_speed: float,
        uptime_score: int,
        available_storage_space_gb: float,
        available_file_send_limit_gb: float,
        file_send_frequency: int,
        rng: random.Random,
        ):

        self.node_id = node_id
        self.owned_files = owned_files
        self.is_online = is_online
        self.upload_speed = upload_speed
        self.download_speed = download_speed
        self.uptime_score = uptime_score
        self.available_storage_space_gb = available_storage_space_gb
        self.available_file_send_limit_gb = available_file_send_limit_gb
        self.file_send_frequency = file_send_frequency
        self.last_upload_tick = -1
        self.file_creation_frequency = rng.randint(5, 60) * 60

    def __repr__(self):
        return (
            f"<SimNode {self.node_id} | "
            f"Online: {self.is_online} | "
            f"Upload: {self.upload_speed:.1f} Mbps | "
            f"Download: {self.download_speed:.1f} Mbps | "
            f"Files Owned: {len(self.owned_files)}>"
            f"Send Freq: {self.file_send_frequency:.2f}>"
        )

    # --------------- Upload File ---------------

    def upload_file(self, rng: random.Random, file_manager, current_tick: int):
        if not self.is_online:
            return

        if current_tick - self.last_upload_tick < self.file_send_frequency:
            return

        if not self.owned_files:
            return

        selected_file = rng.choice(self.owned_files)
        self.last_upload_tick = current_tick
        return selected_file

    def should_create_file(self, current_tick: int) -> bool:
        return current_tick % self.file_creation_frequency == 0
