# config.py
"""
This module defines all user-configurable parameters for the Wormhole simulation.
Modify these to test different scenarios and network behaviors.
"""

# ----- Network Scale -----
TOTAL_SIMULATED_NODES = 10000         # Total number of nodes in the network
NEW_FILE_CREATION_INTERVAL_MIN = 20   # average interval between new file creations per node

# ----- Chunk/File Config -----
CHUNK_SIZE_MB = 10                   # Size of each chunk (MB)
REPLICATION_FACTOR = 10             # How many times each chunk should be replicated
FILE_EXPIRATION_TIME_MIN = 30       # When files/chunks expire or become obsolete (simulation time)

FILE_SIZE_RANGE_GB = (.1, 50)       # File sizes will be randomly selected from this range

# ----- Transfer Behavior -----
UPLOAD_FREQUENCY_RANGE = (5, 120) # (minutes) Used to scale how often nodes attempt file uploads

# ----- Node Behavior -----
UPLOAD_SPEED_RANGE_MBPS = (10, 100)
DOWNLOAD_SPEED_RANGE_MBPS = (20, 150)
UPTIME_SCORE_RANGE = (1, 100)
STORAGE_RANGE_GB = (10, 1000)
SEND_LIMIT_RANGE_GB = (1, 50)

# ----- File Manager Settings (Minutes) -----
UPDATE_FILE_MAP_FREQUENCY = .25
CHECK_AWAITING_UPLOAD_LIST_FREQUENCY = .25
CHECK_AWAITING_REPLICATION_LIST_FREQUENCY = .25
CHECK_AWAITING_NOTIFY_LIST_FREQUENCY = 1
CHECK_REPAIR_CHUNKS_LIST_FREQUENCY = .25
CHECK_DELETE_OBSOLETE_CHUNKS_LIST_FREQUENCY = 5
CHECK_EXPIRED_FILES_LIST_FREQUENCY = 1
TRANSFER_CHUNKS_TO_RECIPIENTS_FREQUENCY = 1

# ----- Simulation Behavior -----
NETWORK_CHURN_MULTIPLIER = 1.0      # Affects how often nodes go online/offline
NETWORK_RELIABILITY_MULTIPLIER = 1.0 # Affects chance of failures during transfer
SIM_TICK_INTERVAL_SEC = 1.0         # Real time between simulation ticks, for pacing if needed

# ----- Randomization / Determinism -----
RNG_SEED = 236                        # Seed for reproducible simulation behavior

