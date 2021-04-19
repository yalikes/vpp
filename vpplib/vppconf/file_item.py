from tomlkit import table, array


class ModuleFile:
    def __init__(self, file_name: str, depends: list[str] = []) -> None:
        self.file_name = file_name
        self.depends = depends

    def to_record(self) -> dict:
        file_table = table()
        file_table.add("file_name", self.file_name)
        file_table.add("depends", array(self.depends))
