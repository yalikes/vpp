import tomlkit
import argparse
from pathlib import Path
from vvplib.utils.utils import check_file_exists
def init_command(args: argparse.Namespace):
    project_file = Path("./Vvp.toml")
    if check_file_exists(project_file):
        pass