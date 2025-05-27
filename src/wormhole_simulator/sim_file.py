"""

This file defines the file class. It holds all the attributes, behaviors, and methods for a typical wormhole file.

"""

from enum import Enum
from typing import List, Optional
from sim_chunk import SimChunk


class SimFile:
    def __init__(self, file_id: str, file_size_mb: int, owner_node_id: str, file_recipient: str):
        self.file_id: str = file_id                                     #set automatically at simulation initialization
        self.file_size_mb: int = file_size_mb                           #set automatically at simulation initialization
        self.owner_node_id: str = owner_node_id                         #set automatically at simulation initilization
        self.file_recipient: str = file_recipient                       #should be none until set by set_recipient

        self.child_chunks = set()                                       #set during transfer_file process during generate_chunks loop 
        self.is_uploaded: bool = False                                  #Default is false. Set to true when is uploaded = true for all child chunks
        self.is_replicated: bool = False                                #default is false. Set to true when all child chunks replication = True
        self.should_expire: bool = True                                 #default is false. set to true if file is transfered rather than uploaded
        self.expiration_tick: Optional[int] = None                      #set to none by default. Set up upload_file.py if file is flagges as a transfer
        self.has_expired: bool = False                                  #should default to flase. Set to true by file_expiration_timer
