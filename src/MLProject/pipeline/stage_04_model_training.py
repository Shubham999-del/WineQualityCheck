from MLProject.components.model_trainer import ModelTrainer
from MLProject.config.configuration import ConfigurationManager
from MLProject import logger



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config  = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            logger.error(e)
            raise e
