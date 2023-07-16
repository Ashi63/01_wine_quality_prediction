import streamlit as st
from src.components import predict
from src.components import model_evalution
import pandas as pd
import numpy as np
import pickle
from src.utils import *
from dataclasses import dataclass
import os

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
        
st.divider()

def get_sample_prediction_manual():
    obj2 = PredictManually()
    sample = obj2.record_sample()
    #st.dataframe(sample)
    obj1 = PredictManually()
    prediction_manual = obj1.predict_manually()
    #st.dataframe(prediction_manual) 
    return sample,prediction_manual




if st.button('Show the record and make prediction'):
    obj2 = PredictManually()
    sample = obj2.record_sample()
    st.dataframe(sample)   
    
    obj1 = PredictManually()
    prediction_manual = obj1.predict_manually()
    st.dataframe(prediction_manual)
    


if st.button('Save the Prediction.'):
    sample,prediction_manual = get_sample_prediction_manual()
    result_file = pd.concat([sample,prediction_manual],axis=1)
    st.dataframe(result_file)
        
    if 'prediction_from_manual' not in os.listdir(prediction_file_path):
        os.mkdir(prediction_file_path/'prediction_from_manual')
        result_file.to_csv(prediction_from_manual_path)
        st.write('Result file saved successfully.')




    #st.dataframe(result_file)

