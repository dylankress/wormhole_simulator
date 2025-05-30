#node_manager.py
"""
The network controller is the brain of the wormhole simulation.
It's the only persistent object in the entire simulation, so it's responsible for keeping track of
many important data sets and events throughout the course of each simulation.
"""

import random
from utils.distribute_chunks import distribute_chunks
from config import (
    ONLINE_WEIGHT_EXPONENT,
    OFFLINE_WEIGHT_EXPONENT,
    NETWORK_CHURN_MULTIPLIER
)

class NodeManager:
    def __init__(self, nodes: list):
        self.all_nodes: dict[str, SimNode] = {node.node_id: node for node in nodes}
        self.online_nodes: set[str] = {node.node_id for node in nodes if node.is_online}
        self.offline_nodes: set[str] = set(self.all_nodes.keys()) - self.online_nodes

    def bring_online(self, node_id: str):
        node = self.all_nodes[node_id]
        if not node.is_online:
            node.is_online = True
            self.offline_nodes.discard(node_id)
            self.online_nodes.add(node_id)

    def take_offline(self, node_id: str):
        node = self.all_nodes[node_id]
        if node.is_online:
            node.is_online = False
            self.online_nodes.discard(node_id)
            self.offline_nodes.add(node_id)

    def compute_weighted_probabilities(self, uptime_scores, exponent):
        weights = [score ** exponent for score in uptime_scores]
        total = sum(weights)
        return [w / total for w in weights] if total > 0 else [1 / len(uptime_scores)] * len(uptime_scores)

    def simulate_churn(self, rng: random.Random):
        # Churn % scales with the multiplier and node count
        num_online_to_offline = int(len(self.online_nodes) * 0.05 * NETWORK_CHURN_MULTIPLIER)
        num_offline_to_online = int(len(self.offline_nodes) * 0.05 * NETWORK_CHURN_MULTIPLIER)

        # --- Offline to Online ---
        offline_node_ids = list(self.offline_nodes)
        offline_scores = [self.all_nodes[nid].uptime_score for nid in offline_node_ids]
        online_probs = self.compute_weighted_probabilities(offline_scores, ONLINE_WEIGHT_EXPONENT)
        selected_online_ids = rng.choices(offline_node_ids, weights=online_probs, k=min(num_offline_to_online, len(offline_node_ids)))
        for nid in selected_online_ids:
            self.bring_online(nid)

        # --- Online to Offline ---
        online_node_ids = list(self.online_nodes)
        online_scores = [self.all_nodes[nid].uptime_score for nid in online_node_ids]
        inverse_scores = [101 - s for s in online_scores]  # 101 - score gives higher value for low-uptime
        offline_probs = self.compute_weighted_probabilities(inverse_scores, OFFLINE_WEIGHT_EXPONENT)
        selected_offline_ids = rng.choices(online_node_ids, weights=offline_probs, k=min(num_online_to_offline, len(online_node_ids)))
        for nid in selected_offline_ids:
            self.take_offline(nid)

