"""

The network controller is the brain of the wormhole simulation.
It's the only persistent object in the entire simulation, so it's responsible for keeping track of
many important data sets and events throughout the course of each simulation.

"""

from utils.distribute_chunks import distribute_chunks

class NodeManager:
    def __init__(self):
        self.online_nodes: list[str]
        self.notification_queue = set() #queue for nodes to notify when all chunks have been replicated for a file being sent to them.


def simulate_network_joins():
    """From offline nodes, bring n% (percentage range) online.
    Random selection should be weighted to effect higher reliability score nodes more heavily."""
    pass

def simulate_network_leaves():
    """From online nodes, send n% (percentage range) offline.
    Random selection should be weighted to effect lower reliability score nodes more heavily."""
    pass

def replicate_chunks():
    """monitor for and replicate all unreplicated chunks to ensure perfect file availability for downloaders"""
    pass

def maintain_chunk_replication_factor():
    """"""
    distribute_chunks
    pass

def cleanup_obsolete_chunks():
    """"""
    pass

def notify_recipients():
    """notify offline recipient."""
    pass

def maintain_available_file_send_limits():
    """monitor network for uptime, file transfers & uploads and adjust node available_file_send_limit_gb
    Uptime increases limit. Uploads & transfers decrease limit"""
    pass
