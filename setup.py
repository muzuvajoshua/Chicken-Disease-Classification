import setuptools
# from typing import List

HYPHEN_E_DOT = '-e .'
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = '0.0.0'
REPO_NAME = 'Chicken-Disease-Classification'
AUTHOR_USER_NAME = 'muzuvajoshua'
SRC_REPO ='ChickenDiseaseClassifier'
AUTHOR_EMAIL ='muzuvajoshua@gmail.com'

# def get_requirements(file_path:str)->List[str]:
#     '''
#     This returns a list of requirements from a file path
    
#     '''
#     requirements =[]
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [requirement.replace('\n','') for requirement in requirements]

#     if HYPHEN_E_DOT in requirements:
#         requirements.remove(HYPHEN_E_DOT)

#     return requirements

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "A small pyhton package for classifying chicken diseases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url =f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)