import streamlit as st
from src.components import predict
from src.components import model_evalution
import pandas as pd
import numpy as np
import pickle
from src.utils import *
from dataclasses import dataclass
import os


st.title('Wine Quality Prediction Manually.')
st.sidebar.success('Enter the data for the wine.')
st.divider()

@dataclass
class Features:
    fixed_acidity = st.number_input('fixed acidity')
    volatile_acidity = st.number_input('volatile acidity')
    citric_acid = st.number_input('citric acid')
    residual_sugar = st.number_input('residual sugar')
    chlorides = st.number_input('chlorides')
    free_sulfur_dioxide = st.number_input('free sulfur dioxide')
    total_sulfur_dioxide = st.number_input('total sulfur dioxide')
    density = st.number_input('density')
    pH = st.number_input('pH')
    sulphates = st.number_input('sulphates')
    alcohol = st.number_input('alcohol')
    trained_model_file_path = trained_model_file_path
    prediction_file_path = prediction_file_path
    prediction_from_manual_path = prediction_from_manual_path
    prediction_from_manual = prediction_from_manual
    
class PredictManually:
    def __init__(self):
        self.predict_manual_config = Features()
            
    def predict_manually(self):
        model = pickle.load(open(self.predict_manual_config.trained_model_file_path,'rb'))
        sample = np.array([self.predict_manual_config.fixed_acidity,self.predict_manual_config.volatile_acidity,self.predict_manual_config.citric_acid,self.predict_manual_config.residual_sugar,self.predict_manual_config.chlorides,self.predict_manual_config.free_sulfur_dioxide,self.predict_manual_config.total_sulfur_dioxide,self.predict_manual_config.density,self.predict_manual_config.pH,self.predict_manual_config.sulphates,self.predict_manual_config.alcohol])
        sample = sample.reshape(1,-1)
        columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                                        'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                                        'pH', 'sulphates', 'alcohol']
        sample = pd.DataFrame(sample,columns=columns)
        #return sample
        prediction_manual = model.predict(sample)
        prediction_manual = pd.DataFrame(prediction_manual,columns=['Predicted Quality'])
        return prediction_manual
    
    def record_sample(self):
        sample = np.array([self.predict_manual_config.fixed_acidity,self.predict_manual_config.volatile_acidity,self.predict_manual_config.citric_acid,self.predict_manual_config.residual_sugar,self.predict_manual_config.chlorides,self.predict_manual_config.free_sulfur_dioxide,self.predict_manual_config.total_sulfur_dioxide,self.predict_manual_config.density,self.predict_manual_config.pH,self.predict_manual_config.sulphates,self.predict_manual_config.alcohol])
        sample = sample.reshape(1,-1)
        columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                                        'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                                        'pH', 'sulphates', 'alcohol']
        sample = pd.DataFrame(sample,columns=columns)
        return sample
       
    def create_predictions_from_manual_folder(self):
        if self.predict_manual_config.prediction_from_manual not in os.listdir(self.predict_manual_config.prediction_file_path):
            os.makedirs(self.predict_manual_config.prediction_from_manual,exist_ok=True)
    
    def save_predicted_file(self):
        self.create_predictions_from_manual_folder()
        sample_df = self.record_sample()
        predictions = self.predict_manually()
        result_file = pd.concat([sample_df, predictions],axis=1)
        #st.dataframe(result_file)
        result_file.to_csv(self.predict_manual_config.prediction_from_manual_path,index=False)
        return result_file
        
st.divider()



if st.button('Predict and Save the file.'):
    st.divider()
    obj1 = PredictManually()
    test_sample_df = obj1.record_sample()
    #st.dataframe(test_sample_df)
    prediction = obj1.predict_manually()
    #st.dataframe(prediction)
    result_df = obj1.save_predicted_file()
    st.write('Your predicted result.')
    st.dataframe(result_df)
    st.success('Prediction Record Saved Successfully as csv file.')


