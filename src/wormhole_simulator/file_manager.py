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

    # --------------- Methods ---------------

    def register_upload_request(self, sim_file: SimFile):
        # Register each chunk → file mapping
        for chunk_id in sim_file.chunks:
            self.chunk_to_file_map[chunk_id] = sim_file
            self.awaiting_upload.add(chunk_id)

    def process_awaiting_upload_list(self):
        pass

    def process_awaiting_replication_list(self):
        pass

    def process_awaiting_repair_list(self):
        pass

    def process_obsolete_chunks_list(self):
        pass

    def process_awaiting_recipient_notify_list(self):
        pass

    def process_awaiting_download_list(self):
        pass

    def get_file_by_chunk(self):
        pass

    def get_owner_by_chunk(self):
        pass

    def get_file_recipient(self):
        pass
