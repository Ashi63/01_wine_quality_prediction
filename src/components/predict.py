from src.utils import *
import pandas as pd
import numpy as np
from dataclasses import dataclass
import pickle

@dataclass
class PredictionConfig:
    trained_model_file_path = trained_model_file_path
    X_test_file_path = X_test_file_path
    prediction_file_path = prediction_file_path
    artifacts_path = artifacts_path
    
class Prediction:
    def __init__(self):
        self.prediction_config = PredictionConfig()
        
    def predict(self):
        # loading the model.
        model = pickle.load(open(self.prediction_config.trained_model_file_path,'rb'))
        X_test = pd.read_csv(self.prediction_config.X_test_file_path)
        print(X_test.shape)
        # making the prediction through the model.
        prediction =  model.predict(X_test)    
        prediction = pd.DataFrame(prediction,columns=['Predictions'])
        # creating a prediction folder to save the predictions.
        if 'predictions' not in os.listdir(artifacts_path):
            os.mkdir(artifacts_path/'predictions')
            prediction.to_csv(self.prediction_config.prediction_file_path,index=False)
        else:
            prediction.to_csv(self.prediction_config.prediction_file_path,index=False)
        
        
if __name__=='__main__':
    obj1= Prediction()
    obj1.predict()    
    