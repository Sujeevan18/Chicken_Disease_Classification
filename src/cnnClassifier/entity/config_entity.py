# src/cnnClassifier/entity/config_entity.py
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Dict, Union

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

