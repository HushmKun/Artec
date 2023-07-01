class static_list(list):
    def format(self, name):
        for _ in self:
            for i, j in _.items():
                _[i] = j.format(name)
        return self

PYTHON_PACKAGE = static_list(
    [
        {"folder": "{}"},
        {"file": "{}/__init__.py"},
        {"folder": "test"},
        {"file": "test/__init__.py"},
        {"file": "README.md"},
        {"file": "LICENSE"},
        {"file": "setup.py"},
        {"file": "setup.cfg"},
        {"file": "pyproject.toml"},
    ]
)

templates = {
    "python": PYTHON_PACKAGE,
    "node.js": None,
    "web": None,
}