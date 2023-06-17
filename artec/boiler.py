"""
	Main module core.
	#3 Step
"""
import json
import os


class boiler_builder:
    #! TUI is not implemented yet.
    def __init__(self, source=None, target=None, tui=False, verbose=False) -> None:
        self.verbose = verbose
        self.target = target
        self.structure = self._source(source)

    def _source(self, source) -> list[dict[str, str]]:
        try:
            if os.path.isfile(source):
                with open(source, "rt", encoding="utf-8") as file_data:
                    structure = json.load(file_data)
            else : 
                raise Exception()
            # TODO : What if it's a directory ?  
    
        except :
            if (source is None) and (self.verbose) :
                print("> No Source Provided.")
            
            elif (self.verbose) and not os.path.isfile(source):
                print("> Provided Source isn't a file.")
                
            print("> Reverting to default structure.")
            structure = DEFAULT_FOLDER_STRUCTURE
        return structure

    def build(self):
        print("> Creating folder structure: {}\n".format(self.target))

        for entry in self.structure:
            for _type, name in entry.items():
                try:
                    joined = os.path.join(self.target, name)
                    if _type == "folder":
                        self._make_folder(joined)
                    elif _type == "file":
                        self._make_file(joined)
                    print("Created: %s" % joined)
                except OSError:
                    exit("> Fatal error - exiting...")

    def _make_file(self, path):
        """Create an empty file in a given directory"""
        open(path, "a").close()

    def _make_folder(self, path):
        """Create an empty directory"""
        if not os.path.exists(path):
            os.makedirs(path)


DEFAULT_FOLDER_STRUCTURE = [
    {"folder": "src"},
    {"folder": "src\\__init__.py"},
    {"folder": "tests"},
    {"folder": "tests\\__init__.py"},
    {"folder": "res"},
    {"file": "README.md"},
    {"file": "setup.py"},
    {"file": "setup.cfg"},
    {"file": "pyproject.toml"},
]


if __name__ == "__main__":
    pass
