from MLProject.constants import *
from MLProject.utils.common import read_yaml,create_directories
from MLProject.entity.config_entity import DataIngestionConfig, DataTransformationConfig,DataValidationConfig, ModelEvaluationConfig, ModelTrainerConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIGFILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH,):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        create_directories([self.config.artifacts_root])
        

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config['data_ingestion']

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            source_URL=config['source_url'],
            local_data_file=config['local_data_file'],
            unzip_dir=config['unzip_dir']
        )

        return data_ingestion_config
    
    def get_data_validation_config(self)-> DataValidationConfig:
        config= self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:

        create_directories([self.config.model_trainer.root_dir])

        model_tranier_config = self.config.model_trainer
        params_config = self.params.ElasticNet
        schema_config = self.schema
        return ModelTrainerConfig(
            root_dir=model_tranier_config.root_dir,
            train_data_path=model_tranier_config.train_data_path,
            test_data_path=model_tranier_config.test_data_path,
            model_name=model_tranier_config.model_name,
            alpha=params_config.alpha,
            l1_ratio=params_config.l1_ratio,
            target_column=schema_config.TARGET_COLUMN
        )
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        model_evaluation_config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([model_evaluation_config.root_dir])
        return ModelEvaluationConfig(
            root_dir=model_evaluation_config.root_dir,
            test_data_path=model_evaluation_config.test_data_path,
            model_path = model_evaluation_config.model_path,
            all_params= params,
            metric_file_name=model_evaluation_config.metric_file_path,
            target_column=schema.name
        )
