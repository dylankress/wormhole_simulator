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
        # This method should operate at a frequency we set in config.py called PROCESS_AWAITING_UPLOAD_LIST_FREQUENCY. Every time it runs it's goal is to move all the chunks in that list into self.awaiting_replication. In order to do this we need a few things for every chunk on the list: the chunk's owner and their upload_speed (use chunk_to_file_map for this), an online node we can send the file to (must be online, must have enough available storage space, would be best if they have a good uptime score, would be best if they have a good download speed). Once we've found a suitable host node we need to simulate this "transfer" by actually delaying moving chunks from awaiting_upload to awaiting_replication over the number of ticks it would take based on the lower of the 2 transfer speeds (upload_speed for uploading node or download_speed for host node). Then once that transfer is complete we need to either update chunk_to_file_map to keep track of where the uploaded chunk is being stored or add it to another Dict if there's a better way to keep track of it beyond what we already have built out here.
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
