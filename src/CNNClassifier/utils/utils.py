# These functions will used everywhere in the project so we don't have to write them again and again
import os
import yaml
import json
import joblib
from pathlib import Path
from CNNClassifier import logger
from typing import Any
from ensure import  ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox

# using this '@ensure_annotations' decorator for every function
@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        return ConfigBox(content)    # using 'ConfigBox so that it consider 'content' as dictionary

@ensure_annotations
def save_json():
    pass

@ensure_annotations
def load_json():
    pass

@ensure_annotations
def save_model():
    pass

@ensure_annotations
def load_model():
    pass

@ensure_annotations
def get_size():
    pass

@ensure_annotations
def create_dir(path_to_dir:list , verbose=True):
    for path in path_to_dir:
        os.makedirs(path , exist_ok=True)
        if verbose:
            logger.info(f'create directory at : {path}')
