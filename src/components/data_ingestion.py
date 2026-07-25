import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass ## (( Used to class variables ))

from src.components.data_transfermation import DataTransformation
from src.components.data_transfermation import DataTransformationConfig
## that are the modular coding here in the python 

from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

@dataclass

class DataIngestionConfig:
    train_data_path = str = os.path.join('artificts', 'train.csv')
    test_data_path = str = os.path.join('artificts', 'test.csv') 
    raw_data_path = str = os.path.join('artificts', 'data.csv') 

class DataIngestion:
    def __init__(self):
        self.data_ingestion = DataIngestionConfig()

    def initaite_data_ingestion(self):
        logging.info("Enterd the data ingestion components or method ")
        try:
            df = pd.read_csv("notebook\data\StudentsPerformance.csv")
            logging.info("Read data from DataFram")
            
            os.makedirs(os.path.dirname(self.data_ingestion.train_data_path), exist_ok= True)


            df.to_csv(self.data_ingestion.raw_data_path, index=False, header= True)
            logging.info("Train Test split Initiate ")

            train_set , test_set = train_test_split(df , test_size= 0.2, random_state=42)

            train_set.to_csv(self.data_ingestion.train_data_path, index= False, header = True )
            test_set.to_csv(self.data_ingestion.test_data_path, index= False, header = True )

            logging.info("Data Ingestion are completed ")
            
            return(
                self.data_ingestion.train_data_path,
                self.data_ingestion.test_data_path, 

            )

        except Exception as e:
            raise CustomException(e, sys )


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initaite_data_ingestion()

    data_transfermation = DataTransformation()
    train_arr, test_arr = data_transfermation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))


