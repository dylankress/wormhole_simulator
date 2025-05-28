#node_mamager.py
"""
This module is responsible for generating all nodes at the begining of the simulation.
"""

from sim_node import SimNode

"""
I need to update the attributes to include the logic necessary to assign the correct valies to the attributes below...
"""

def generate_node(node_id, rng):
    attrs = {
        "available_storage_space_gb": float,


    }
    return SimNode(node_id, **attrs)

def generate_nodes():
    '''
    The modeule about outlines the process for generating 1 node instance. This logic needs to use that to geenrate many randmonized multiples
    '''
    pass
