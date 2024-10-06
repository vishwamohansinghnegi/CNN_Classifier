import os
from pathlib import Path
import logging

# This sets the logging level to INFO and specifies a format for the log messages 
# where the timestamp (asctime) and the log message (message) are displayed.
logging.basicConfig(level=logging.INFO , format='[%(asctime)s:%(message)s])')

# Creating package name
package_name = 'CNN_Classifier'

# List of file
list_of_files = [
    ".github/workflows/.gitkeep",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)  #  Using 'Path' to remove conflict of path
    # As it converts path according to OS . Windows use backslash'\' while Linux use forward slash'/'
    filedir , filename = os.path.split(filepath)   # For getting file directory and file name

    if filedir:   #  Create directory if it exist for a file (if not then it will return empty string)
        os.makedirs(filedir , exist_ok=True)  # Creating directories
        logging.info(f'creating directory : {filedir} for the file : {filename}')  # logging the information

    # Creating files
    if (not os.path.exists(filepath)) or (os.filepath.get_size(filepath)==0):
        with open(filepath , 'w'):   # opening file in write mode as it creates file if it doesn't exist
            logging.info(f'creating empty file : {filepath}')
            pass
    # if file already exists
    else:
        logging.info(f'{filepath} already exists')