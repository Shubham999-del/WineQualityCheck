from MLProject import logger
from MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLProject.pipeline.stage_03_data_transformation import DatatransformationTrainingPipeline
from MLProject.pipeline.stage_04_model_training import ModelTrainingPipeline
from MLProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

logger.info("Welcome to ML Project")


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"Starting {STAGE_NAME}")
    dataIngestion = DataIngestionTrainingPipeline()
    dataIngestion.main()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {str(e)}")
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f"Starting {STAGE_NAME}")
    dataValidation = DataValidationTrainingPipeline()
    dataValidation.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {str(e)}")
    raise e


STAGE_NAME = "Data Transformation"
try:
    logger.info(f"Starting {STAGE_NAME}")
    dataTransformation = DatatransformationTrainingPipeline()
    dataTransformation.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {str(e)}")
    raise e

STAGE_NAME = "Model Training"
try:
    logger.info(f"Starting {STAGE_NAME}")
    modelTraining = ModelTrainingPipeline()
    modelTraining.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e: 
    logger.error(f"Error in {STAGE_NAME}: {str(e)}")
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"Starting : {STAGE_NAME}")
    modelEvaluationPipeline = ModelEvaluationPipeline()
    modelEvaluationPipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} : {str(e)}")


