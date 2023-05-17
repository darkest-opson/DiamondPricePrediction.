from setuptools import find_packages,setup
from typing import List
hyphen_e_dot = '-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path,'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements


setup(
    name = "DiamondPricePrediction",
    version= '0.0.1',
    author="Prabhat tripathi",
    author_email= 'pmb2022001@iiita.ac.in',
    install_requires =get_requirements("requirements.txt") ,
    packages=find_packages()
)
# print(get_requirements('requirements.txt'))