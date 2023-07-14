import pandas as pd
import shutil 
from src.utils import *
from pathlib import Path
from sklearn.model_selection import train_test_split
import os
from dataclasses import dataclass
import os
  
@dataclass
class DataIngestionConfig:
    raw_data_file_path = raw_data_file_path
    training_data_path =  training_data_path
    training_data_file_path = training_data_path /'training_data.csv'
    testing_data_path = testing_data_path
    testing_data_file_path = testing_data_path /'testing_data.csv'
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        df = pd.read_csv(self.ingestion_config.raw_data_file_path)
        df.drop(['Id'],axis=1)
        training_data,testing_data = train_test_split(df,test_size=0.2,random_state=0)
        if 'training_data' not in os.listdir(data_source_path):
            os.mkdir(data_source_path /'training_data')
            training_data.to_csv(self.ingestion_config.training_data_file_path,index=False)
        if 'testing_data' not in os.listdir(data_source_path):
            os.mkdir(data_source_path / 'testing_data')
            testing_data.to_csv(self.ingestion_config.testing_data_file_path,index=False)
            

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
