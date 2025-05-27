"""

This file defines the node class. It holds all the attributes, behaviors, and methods for a typical wormhole node.

"""

class SimNode:
    def __init__(
        self,
        node_id,
        available_storage_space_gb,
        reliability_score,
        owned_files,
        is_online,
        hosted_chunks,
        my_hosted_files,
        my_sent_files,
        pending_downloads,
        downloaded_files,
        chosen_sender_chance,
        total_files_sent,
        total_files_sent_size_gb,
        available_file_send_limit_gb
        ):
        
        
        self.node_id = node_id   
        self.available_storage_space_gb = available_storage_space_gb
        self.reliability_score = reliability_score
        self.owned_files = owned_files
        self.is_online = is_online
        self.hosted_chunks = hosted_chunks
        self.my_hosted_files = my_hosted_files
        self.my_sent_files = my_sent_files
        self.pending_downloads = pending_downloads
        self.downloaded_files = downloaded_files
        self.chosen_sender_chance = chosen_sender_chance
        self.total_files_sent = total_files_sent
        self.total_files_sent_size_gb = total_files_sent_size_gb
        self.available_file_send_limit_gb = available_file_send_limit_gb

