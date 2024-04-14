![Logo](img/Artec.png)
# Artec
A python application that creates a configurable python project template in a given directory.<br>
_It's a maintained version of PyBoiler_

## Installation

Download from pip 

```bash
$ pip install Artec
```

or Install manually
```bash
$ git clone https://github.com/HushmKun/Artec
$ cd Artec
$ pip install -U . 
```
## Usage
Create a JSON file to match the folder structure you desire
```
$ vim structure.json 
    
# Paste the below into your file and modify as you desire
{
    "folders": [
        "{}",
        "test"
    ], 
    "files": [
        "{}/__init__.py",
        "test/__init__.py",
        "README.md",
        "LICENSE",
        "setup.py",
        "pyproject.toml"
    ]
}

```
How to execute
```
$ artec -h
usage: artec [OPTIONS] -o [DEST] 

Artec is a python application that creates a configurable python project template in a given directory.

options:
  -h, --help            show this help message and exit
  -s SOURCE, --source-file SOURCE
                        Source JSON file containing structure to be created
  -t TEMPLATE, --template TEMPLATE
                        Uses ready-made templates.
  -o TARGET, --output-directory TARGET
                        Target output path where the structure will be created
  -ls, --list-template  lists all ready-made templates.
  -v, --verbose         Runs Artec in verbose mode.
  -g, --git-init        Creates a git Repo for the project.
  -V, --version         Display current version of Artec

Examples:
        artec -h
        artec -o dest
        artec -o dest -t python
        artec -o dest -s structure.json
        artec -o dest -s structure.json -v
```

## Templates
- Python
- Flask 
- Node.Js
- Data_Science

## Version

    0.3.1

## Contributing
Please refer to [Here](CONTRIBUTING.md) for contributing.
Any help that can contribute to the templates will be really appreciated.

* Big Thanks to [Link-](https://github.com/Link-) for jump starting the project.
* Thanks for [Narayandas Akhil Achary](https://github.com/0018akhil) for various fixes & features.

## Learning
Since this project is intended as a learning project, It helps me figure out what is the best practices of X, How to use Y, etc...

If you come here to learn, Read [this](LEARN.md), I will be glad if it helped you learn something new. 
## License

[GNU GPLv3.0](https://choosealicense.com/licenses/gpl-3.0/)
