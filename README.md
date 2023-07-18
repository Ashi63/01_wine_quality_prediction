## Wine Quality Prediction Application 

![Alt text](/documents/images/wq.jpg)

**Description:**


        - This datasets is related to red variants of the Portuguese "Vinho Verde" wine.
        - The dataset describes the amount of various chemicals present in wine 
          and their effect on it's quality.
        - The datasets can be viewed as classification or regression tasks. 
        - The classes are ordered and not balanced
            (e.g. there are much more normal wines than excellent or poor ones).


**Task:** 

        - Your task is to predict the quality of wine using the given data.

**Objective:**



        - Understand the Dataset & cleanup (if required).
            
        - Build classification models to predict the wine quality.
            
        - Also fine-tune the hyperparameters & compare the evaluation metrics 
          of various classification algorithms.



**This data frame contains the following columns:**

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

**Application Preview**

![Alt text](/documents/images/app_home_page.png)

![Alt text](/documents/images/batch_prediction.png)

![Alt text](/documents/images/manual_prediction.png)

![Alt text](/documents/images/see_prediction.png)

**AWS Deployment in EC2 instance**
- Create a EC2 instance(Amazon Linux) in AWS.
- Upload the project files to the instance (using WinSCP tool).
- SSH to your instance
        - install python using command '''sudo yum install python3'''
        - check the version of python installed '''python3 -V'''
        - create a environment for the application '''python -m venv .venv'''
        - activate the environment '''source .venv/bin/activate'''
        - install all the packages using the requirements.txt file '''pip3 install -r requirements.txt'''
        - to run the application '''streamlit run application.py'''