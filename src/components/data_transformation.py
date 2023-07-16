import pandas as pd
import numpy as np
from src.utils import *
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
import os
from sklearn.model_selection import train_test_split

@dataclass
class DataTransformationConfig():
    training_data_file_path = training_data_file_path
    X_train_file_path = X_train_file_path
    X_test_file_path = X_test_file_path  
    y_train_file_path = y_train_file_path
    y_test_file_path = y_test_file_path

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()
        
    def initiate_data_transformation(self):
        # loading the training data.
        df_training = pd.read_csv(self.transformation_config.training_data_file_path)
        
        # removing the 'Id' column
        #df_training_transformed = df_training.drop(['Id'],axis=1)
        
        # checking for null values.
        #print('Null values in training data set: ',df_training_transformed.isnull().sum())
   
        # filling the null values.
        for i in df_training.isnull().sum():
            if i == 0:
                #print(f"No null values found.")
                df_training_transformed = df_training
            else:
                null_imputer = SimpleImputer(strategy='mean')
                df_training_transformed = null_imputer.fit_transform(df_training)
                print(type(df_training_transformed))
        
        
        # splitting the data into independent(X) and dependent(y) features.
        X = df_training_transformed.drop(['quality'],axis=1)
        y = df_training_transformed[['quality']]
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
        X_train = pd.DataFrame(X_train,columns=X.columns)
        y_train = pd.DataFrame(y_train,columns=y.columns)
        X_test = pd.DataFrame(X_test,columns=X.columns)
        y_test = pd.DataFrame(y_test,columns=y.columns)
        print(X_train.shape)
        print(y_train.shape)
        print(X_test.shape)
        print(y_test.shape)

        
        # scaling the data 
        scaler = StandardScaler()
        scaler.fit(X_train)
        X_train_scaled = scaler.transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        X_train = pd.DataFrame(X_train_scaled,columns=X_train.columns)
        X_test = pd.DataFrame(X_test_scaled,columns=X_test.columns)

        
        # create transformed_data folder and save transformed file.
        if 'transformed_data' not in os.listdir(data_source_path):
            os.mkdir(data_source_path /'transformed_data')
            X_train.to_csv(self.transformation_config.X_train_file_path,index=False)
            X_test.to_csv(self.transformation_config.X_test_file_path,index=False)
            y_train.to_csv(self.transformation_config.y_train_file_path,index=False)
            y_test.to_csv(self.transformation_config.y_test_file_path,index=False)
            
    
'''
if __name__=="__main__":
    obj1 = DataTransformation()
    obj1.initiate_data_transformation()
'''