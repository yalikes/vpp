from pathlib import Path
from typing import Tuple, Union
from ..constants import PROJECT_CONFIG_FILE_NAME


def check_file_exists(filename: Union[str, Path]) -> bool:
    project_file = Path(filename)
    return project_file.exists() and not project_file.is_dir()


def recursive_find_file(filename: Union[str, Path]) -> Tuple[bool, Path]:
    file_path = Path(filename)
    if check_file_exists(file_path):
        return (True, file_path)

    name = filename.name
    root_path = Path(file_path.absolute().root)
    current_path_dir = file_path.absolute().parent
    while current_path_dir != root_path:  # check file exists backward
        current_path_dir = current_path_dir.parent
        if check_file_exists(current_path_dir/name):
            return (True, current_path_dir/name)
    return (False, filename)


def get_project_root() -> Tuple[bool, Path]:
    (exists, root_config_file) = recursive_find_file(PROJECT_CONFIG_FILE_NAME)
    return (exists, root_config_file.parent)