from typing import Union
import tomlkit
from pathlib import Path
from ..constants import PROJECT_CONFIG_FILE_NAME


def write_vvp_toml_file(data: dict, path: Union[str,Path]):
    content=tomlkit.dumps(data)
    file_path=Path(path)
    file_path.write_text(content,encoding="UTF8")
