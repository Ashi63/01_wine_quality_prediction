import streamlit as st
import pandas as pd
import pickle
from src.utils import *
from src.components import predict
from dataclasses import dataclass
import os


st.title('Predict uploading the batch file.')
st.sidebar.success('Upload your batch file to be Predicted.')
st.divider()

@dataclass
class Features:
    trained_model_file_path = trained_model_file_path
    prediction_file_path = prediction_file_path
    prediction_from_file = prediction_from_file
    prediction_from_file_path = prediction_from_file_path
    uploaded_file = st.file_uploader('Choose the file.')
    if uploaded_file is not None:
        test_df = pd.read_csv(uploaded_file)
        st.success('File uploaded successfully.')
        
    


class Prediction:
    def __init__(self):
        self.prediction_config = Features()
    
    def record_sample_df(self):
        test_df = self.prediction_config.test_df
        return test_df
        
    
    def file_prediction(self):
        model = pickle.load(open(self.prediction_config.trained_model_file_path,'rb'))
        test_df = self.record_sample_df()
        #st.dataframe(test_df)
        predictions = model.predict(test_df)
        predictions = pd.DataFrame(predictions,columns=['Predicted Quality'])
        return predictions
    
    def create_prediction_from_file_folder(self):
        if 'prediction_from_file' not in os.listdir(self.prediction_config.prediction_file_path):
            os.makedirs(self.prediction_config.prediction_from_file,exist_ok=True)
             
    
    def save_prediction_file(self):
        test_dataframe = self.prediction_config.test_df
        predictions_dataframe = self.file_prediction()
        result_df = pd.concat([test_dataframe, predictions_dataframe],axis=1)
        st.write('Predicted dataframe.')
        self.create_prediction_from_file_folder()
        result_df.to_csv(self.prediction_config.prediction_from_file_path,index=False)
        return result_df

st.divider()

if st.button('Predict and Save the Prediction'):
    obj1 = Prediction()
    sample_df = obj1.record_sample_df()
    #st.dataframe(sample_df)
    predictions = obj1.file_prediction()
    #st.dataframe(predictions)
    result = obj1.save_prediction_file()
    st.dataframe(result)
    st.success('Prediction Record Saved Successfully as csv file.')

    
    