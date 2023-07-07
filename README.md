# 01_wine_quality_prediction
Wine quality prediction application.

## Steps to start a project

1.Create a git repository for the project.

	- .gitignore
	- README.md
	- LICENSE

2.Clone the repository to local machine.

    <git clone 'repository url'>

3.Create a set up file.
    
4.Create a requirements.txt file.

	<pandas,
    scikit-learn,
    seaborn,
    streamlit>
    #### this -e . is so that setup.py file will also run when ever we intall the requirements.txt file.
    -e .>

5.Create a src folder with the __init__.py file in it.

    - __init__.py
    - components
        - __init__.py
        - data_ingestion.py
        - data_transformation.py
        - model_training.py
    - pipeline
        - __init__.py
        - training_pipeline.py
        - prediction_pipeline.py
    - exception.py
    - logger.py
    - utils.py

6.Install Packages from the requirements.txt file.

    <pip install -r requirements.txt>

7.Make 'artifacts' dir to store  which will be created during the project.
    
    - data_source
        - raw_data
        - training_data
        - testing_data
    - models


