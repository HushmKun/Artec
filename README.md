# Artec

Artec is a simple python 3 script to create a project template in a given directory.<br>
_It's a maintained version of PyBoiler_

## Installation

Download from pip 

```bash
pip install artec
```

or Install manually
```bash
$ cd Artec
$ pip install . 
```
## Usage
Create a JSON file to match the folder structure you desire
```
$ vim structure.json 
    
# Paste the below into your file and modify as you desire
[{'folder': 'source'}, 
{'file': 'source/file1.txt'}, # Nested file
{'folder': 'sublime'}, 
{'file': 'sublime/file2.txt'}, 
{'folder': 'docs'}, 
{'file': 'docs/file3.txt'}, 
{'file': 'docs/file4.txt'},
{'file': 'README.md'}]
```
 How to execute
```
usage: artec [OPTIONS] -o [DEST] 

Artec is a simple python 3 script to create a project template in a given directory.

options:
  -h, --help            show this help message and exit
  -o TARGET, --output-directory TARGET
                        Target output path where the structure will be created
  -s SOURCE, --source-file SOURCE
                        Source JSON file containing structure to be created
  -i, --interactive     Runs Artec in interactive mode.
  -v, --verbose         Runs Artec in verbose mode.

Examples:
        artec -o dest
        artec -o dest -s structure.json
```
## Version

    0.1.3

## Contributing

* Big Thanks to [Link-](https://github.com/Link-) for jump starting the project.
* Thanks for [Narayandas Akhil Achary](https://github.com/0018akhil) for solving the ```-s``` [bug](https://github.com/HushmKun/Artec/issues/4).

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU GPLv3.0](https://choosealicense.com/licenses/gpl-3.0/)
