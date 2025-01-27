import os
import urllib.request as request
import zipfile
from MLProject import logger
from MLProject.entity.config_entity import DataIngestionConfig
from MLProject.utils import common

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file {filename}")

        else:
            logger.info(f"File already exists of size : {common.get_size(self.config.local_data_file)}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted {self.config.local_data_file} to {unzip_path}")
        except zipfile.BadZipFile:
            logger.error(f"Error: {self.config.local_data_file} is not a zip file")