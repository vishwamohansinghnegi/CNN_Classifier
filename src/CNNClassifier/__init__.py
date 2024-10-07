import os
import sys
import logging

# 1st we define format of logging message -> it will give time , level name , module name & message
logging_format = '[%(asctime)s: %(levelname)s: %(module)s]: %(message)s'
log_dir = 'logs'     # Directory for logs
log_filepath = os.path.join(log_dir,'running_logs.log')   # For creating logs in this file
os.mkdir(log_dir , exist_ok=True)

logging.basicConfig(          # Configuration of logging
    level = logging.INFO,       # level of logging
    format=logging_format,      # format of message
    handlers=[         # Creating 2 handlers -> one for file & other for cmd
        logging.FileHandler(log_filepath),     
        logging.StreamHandler(sys.stdout)# whatever logs we capture in file will be available in cmd prmt
    ]
)
logging.getLogger('CNNClassifier') 