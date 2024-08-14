import logging

def setup_logger():
    logging.basicConfig(filename='employee_management.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()

logger = setup_logger()

#Integrate logging in existing functions
from logger import logger

# In add_employee function:
logger.info(f"Attempting to add employee with Id: {Id}")