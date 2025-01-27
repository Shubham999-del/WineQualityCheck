from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_transformation import DataTransformation
from MLProject import logger

class DatatransformationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            config  = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            dataTransformation = DataTransformation(data_transformation_config)
            dataTransformation.train_test_spliting()
        except Exception as e:
            logger.error(f"error in training pipeline {str(e)}")
            raise e