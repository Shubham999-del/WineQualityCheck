import os
from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
from MLProject.utils.common import save_json


class ModelEvaluation:
    def __init__(self,config):
        self.config = config
    
    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return (rmse,mae,r2)

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        predicted_values = model.predict(test_x)

        (rmse,mae,r2) = self.eval_metrics(test_y,predicted_values)

        scores = {"rmse" : rmse, "mae":mae, "r2_score": r2}
        save_json(path=Path(self.config.metric_file_name), data=scores)
