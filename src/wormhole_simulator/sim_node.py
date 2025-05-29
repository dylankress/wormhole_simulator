#sim_node.py
"""
This file defines the node class. It holds all the attributes, behaviors, and methods for a typical wormhole node.
All attributes will be passed via node_generator.py
"""

from typing import List
from sim_file import SimFile

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

    def __repr__(self):
        return (
            f"<SimNode {self.node_id} | "
            f"Online: {self.is_online} | "
            f"Upload: {self.upload_speed:.1f} Mbps | "
            f"Download: {self.download_speed:.1f} Mbps | "
            f"Files Owned: {len(self.owned_files)}>"
            f"Send Freq: {self.file_send_frequency:.2f}>"
        )

    def upload_file(self):
        #This function needs to fire periodically based on a frequency range set in the config file. Every x minutes the node should check, do i own any files? If yes proceed, if no do nothing. The if they have a file it should choose one of their files at random and add that file, its chunks, and the file recipient to the file_managr.py chunk_to_file_map.
        pass
