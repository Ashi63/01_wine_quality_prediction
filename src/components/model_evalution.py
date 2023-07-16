from src.utils import *
from dataclasses import dataclass
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report


@dataclass
class ModelEvalutionConfig:
    prediction_file_path = prediction_file_path
    y_test_file_path = y_test_file_path
    
class ModelEvalution:
    def __init__(self):
        self.model_eval_config = ModelEvalutionConfig()
        
    def model_evalution(self):
        y_test_df = pd.read_csv(self.model_eval_config.y_test_file_path)
        y_predict_df = pd.read_csv(self.model_eval_config.prediction_file_path)
        evaluation_score = accuracy_score(y_test_df,y_predict_df)
        return evaluation_score
        
'''
if __name__ == '__main__':
    obj1 = ModelEvalution()
    obj1.model_evalution()
'''    