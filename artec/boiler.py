"""
	Main module core.
	#3 Step
"""
import json
import os
from pathlib import Path
from .exceptions import NotJsonFile, NotValidJson, NoSource, InValidTemplate
from .templates import templates, static_list


class boiler_builder:
    def __init__(self, source=None, target=None, verbose=False, template=None) -> None:
        self.verbose = verbose
        self.target = target
        self.template = template
        if self.template is None:
            self.structure = self._source(source)
        else:
            self.structure = self._source_temp(template.lower())

    def _source_temp(self, template) -> list[dict[str, str]]:
        try:
            if template in templates:
                structure = templates[template].format(self.target)
            else:
                raise InValidTemplate(self.verbose)

        except InValidTemplate:
            structure = templates["python"].format(self.target)
        return structure

    def _source(self, source) -> list[dict[str, str]]:
        try:
            if os.path.isfile(source) and source.endswith(".json"):
                with open(source, "rt", encoding="utf-8") as file_data:
                    structure = static_list(json.load(file_data)).format(self.target)
            else:
                raise NotJsonFile(self.verbose)

        except Exception as e:
            if not hasattr(e, "errno"):
                NoSource(self.verbose)

            structure = templates["python"].format(self.target)
        return structure

    def build(self):
        print("> Creating folder structure: {}\n".format(self.target))

        for entry in self.structure:
            for _type, name in entry.items():
                try:
                    joined = Path(os.path.join(self.target, name))
                    if _type == "folder":
                        self._make_folder(joined)
                    elif _type == "file":
                        self._make_file(joined)
                    else:
                        raise NotValidJson(self.verbose)
                    print("Created: %s" % joined)
                except Exception:
                    exit("> Fatal error - exiting...")

    def _make_file(self, path):
        """Create an empty file in a given directory"""
        path.parent.mkdir(parents=True, exist_ok=True)
        open(path, "a").close()

    def _make_folder(self, path):
        """Create an empty directory"""
        os.makedirs(path, exist_ok=True)


if __name__ == "__main__":
    pass
