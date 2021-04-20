from vpplib.vppconf.file_item import ModuleFile


from pathlib import Path
from .constants import PROJECT_CONFIG_FILE_NAME, VPP_DESC_FILE
from .utils.utils import recursive_find_file
from .vppconf.conf import (
    read_json_file,
    read_vvp_toml_file,
    write_json_file)


def add_module_file_to_desc_file(module_file_item: ModuleFile):
    project_config_file = Path("./", PROJECT_CONFIG_FILE_NAME)
    vpp_desc_file = Path("./", VPP_DESC_FILE)
    (file_exists, config_file_path) = recursive_find_file(project_config_file)
    if not file_exists:
        print(
            f"error, {PROJECT_CONFIG_FILE_NAME} is not exists, this is not a vpp project directory")
        exit(-1)
    config = read_vvp_toml_file(config_file_path)
    files = read_json_file(vpp_desc_file)
    files["files"].append(module_file_item.to_record())
    write_json_file(files, vpp_desc_file)
