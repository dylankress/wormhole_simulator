#node_manager.py
"""
The network controller is the brain of the wormhole simulation.
It's the only persistent object in the entire simulation, so it's responsible for keeping track of
many important data sets and events throughout the course of each simulation.
"""

from utils.distribute_chunks import distribute_chunks

class NodeManager:
    def __init__(self):
        self.online_nodes: list[str]

    def simulate_network_joins():
        """From offline nodes, bring n% (percentage range) online.
        Random selection should be weighted to effect higher reliability score nodes more heavily."""
        pass

    def simulate_network_leaves():
        """From online nodes, send n% (percentage range) offline.
        Random selection should be weighted to effect lower reliability score nodes more heavily."""
        pass

