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
[
    {"folder": "{}"},           # Use '{}' to be replaced with project name.
    {"file": "{}/__init__.py"},
    {"folder": "test"},
    {"file": "test/__init__.py"},
    {"file": "README.md"},
    {"file": "LICENSE"},
    {"file": "setup.py"},
    {"file": "setup.cfg"},
    {"file": "pyproject.toml"},
]
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
<details>
<summary> Python </summary>

Project Named Artec 
```
artec
├── artec
│   └── __main__.py
├── test
│   └── __init__.py
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
└── setup.py
 
2 directories, 7 files
```
</details>

<details>
<summary> Flask </summary>

Project Named flaskr 
```
flaskr
.
├── flaskr
│   ├── auth.py
│   ├── blog
│   │   ├── create.html
│   │   ├── index.html
│   │   └── update.html
│   ├── blog.py
│   ├── db.py
│   ├── __init__.py
│   ├── schema.py
│   ├── static
│   │   └── style.css
│   └── templates
│       ├── auth
│       │   ├── login.html
│       │   └── register.html
│       └── base.html
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.py
└── test
    ├── conftest.py
    ├── data.sql
    ├── __init__.py
    ├── test_auth.py
    ├── test_blog.py
    └── test_db.py

7 directories, 22 files
```
</details>
<details>
<summary> Node.Js </summary>

Project Named Node 
```
Node
├── LICENSE
├── package.json
├── package-lock.json
├── README.md
└── src
    ├── api
    │   ├── controllers
    │   │   └── user
    │   │       ├── auth
    │   │       │   ├── forgot-password.js
    │   │       │   ├── login.js
    │   │       │   ├── logout.js
    │   │       │   ├── refresh-token.js
    │   │       │   ├── register.js
    │   │       │   ├── send-verification-code.js
    │   │       │   └── verify-email.js
    │   │       ├── delete-user.js
    │   │       ├── edit
    │   │       │   ├── change-password.js
    │   │       │   └── edit-user.js
    │   │       ├── get-user.js
    │   │       └── index.js
    │   ├── middlewares
    │   │   ├── auth
    │   │   │   ├── check-auth.js
    │   │   │   └── check-authority.js
    │   │   ├── image-upload.js
    │   │   ├── index.js
    │   │   ├── object-id-control.js
    │   │   └── rate-limiter.js
    │   ├── routes
    │   │   ├── index.js
    │   │   └── user.js
    │   └── validators
    │       ├── index.js
    │       └── user.validator.js
    ├── app.js
    ├── config
    │   └── index.js
    ├── loaders
    │   ├── express.js
    │   ├── index.js
    │   └── mongoose.js
    ├── models
    │   ├── index.js
    │   ├── log.js
    │   ├── token.js
    │   └── user.js
    └── utils
        ├── helpers
        │   ├── error-helper.js
        │   ├── generate-random-code.js
        │   ├── ip-helper.js
        │   ├── jwt-token-helper.js
        │   └── local-text-helper.js
        ├── index.js
        ├── lang
        │   ├── en.json
        │   ├── get-text.json
        │   └── tr.json
        ├── logger.js
        └── send-code-to-email.js

17 directories, 46 files
```
</details>

## Version

    0.3.0

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
