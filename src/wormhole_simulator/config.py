# config.py
"""
This module defines all user-configurable parameters for the Wormhole simulation.
Modify these to test different scenarios and network behaviors.
"""

# ----- Network Scale -----
TOTAL_SIMULATED_NODES = 1000         # Total number of nodes in the network
TOTAL_SIMULATED_FILES = 100          # Optional: total number of files to generate

# ----- Chunk/File Config -----
CHUNK_SIZE_MB = 10                   # Size of each chunk (MB)
REPLICATION_FACTOR = 10             # How many times each chunk should be replicated
FILE_EXPIRATION_TIME_MIN = 30       # When files/chunks expire or become obsolete (simulation time)

FILE_SIZE_RANGE_GB = (1, 5000)       # File sizes will be randomly selected from this range

# ----- Transfer Behavior -----
TRANSFER_FREQUENCY_MULTIPLIER = 1.0 # Used to scale how often nodes attempt file transfers
FILE_SEND_FREQUENCY_RANGE = (0.1, 1.0)  # Range of how aggressive a node is in initiating transfers (normalized)

# ----- Node Behavior -----
UPLOAD_SPEED_RANGE_MBPS = (10, 100)
DOWNLOAD_SPEED_RANGE_MBPS = (20, 150)
UPTIME_SCORE_RANGE = (1, 100)
STORAGE_RANGE_GB = (10, 1000)
SEND_LIMIT_RANGE_GB = (1, 50)

# ----- Simulation Behavior -----
NETWORK_CHURN_MULTIPLIER = 1.0      # Affects how often nodes go online/offline
NETWORK_RELIABILITY_MULTIPLIER = 1.0 # Affects chance of failures during transfer
SIM_TICK_INTERVAL_SEC = 1.0         # Real time between simulation ticks, for pacing if needed

# ----- Randomization / Determinism -----
RNG_SEED = 42                        # Seed for reproducible simulation behavior

