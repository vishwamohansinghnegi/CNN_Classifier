# For creating local packages -> we can make these package public also  

import setuptools

__version__ = '0.0.1'

with open('README.md' , 'r' , encoding='utf-8') as f:
    long_description = f.read()

REPO_NAME = 'CNN_Classifier'
AUTHOR_NAME = 'Vishwamohan Singh Negi'
SRC_REPO = 'src/CNNClassifier'
AUTHOR_Email = 'vishwamohansinghnegi@gmail.com'

setuptools.setup(
    name = SRC_REPO,   # which folder we are converting to package
    version = __version__,    # Version we are going to write
    author = AUTHOR_NAME,
    author_email = AUTHOR_Email,
    description = 'This is my classification project',
    long_description = long_description,
    long_description_content = 'test/markdown',
    url = f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',

    project_urls = {
        'Bug Tracker' : f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues',
    },
    package_dir = {'' : 'src'},
    packages = setuptools.find_packages(where='src')
) 