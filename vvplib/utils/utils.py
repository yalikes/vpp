from pathlib import Path
from typing import Union


def check_file_exists(filename: Union[str, Path]) -> bool:
    project_file = Path(filename)
    return project_file.exists() and not project_file.is_dir()
