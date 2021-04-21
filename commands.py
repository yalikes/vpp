import argparse
from pathlib import Path
from vpplib.utils.utils import check_file_exists, recursive_find_file
from vpplib.vppconf.conf import read_vvp_toml_file, write_vvp_toml_file, read_json_file, write_json_file
from vpplib.constants import (
    PROJECT_CONFIG_FILE_NAME, VPP_DESC_FILE,
    MODULE_NAME_PLACEHOLDER,
    TEST_MODULE_NAME_PLACEHOLDER
)
from vpplib.vppconf.file_item import ModuleFile
from vpplib.routines import add_module_file_to_desc_file, read_module_template, read_test_module_template


def init_command(args: argparse.Namespace):
    project_config_file = Path("./", PROJECT_CONFIG_FILE_NAME)
    vpp_desc_file = Path("./", VPP_DESC_FILE)
    if check_file_exists(project_config_file):
        print(f"error, {PROJECT_CONFIG_FILE_NAME} alread exists! exit.")
        exit(-1)
    # basic config file here
    config = {
        "version": "0.1.0",
        "author": "",
    }
    files = {"files": []}
    write_vvp_toml_file(config, project_config_file)
    write_json_file(files, vpp_desc_file)


def add_command(args: argparse.Namespace):
    module_name = args.module_name
    depends = args.deps if args.deps else []
    module_file_item = ModuleFile(module_name, depends)
    add_module_file_to_desc_file(module_file_item)


def generate_command(args: argparse.Namespace):
    project_config_file = Path("./", PROJECT_CONFIG_FILE_NAME)
    vpp_desc_file = Path("./", VPP_DESC_FILE)
    (file_exists, config_file_path) = recursive_find_file(project_config_file)
    if not file_exists:
        print(
            f"error, {PROJECT_CONFIG_FILE_NAME} is not exists, this is not a vpp project directory")
        exit(-1)
    config = read_vvp_toml_file(config_file_path)
    files = read_json_file(vpp_desc_file)

    module_name = args.module_name
    test_module_name = module_name+"_tb"
    module_file_name = module_name+".v"
    test_module_file_name = test_module_name+".v"  # get module files name

    # module_content
    module_content = read_module_template().replace(
        MODULE_NAME_PLACEHOLDER, module_name)

    # test module content
    test_module_content = read_test_module_template().replace(
        TEST_MODULE_NAME_PLACEHOLDER, test_module_name).replace(
            MODULE_NAME_PLACEHOLDER, module_name)
    # write module file
    module_file = Path(module_file_name)
    module_file.write_text(module_content)

    # add module to desc file
    module_item = ModuleFile(module_file_name)
    add_module_file_to_desc_file(module_file_item=module_item)

    if not args.notest:
        # write test module file
        test_module_file = Path(test_module_file_name)
        test_module_file.write_text(test_module_content)

        # add test module to desc file
        test_module_item = ModuleFile(
            test_module_file_name, depends=[module_file_name])
        add_module_file_to_desc_file(module_file_item=test_module_item)
