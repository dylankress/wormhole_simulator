# config.py
"""
This module defines all user-configurable parameters for the Wormhole simulation.
Modify these to test different scenarios and network behaviors.
"""

# ----- Network Scale -----
TOTAL_SIMULATED_NODES = 10000
NEW_FILE_CREATION_INTERVAL_MIN = 20

# ----- Chunk/File Config -----
CHUNK_SIZE_MB = 10
REPLICATION_FACTOR = 10
FILE_EXPIRATION_TIME_MIN = 30
FILE_SIZE_RANGE_GB = (.1, 50)

# ----- Transfer Behavior -----
UPLOAD_FREQUENCY_RANGE = (5, 120)

# ----- Node Behavior -----
UPLOAD_SPEED_RANGE_MBPS = (10, 100)
DOWNLOAD_SPEED_RANGE_MBPS = (20, 150)
UPTIME_SCORE_RANGE = (1, 100)
STORAGE_RANGE_GB = (10, 1000)
SEND_LIMIT_RANGE_GB = (1, 50)
SEND_LIMIT_RECOVERY_RATE_GB_PER_TICK = 0.004

# ----- File Manager Settings (Minutes) -----
UPDATE_FILE_MAP_FREQUENCY = .25
PROCESS_AWAITING_UPLOAD_LIST_FREQUENCY = .25
PROCESS_AWAITING_REPLICATION_LIST_FREQUENCY = .25
PROCESS_AWAITING_NOTIFY_LIST_FREQUENCY = 1
PROCESS_REPAIR_CHUNKS_LIST_FREQUENCY = .25
PROCESS_DELETE_OBSOLETE_CHUNKS_LIST_FREQUENCY = 5
PROCESS_EXPIRED_FILES_LIST_FREQUENCY = 1
TRANSFER_CHUNKS_TO_RECIPIENTS_FREQUENCY = 1

# ---- Node Churn Behavior ----
ONLINE_WEIGHT_EXPONENT = 2.0     # Higher = even more likely to bring high-uptime nodes online
OFFLINE_WEIGHT_EXPONENT = 2.0    # Higher = even more likely to kick low-uptime nodes offline
NETWORK_CHURN_MULTIPLIER = 1.0   # 1.0 = baseline 5% churn, 2.0 = 10%, etc.

# ----- Simulation Behavior -----
SIM_TICK_INTERVAL_SEC = 1.0

# ----- Randomization / Determinism -----
RNG_SEED = 736

