import argparse


def parser_arg() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    sub_parser = parser.add_subparsers(dest="sub_command_name")

    init_parser = sub_parser.add_parser("init", help="init a project")

    generate_parser = sub_parser.add_parser(
        "generate", aliases=["g"], help="generate module to project.")
    generate_parser.add_argument("module_name", type=str,
                                 help="module name to be generated.")
    generate_parser.add_argument(
        "--notest", "-n", help="if this flag is set, then no test bench will be created.")
    add_parser = sub_parser.add_parser("add", help="add module to project.")
    add_parser.add_argument("module_name", type=str,
                            help="module name to be added.")
    add_parser.add_argument(
        "--deps",nargs="+" ,type=str, help="module names that this module depends.")

    args = parser.parse_args()
    return args
