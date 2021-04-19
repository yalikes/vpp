import argparse
from pathlib import Path
from vpplib.utils.utils import check_file_exists, recursive_find_file
from vpplib.vppconf.conf import read_vvp_toml_file, write_vvp_toml_file
from vpplib.constants import PROJECT_CONFIG_FILE_NAME


def init_command(args: argparse.Namespace):
    project_config_file = Path("./", PROJECT_CONFIG_FILE_NAME)
    if check_file_exists(project_config_file):
        print(f"error, {PROJECT_CONFIG_FILE_NAME} alread exists! exit.")
        exit(-1)
    # basic config file here
    config = {
        "version": "0.1.0",
        "author": ""
    }
    write_vvp_toml_file(config, project_config_file)


def add_command(args: argparse.Namespace):
    project_config_file = Path("./", PROJECT_CONFIG_FILE_NAME)
    (file_exists, config_file_path) = recursive_find_file(project_config_file)
    if not file_exists:
        print(
            f"error, {PROJECT_CONFIG_FILE_NAME} is not exists, this is not a vpp project directory")
        exit(-1)
    config = read_vvp_toml_file(config_file_path)
    module_name = args.module_name
    
    