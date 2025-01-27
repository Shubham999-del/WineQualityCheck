from MLProject import logger
from MLProject.components.model_evaluation import ModelEvaluation
from MLProject.config.configuration import ConfigurationManager


class ModelEvaluationPipeline:
    def __init__(self):
        self
        
    def main(self):
        try:
            config = ConfigurationManager()
            model_eval_config = config.get_model_evaluation_config()
            model_eval = ModelEvaluation(config=model_eval_config)
            model_eval.save_results()
        except Exception as e:
            logger.error(f"Error occured : {e}")
            raise e