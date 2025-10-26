import os
import logging
import sys

log_dir = "logs"
log_filepath=os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s]: %(message)s]',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filepath)
        ]     
)
logger=logging.getLogger("cnnClassifierLogger") 