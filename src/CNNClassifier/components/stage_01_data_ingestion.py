import os
import urllib.request as request    # For sending request to the server
from zipfile import ZipFile
from CNNClassifier import logger    # When we import from CNNClassifier it will 1st run '__init__.py'     
from tqdm import tqdm
from CNNClassifier.entity.config_entity import DataIngestionConfig

# For data ingestion

class DataIngestion:
    def __init__(self , config:DataIngestionConfig):  # type of config -> DataIngestionConfig
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file): # if it doesn't exists
            logger.info('trying to download file')
            request.urlretrieve(
                url = self.config.Source_URL,
                filename = self.config.local_data_file
            )    # request for data
        else:
            logger.info('file already exists')

    def get_updated_list_of_files(self , list_of_files):
        return [f for f in list_of_files if f.endswith('.jpg')]

    def preprocess(self , zf , f , working_dir):
        target_filepath = os.path.join(working_dir,f)
        if not os.path.exists(target_filepath):
            zf.extract(f , working_dir)

    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file , mode='r') as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self.get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):    # tqdm means we are going to showcase the progress
                self.preprocess(zf , f , self.config.unzip_dir)