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
def read_yaml(path_to_yaml: Path) ->  ConfigBox:
    """
        reads yaml file and returns the data
        Args:
            path_to_yaml: path to yaml file
        Returns
            ConfigBox object
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"reading the config file from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml File is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
        creates list of directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """
        returns the size of the object
    """
    size = round(os.path.getsize(path)/1024)
    return f"~{size} KB"

@ensure_annotations
def save_json(path: Path,data: dict, verbose=True):
    with open(path,'w') as f:
        json.dump(data,f)

    logger.info(f"json file saved at {path}")

