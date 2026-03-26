from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

# 1: Data ingestion stage
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage1: {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage1: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
# 2: Data validation stage
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage2: {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage2: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
# 3: Data transformation stage
STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage3: {STAGE_NAME} started <<<<<<") 
   data_transformation = DataValidationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage3: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
# 4: Model trainer stage
STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage4: {STAGE_NAME} started <<<<<<") 
   model_trainer = ModelTrainerPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage4: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
# 5: Model evaluation stage
STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f"#=====#======# stage5: {STAGE_NAME} started #=====#======#") 
   model_evaluation = ModelEvaluationPipeline()
   model_evaluation.main()
   logger.info(f"#=====#======# stage5: {STAGE_NAME} completed #=====#======#\n\nx<<<<<<<x")
except Exception as e:
        logger.exception(e)
        raise e
     
