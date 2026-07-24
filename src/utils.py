import os 
import sys
import numpy as np 
import pandas as pd 
import dill 

from src.exception import CustomException


def save_object(file_path, obj):
    try:

        # Get the directory from the file path
        dir_path = os.path.dirname(file_path)

        # Create the directory if it does not exist
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in write-binary mode
        with open(file_path, "wb") as file_obj:

            # Save (serialize) the Python object
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)