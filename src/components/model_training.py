from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.utils import *
from sklearn.linear_model import LogisticRegression
import pickle


@dataclass
class ModelTrainingConfig:
    X_train_file_path = X_train_file_path
    X_test_file_path = X_test_file_path
    y_train_file_path = y_train_file_path
    y_test_file_path = y_test_file_path
    trained_model_file_path = trained_model_file_path
    
class ModelTraining:
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()

    def initiate_model_training(self):
        # load transformed data for training.
        X_train = pd.read_csv(self.model_training_config.X_train_file_path)
        X_test = pd.read_csv(self.model_training_config.X_test_file_path)
        y_train = pd.read_csv(self.model_training_config.y_train_file_path)
        y_test = pd.read_csv(self.model_training_config.y_test_file_path)
        
        # building the model
        model  = LogisticRegression()
        model.fit(X_train,y_train)
        if 'Models' not in os.listdir(artifacts_path):
            os.mkdir(artifacts_path/'models')
            pickle.dump(model,open(self.model_training_config.trained_model_file_path,'wb'))
        else:
            pickle.dump(model,open(self.model_training_config.trained_model_file_path,'wb'))

'''        
if __name__ == '__main__':
    obj1 = ModelTraining()
    obj1.initiate_model_training()
'''    
        
