from tkinter import E
from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig, \
                DataTranformationConfig,ModelEvaluationConfig,ModelPusherConfig,ModelTrainerConfig, TrainingPipelineConfig


from housing.util.util import read_yaml_file
import os
import sys

from housing.constant import *
from housing.exception import HousingException
from housing.logger import logging


class Configuration:

    def __init__(self,
    config_file_path:str=CONFIG_FILE_PATH,
    curretn_time_stamp:str=CURRENT_TIME_STAMP) -> None:
        self.config_info=read_yaml_file(file_path=config_file_path)
        self.training_pipeline_config=self.get_training_pipeling_config()
        self.time_stamp=curretn_time_stamp


    def get_data_ingestion_config(self)->DataIngestionConfig:
        pass

    def get_data_validation_config(self)->DataValidationConfig:
            pass
    
    def get_data_transformation_config(self)->DataTranformationConfig:
            pass

    def get_data_trainer_config(self)->ModelTrainerConfig:
            pass

    def get_data_evaluation_config(self)->ModelEvaluationConfig:
            pass
    
    def get_model_pusher_config(self)->ModelPusherConfig:
            pass
    
    def get_training_pipeling_config(self)->TrainingPipelineConfig:
            try:
                training_pipeline_config=self.config_info[TRAINING_PIPLEINE_CONFIG_KEY]
                artifact_dir=os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR])

                
                training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)
                logging.info("training pipeline config {training_pipeline_config}" )
                return training_pipeline_config
            except Exception as e:
                raise HousingException(e,sys) from e
    