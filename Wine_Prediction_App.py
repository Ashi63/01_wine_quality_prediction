import streamlit as st
import pandas as pd
from src.utils import *


st.set_page_config(page_title='Wine Prediction')
st.title('Wine Prediction Application.')
st.sidebar.success('Select Any Page.')

st.divider()
st.subheader('Description:')
st.markdown('''
            This datasets is related to red variants of the Portuguese "Vinho Verde" wine.
            The dataset describes the amount of various chemicals present in wine and their effect on it's quality.
            The datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).''')
st.subheader('Task: ')
st.markdown('''Your task is to predict the quality of wine using the given data.''')

st.subheader('Objective:')
st.markdown('''
            - Understand the Dataset & cleanup (if required).
            
            - Build classification models to predict the wine quality.
            
            - Also fine-tune the hyperparameters & compare the evaluation metrics of various classification algorithms.''')

st.markdown('''
            ### This data frame contains the following columns:

            **Input variables (based on physicochemical tests):**
                
            1. fixed acidity
            2. volatile acidity
            3. citric acid
            4. residual sugar 
            5. chlorides
            6. free sulfur dioxide
            7. total sulfur dioxide
            8. density
            9. pH
            10. sulphates
            11. alcohol
                
            **Output variable (based on sensory data):**
                
            12. quality (score between 0 and 10)
            ''')

st.divider()
if st.button('Preview Sample Data'):
    sample_df = pd.read_csv(training_data_file_path)
    st.dataframe(sample_df.head(10))