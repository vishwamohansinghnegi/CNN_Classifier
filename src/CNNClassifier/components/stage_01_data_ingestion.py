import os
import urllib.request as request    # For sending request to the server
from zipfile import ZipFile
from CNNClassifier import logger    # When we import from CNNClassifier it will 1st run '__init__.py'     
from pathlib import Path
from tqdm import tqdm
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.utils import utils

# For data ingestion

class DataIngestion:
    def __init__(self , config:DataIngestionConfig):  # type of config -> DataIngestionConfig
        self.config
        pass

    def download_file(self):
        pass

    def get_updated_list_of_files(self):
        pass

    def preprocess(self):
        pass

    def unzip_and_clean(self):
        pass