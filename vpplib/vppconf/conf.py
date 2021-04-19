from typing import Union
from pathlib import Path
import json

import toml
from ..constants import PROJECT_CONFIG_FILE_NAME


def write_vvp_toml_file(data: dict, path: Union[str, Path]):
    content = toml.dumps(data)
    file_path = Path(path)
    file_path.write_text(content, encoding="UTF8")


def read_vvp_toml_file(path: Union[str, Path]) -> dict:
    file_path = Path(path)
    content = file_path.read_text()
    return toml.loads(content)


def write_json_file(data: dict, path: Union[str, Path]):
    content = json.dumps(data)
    file_path = Path(path)
    file_path.write_text(content)


def read_json_file(path: Union[str, Path]) -> dict:
    file_path = Path(path)
    content = file_path.read_text()
    return json.loads(content)
