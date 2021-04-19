import toml

class ModuleFile:
    def __init__(self, file_name: str, depends: list[str] = []) -> None:
        self.file_name = file_name
        self.depends = depends

    def to_record(self) -> dict:
        return {
            "file_name": self.file_name,
            "depends": self.depends
        }