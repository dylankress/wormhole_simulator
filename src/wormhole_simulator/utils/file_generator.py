"""

The file generator module is responsible for generating files at the beginig of the simualtion and siigning them to owning nodes.

"""

from sim_file import SimFile

def generate_file(file_id, rng):
    attrs = {

    }
    return SimFile(file_id, **attrs)

def generate_files():
    """
    The above funstion geenerates 1 SimFile instance. This uses that to generate many.
    """
    pass