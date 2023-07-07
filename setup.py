from setuptools import setup,find_packages
from typing import List


HYPEN_E_DOT = '-e .'
# funtion to get the list of requirements
def get_requirements(file_path:str)->List[str]:
    '''
        This function returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
        

setup(
    name = 'wine_quality_prediction',
    version = '0.1',
    description = 'Application for the prediction of wine quality.',
    author = 'Ashish Khobragade',
    author_email = 'ashish.ashi6388@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)




