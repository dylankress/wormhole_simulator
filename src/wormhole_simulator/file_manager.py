"""

The file manager modeule is solely responsible for managing all files, and their corresponsing chunks.

"""

class FileManager:
    def __init__(self):
        self.uploaded_files = []
        self.downloaded_files = []
        self.upload_queue = set()   #queue for initial uploads. lists all chunks that need to be assigned to a host node.
        self.replication_queue = set()  #queue for chunks needing initial replication. 
        self.under_replicated_queue = set() #queue for chunks that have dropped below replication factor
