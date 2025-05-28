#file_manager.py
"""
The file manager modeule is solely responsible for managing all files, and their corresponsing chunks.
"""

from typing import Dict, Set
from sim_file import SimFile

class FileManager:
    def __init__(self):
        self.chunk_to_file_map: Dict[str, SimFile] = {}
        self.awaiting_upload: Set[str] = set()
        self.awaiting_replication: Set[str] = set()
        self.awaiting_recipient_notify: Set[str] = set()
        self.awaiting_download: Set[str] = set()
        self.awaiting_repair: Set[str] = set()
        self.obsolete_chunks: Set[str] = set()

    def register_file(self):
        pass

    def upload_chunks(self):
        pass

    def replicate_chunks(self):
        pass

    def notify_recipients(self):
        pass

    def transfer_chunks_to_recipient(self):
        pass

    def repair_chunks(self):
        pass

    def delete_obsolete_chunks(self):
        pass

    def get_file_by_chunk(self):
        pass

    def get_owner_by_chunk(self):
        pass

    def get_file_recipient(self):
        pass
