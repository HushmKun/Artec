"""
	Main module core.
	#3 Step
"""
import json
import os
from pathlib import Path
from . import exceptions as ex
from . import templates as temps
from . import repo 
from . import logger 

class boiler_builder:
    def __init__(
        self,
        source: str = None,
        target: str = None,
        template: str = None,
        git=False,
    ) -> None:
        self.target = target
        self.git = git
        self.home_dir = os.path.abspath(os.path.curdir)

        if template is None:
            self.structure = self._source(source)
        else:
            self.structure = self._source_temp(template.lower())

    def _source_temp(self, template) -> list[dict[str, str]]:
        try:
            if template in temps.templates:
                structure = temps.templates[template].format(self.target)
            else:
                raise ex.InValidTemplate()

        except ex.InValidTemplate:
            structure = temps.templates["python"].format(self.target)
        return structure

    def _source(self, source) -> list[dict[str, str]]:
        try:
            if source is None:
                raise ex.NoSource()
            if os.path.isfile(source) and source.endswith(".json"):
                with open(source, "rt", encoding="utf-8") as file_data:
                    structure = temps.static_list(json.load(file_data)).format(
                        self.target
                    )
            else:
                raise ex.NotJsonFile()

        except Exception:
            structure = temps.templates["python"].format(self.target)

        return structure

    def build(self):
        print("> Creating folder structure: {}\n".format(self.target))

        for entry in self.structure:
            for _type, name in entry.items():
                try:
                    joined = Path(os.path.join(self.target, name))
                    if "folder" in _type:
                        self._make_folder(joined)
                    elif "file" in _type:
                        self._make_file(joined)
                    else:
                        raise ex.NotValidJson()
                    print("Created: %s" % joined)
                except Exception:
                    pass
        print()

        if self.git:
            try:
                Repo = repo.repository(os.path.join(self.home_dir, self.target), self.target)
                Repo.add()
                    
            except Exception as e :
                ex.GitError(e)

    def _make_file(self, path):
        """Create an empty file in a given directory"""
        path.parent.mkdir(parents=True, exist_ok=True)
        open(path, "a").close()

    def _make_folder(self, path):
        """Create an empty directory"""
        os.makedirs(path, exist_ok=True)


if __name__ == "__main__":
    pass
