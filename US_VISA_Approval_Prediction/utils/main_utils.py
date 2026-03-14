import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from US_VISA_Approval_Prediction.exception import US_VISA_Approval_Exception
from US_VISA_Approval_Prediction.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise US_VISA_Approval_Exception(e, sys)


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    if replace:
        if os.path.exists(file_path):
            os.remove(file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, "w") as yaml_file:
            yaml.dump(content, yaml_file)
    except Exception as e:
        raise US_VISA_Approval_Exception(e, sys)
    

# Load any pickle or binary object
def load_object(file_path: str) -> object:
    logging.info(f"Entered the load_object method of Main_utils class for file path: {file_path}")
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
        logging.info(f"Exited the load_object method of Main_utils class for file path: {file_path}")
    except Exception as e:
        raise US_VISA_Approval_Exception(e, sys)
    

# save any numpy array data from file
def save_numpy_array_data(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise US_VISA_Approval_Exception(e, sys)
    

def load_numpy_array_data(file_path: str) -> np.array:
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise US_VISA_Approval_Exception(e, sys)
    

def save_object(file_path: str, obj: object) -> None:
    logging.info(f"Entered the save_object method of Main_utils class for file path: {file_path}")
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Exited the save_object method of Main_utils class for file path: {file_path}")
    except Exception as e:
        raise US_VISA_Approval_Exception(e, sys)
    

# drop columns from dataframe and return the dataframe
def drop_columns(df: DataFrame, columns: list) -> DataFrame:
    logging.info(f"Entered the drop_columns method of Main_utils class for columns: {columns}")
    try:
        df = df.drop(columns=columns, axis=1)
        logging.info(f"Exited the drop_columns method of Main_utils class for columns: {columns}")
        return df
    except Exception as e:
        raise US_VISA_Approval_Exception(e, sys)