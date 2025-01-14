from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<<<<")
    Data_ingestion = DataIngestionTrainingPipeline()
    Data_ingestion.main()
    logger.info(f">>>>>>>>>>>{STAGE_NAME} completed <<<<<<\n\nx==================x")
except Exception as e:
    logger.exception(e)
    raise e