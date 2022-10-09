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

    def __init__(self,config_file_path:str=CONFIG_FILE_PATH,curretn_time_stamp:str=CURRENT_TIME_STAMP) -> None:
         try:
                self.config_info=read_yaml_file(file_path=config_file_path)
                self.training_pipeline_config=self.get_training_pipeling_config()
                self.time_stamp=curretn_time_stamp
         except Exception as e:
                raise HousingException(e,sys) from e


    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
                artifact_dir=self.training_pipeline_config.artifact_dir

                data_ingestion_artifact_dir=os.path.join(artifact_dir,
                                                         DATA_INGESTION_ARTIFACT_DIR,
                                                                self.time_stamp)

                data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]

                dataset_download_url = data_ingestion_info[DATA_INGESTION_DATASET_URL_KEY]

                raw_data_dir=os.path.join(data_ingestion_artifact_dir,
                                                data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_EY])

                tgz_download_dir=os.path.join(data_ingestion_artifact_dir,
                                         data_ingestion_info['tgz_download_dir'])

                ingested_dir=os.path.join(data_ingestion_artifact_dir,
                                        data_ingestion_info[DATA_INGESTION_DIR_NAME_KEY])
                
                ingested_train_dir=os.path.join(ingested_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR])

                ingested_test_dir=os.path.join(ingested_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR])

                data_ingestion_dict=data_ingestion_info[DATA_INGESTION_CONFIG_KEY]
        
                data_ingestion_config=DataIngestionConfig(
                        dataset_download_url=dataset_download_url, 
                        tgz_download_dir=tgz_download_dir, 
                        raw_data_dir=raw_data_dir, 
                        ingested_train_dir=ingested_train_dir, 
                        ingested_test_dir=ingested_test_dir
                )
                
                logging.info("Data Ingestion Config: {data_ingestion_config}")
                return data_ingestion_config
        except Exception as e:
                raise HousingException(e,sys)


    def get_data_validation_config(self)->DataValidationConfig:
        try:
                pass
        except Exception as e:
                raise HousingException(e,sys)
    
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
                logging.info("training pipeline config [{training_pipeline_config}]" )
                return training_pipeline_config
            except Exception as e:
                raise HousingException(e,sys) from e
    