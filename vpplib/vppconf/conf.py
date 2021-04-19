from typing import Union
import tomlkit
from tomlkit.toml_document import TOMLDocument
from pathlib import Path
from ..constants import PROJECT_CONFIG_FILE_NAME


def write_vvp_toml_file(data: TOMLDocument, path: Union[str, Path]):
    content = tomlkit.dumps(data)
    file_path = Path(path)
    file_path.write_text(content, encoding="UTF8")


def read_vvp_toml_file(path: Union[str, Path]) -> TOMLDocument:
    file_path = Path(path)
    content = file_path.read_text()
    return tomlkit.parse(content)
