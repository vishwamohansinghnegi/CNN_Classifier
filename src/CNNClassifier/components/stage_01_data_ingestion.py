import os
import urllib.request as request    # For sending request to the server
from zipfile import ZipFile
from CNNClassifier import logger    # When we import from CNNClassifier it will 1st run '__init__.py'     
from tqdm import tqdm
from CNNClassifier.entity.config_entity import DataIngestionConfig
from PIL import Image


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
        
        # Calling the cleaning function after unzipping
        self.clean_dataset(self.config.unzip_dir)

    def clean_dataset(self, dataset_path):
        logger.info(f"Cleaning dataset in: {os.path.abspath(dataset_path)}")
        for class_dir in os.listdir(dataset_path):
            class_dir_path = os.path.join(dataset_path, class_dir)
            if os.path.isdir(class_dir_path):
                for img_file in os.listdir(class_dir_path):
                    img_path = os.path.join(class_dir_path, img_file)
                    try:
                        with Image.open(img_path) as img:
                            img.verify()  # Will throw an exception if the image is not valid
                    except (IOError, SyntaxError):
                        logger.info(f"Deleting corrupted image: {img_path}")
                        os.remove(img_path)  # Remove corrupted images