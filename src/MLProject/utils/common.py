import os
from box.exceptions import BoxValueError
import yaml
from MLProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(Path: str) -> Any:
    """
    Read yaml file
    :param Path: str: Path of yaml file
    :return: Any: Data from yaml file
    """
    with open(Path, "r") as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            logger.error(f"Error reading the yaml file : {e}")
            raise BoxValueError(f"Error reading the yaml file : {e}")
    return data