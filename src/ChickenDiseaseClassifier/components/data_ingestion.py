import os
import zipfile
from pathlib import Path
import urllib.request as request
from ChickenDiseaseClassifier.constants import *
from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.utils.common import create_directories, read_yaml, get_size
from ChickenDiseaseClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):           
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_file)
            logger.info(f"{filename} download! with the following information:\n{headers}")

        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info("Data unzipped")
    
  