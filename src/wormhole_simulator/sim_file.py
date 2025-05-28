#sim_file.py
"""
This file defines the file class. It holds all the attributes, behaviors, and methods for a typical wormhole file.
"""
from typing import Set

class SimFile:
    def __init__(
        self,
        file_id: str,
        file_size_gb: float,
        file_recipient: str,
        chunks: Set[str],
    ):

        self.file_id = file_id
        self.file_size_gb = file_size_gb
        self.file_recipient = file_recipient
        self.chunks = chunks
