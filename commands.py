import argparse
from pathlib import Path
from vpplib.utils.utils import check_file_exists
from vpplib.vppconf.conf import write_vvp_toml_file
from vpplib.constants import PROJECT_CONFIG_FILE_NAME, VERSION


def init_command(args: argparse.Namespace):
    project_config_file = Path("./", PROJECT_CONFIG_FILE_NAME)
    if check_file_exists(project_config_file):
        print("error, Vvp.toml alread exists! exit.")
        exit(-1)
    config = {
        "version": "0.1.0",
        "author": ""
    }
    write_vvp_toml_file(config, project_config_file)