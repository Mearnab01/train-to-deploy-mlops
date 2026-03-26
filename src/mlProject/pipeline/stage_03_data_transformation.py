from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_tarnsformation import DataTransformation
from src.mlProject import logger



STAGE_NAME = "Data Transformation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e