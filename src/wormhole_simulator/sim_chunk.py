"""

This file defines the chunk class. It holds all the attributes, behaviors, and methods for a typical wormhole chunk.

"""

class SimChunk:
    chunk_id: str   #assigned during generate_chunks in transfer_file.py
    parent_file_id: str #assigned during generate_chunks in transfer_file.py
    parent_node_id: str #assigned during generate_chunks in transfer_file.py
    is_uploaded: bool   #flase by default. set to true during distribute_chunks in transfer_file.py
    is_replicated: bool #false by default. set to true during
    is_obsolete: bool   #false by default. set true 
