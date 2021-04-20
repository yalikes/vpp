from arg_parser import parser_arg
from commands import generate_command, init_command, add_command


def main():
    args = parser_arg()
    args.sub_command_name
    if args.sub_command_name == "init":
        init_command(args)
    elif args.sub_command_name == "add":
        add_command(args)
    elif args.sub_command_name == "generate" or args.sub_command_name == "g":
        generate_command(args)


if __name__ == "__main__":
    main()
