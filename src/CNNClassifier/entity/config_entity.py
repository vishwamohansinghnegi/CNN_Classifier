from dataclasses import dataclass
from pathlib import Path

# Creating decorator and it is creating a immutable dataclass
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    Source_URL : str
    local_data_file : Path
    unzip_dir : Path