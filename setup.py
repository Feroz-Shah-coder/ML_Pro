from setuptools import find_packages, setup
from typing import List

hy_e_dot = '-e .'
def git_requirements(file_path:str)->List[str]:
    ## return the req list 
    requirements = []
    with open(file_path) as file_boj:
        requirements = file_boj.readlines()
        requirements = [req.replace("\n","" ) for req in requirements]
        if hy_e_dot in requirements:
            requirements.remove(hy_e_dot)
    return requirements
setup(
    name='Ml project',
    version='0.0.1',
    author="Feroz",
    author_email="ferozalimze@gmail.com",
    packages=find_packages(),
   install_requires=git_requirements("requirements.txt")
    
)