from setuptools import setup,find_packages
from typing import List


REQ_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
        Description:Returns list of string from requirements.txt file

        this functon is going to return a list which will contain name of libraries mentioned
        in requirements.txt file    
    """
    with open(REQ_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')

setup(
    name="housing-predictor",
    version="0.0.1",
    author="GnaneshGn",
    description="This is house price prediction Machine Learning project",
    packages=find_packages(),
    license="Apache license version 2.0",
    install_requires=get_requirements_list()
)