import os
import urllib.request as request
import zipfile
from MLProject import logger
from MLProject.config.configuration import ConfigurationManager
from MLProject.entity.config_entity import DataIngestionConfig
from MLProject.utils import common
from MLProject.components.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e
