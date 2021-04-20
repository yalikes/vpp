from pathlib import Path
from vpplib.utils.utils import get_project_root


class ModuleFile:
    def __init__(self, file_name: str, depends: list[str] = []) -> None:
        self.file_name = file_name
        self.depends = depends

    def to_record(self) -> dict:
        (project_file_exists, project_file_path) = get_project_root()
        if not project_file_exists:
            print("this is not a vpp project, exit")
            exit(-1)
        relative_file_name = str(Path(
            self.file_name).relative_to(project_file_path))
        relative_depends = [str(Path(dep_file).relative_to(project_file_path)) for
                            dep_file in self.depends]
        return {
            "file_name": relative_file_name,
            "depends": relative_depends
        }
