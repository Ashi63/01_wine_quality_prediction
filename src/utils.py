import os
from pathlib import Path

project_dir_path        = Path('C:/Users/Alkashi/Desktop/demo_ds_apps/01_wine_quality_prediction/')
artifacts_path          = project_dir_path/'artifacts'
data_source_path        = artifacts_path /'data_source'
training_data_path      = data_source_path/'training_data'
training_data_file_path = training_data_path / 'training_data.csv'
testing_data_path       = data_source_path/'testing_data'
testing_data_file_path  = testing_data_path / 'testing_data.csv'
raw_data_path           = project_dir_path /'raw_data'
raw_data_file_path      = raw_data_path / 'WineQT.csv'
transformed_data_path   = data_source_path / 'transformed_data'
X_train_file_path       = transformed_data_path/'X_train_data.csv'
X_test_file_path        = transformed_data_path/'X_test_data.csv'
y_train_file_path       = transformed_data_path/'y_train_data.csv'
y_test_file_path        = transformed_data_path/'y_test_data.csv'
prediction_path         = artifacts_path/'predictions'
prediction_file_path    = prediction_path/'predictions.csv'
trained_model_path      = artifacts_path/ 'models'
trained_model_file_path = trained_model_path /'model.pkl'
