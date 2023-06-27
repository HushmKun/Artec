"""
	Main module core.
	#3 Step
"""
import json
import os
from pathlib import Path
from .exceptions import NotJsonFile, NotValidJson, NoSource
class boiler_builder:
    #! TUI is not implemented yet.
    def __init__(self, source=None, target=None, verbose=False, template=None, tui=False) -> None:
        self.verbose = verbose
        self.target = target
        self.template = template    
        if self.template is None :
            self.structure = self._source(source)

    def _source(self, source) -> list[dict[str, str]]:
        try:
            if os.path.isfile(source) and source.endswith('.json'):
                with open(source, "rt", encoding="utf-8") as file_data:
                    structure = json.load(file_data)
            else : 
                raise NotJsonFile(self.verbose)
    
        except Exception as e :
            
            if not hasattr(e,"errno") : 
                NoSource()                

            structure = DEFAULT_FOLDER_STRUCTURE
        return structure

    def build(self):
        print("> Creating folder structure: {}\n".format(self.target))

        for entry in self.structure:
            for _type, name in entry.items():
                try:
                    joined = os.path.join(self.target, Path(name))
                    if _type == "folder":
                        self._make_folder(joined)
                    elif _type == "file":
                        self._make_file(joined)
                    else : 
                        raise NotValidJson(self.verbose)
                    print("Created: %s" % joined)
                except Exception:
                    exit("> Fatal error - exiting...")
                
    def _make_file(self, path):
        """Create an empty file in a given directory"""
        open(path, "a").close()

    def _make_folder(self, path):
        """Create an empty directory"""
        os.makedirs(path, exist_ok=True)

DEFAULT_FOLDER_STRUCTURE = [
    {"folder": "src"},
    {"file": "src/__init__.py"},
    {"folder": "test"},
    {"file": "test/__init__.py"},
    {"folder": "res"},
    {"file": "README.md"},
    {"file": "setup.py"},
    {"file": "setup.cfg"},
    {"file": "pyproject.toml"},
]


if __name__ == "__main__":
    pass
