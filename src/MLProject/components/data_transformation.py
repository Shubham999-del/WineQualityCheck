import os
from MLProject import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from MLProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        le = LabelEncoder()
        for col in data.select_dtypes(include=['object']).columns:
            data[col] = le.fit_transform(data[col])

        train,test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info(f"train and test data saved at {self.config.root_dir}")
        logger.info(train.shape)
        logger.info(test.shape)
        