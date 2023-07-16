import streamlit as st
import pandas as pd
import pickle
from src.utils import *
from src.components import predict
from dataclasses import dataclass


st.header('Wine Predictions uploading the file.')
st.divider()

@dataclass
class Features:
    trained_model_file_path = trained_model_file_path
    uploaded_file = st.file_uploader('Choose the file.')
    if uploaded_file is not None:
        test_df = pd.read_csv(uploaded_file)
        st.write('File uploaded successfully.')
    else:
        st.write('Please upload the file.')
    


class Prediction:
    def __init__(self):
        self.prediction_config = Features()
        
    def file_prediction(self):
        model = pickle.load(open(self.prediction_config.trained_model_file_path,'rb'))
        #uploaded_file = st.file_uploader('Choose the file.')
        predictions = model.predict(self.prediction_config.test_df)
        return predictions
    

if st.button('Predict_file'):
    obj1 = Prediction()
    prediction_from_file = obj1.file_prediction()
    prediction_from_file = pd.DataFrame(prediction_from_file,columns=['Predictions'])
    st.divider()
    st.write('File prediction successfully.')
    st.dataframe(prediction_from_file)

    
    