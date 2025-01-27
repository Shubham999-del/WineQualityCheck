import os
from MLProject import logger
from MLProject.components.data_validation import DataValidation
from MLProject.config.configuration import ConfigurationManager

class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            logger.error(f"Error in Data Validation: {str(e)}")
            raise e