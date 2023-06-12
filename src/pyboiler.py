"""
	Main module core.
	#3 Step
"""
import codecs
import json
import os


class boiler_builder:
	def __init__(self, source=None, target=None, override=None) -> None:
		self.override = override
		self.structure = self._source(source)
		self.target = target

	def _source(self, source) -> list[dict[str, str]]:
		try:
			if os.path.isfile(source):
				"""Handle UTF-8 Files"""
				with codecs.open(source, "rU", "utf-8") as file_data:
					structure = json.load(file_data)
					
		except:
			structure = DEFAULT_FOLDER_STRUCTURE
			exit("> Fatal error - cannot parse the provided JSON files: %s" % source)

		finally:
			return structure

	def build(self):
		print(
			"> {} folder structure: {}\n".format(
				"Overriding" if self.override else "Creating", self.target
			)
		)

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
	{"folder": "source"},
	{"folder": "sublime"},
	{"folder": "docs"},
	{"file": "README.md"},
]


if __name__ == "__main__":
	pass
