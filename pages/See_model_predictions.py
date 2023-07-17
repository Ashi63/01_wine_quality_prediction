import streamlit as st
import pandas as pd
import pickle
from src.utils import *
from src.components import predict
from dataclasses import dataclass
import os


st.title('See your predictions.')
st.sidebar.success('See your Predictions.')
st.divider()


uploaded_file = st.file_uploader('Show the predicted files.')
st.divider()
if st.button('Click here to see the predictions.'):
    if uploaded_file is not None:
        st.success('File uploaded successfully.')
        predicted_df = pd.read_csv(uploaded_file)
        
        st.dataframe(predicted_df)