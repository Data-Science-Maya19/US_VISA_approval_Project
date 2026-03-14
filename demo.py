from US_VISA_Approval_Prediction.logger import logging
from US_VISA_Approval_Prediction.exception import US_VISA_Approval_Exception
import sys  

logging.info("Welcome to custom logs")

try:
    a = 2/0
except Exception as e:
    logging.info("We are dividing by zero")
    raise US_VISA_Approval_Exception(e, sys)