import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)  # Fix typo in os.makedirs

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,  # Add a comma here
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("wineClassifierLogger")
