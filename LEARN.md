# Artec

## Table of Contents 
- [Artec](#artec)
    - [Table of Contents](#table-of-contents)
    - [Introduction](#introduction)
    - [How it all started?](#how-it-all-started)
    - [How does it work?](#how-does-it-work)
    - [Research](#research)
    - [First Steps](#first-steps)
    - [Roadmap](#roadmap)
        - [Parser](#parser)
        - [Boiler Builder](#boiler_builder)
        - [Tests](#tests)
        - [Packaging](#packaging)
    - [Finishing up](#finishing-up)



## Introduction

Hello 👋🏿! <br>
I am Hussein Mukhtar, a junior student (3rd year) in Computer Science in Suez University, And I'd like to walk you through ```Artec```.  

## How it all started?
Three years ago, I started learning Python and It was a good "hobby", Till you want to share your works with people.

Everything gets very complicated, "How do you share the code?" & "Why is this a single file not module?" & "How come this is not a package?", you name it. 😒

Also in that time I discovered linux and it's terminal tools, Everything you want to do you can do it from the terminal with a tap of your finger.

So I wanted to automate the basic process of starting a new project for me like ```ng new``` or ```flutter create``` , Also use this chance to hone my skills.

Artec was the brainchild of that thought. 

## How does it work?

Simply put, Artec takes a specific configuration you provide or uses the default structure to create the project (I prefer to call it repo), It also helps you setup your license, your README.md and so on.

## Research 

When you encounter a problem, it is often helpful to first search for existing solutions, and that I did.

The first thing I encountered was [cookiecutter](https://github.com/cookiecutter/cookiecutter) a really great tool (Too great for a novice), So I moved on till I found this beauty [here](https://github.com/Link-/pyboiler), It works and does great part of what I want but nothing big just a couple of tweaks here and there and It will work (eventually It was more than couple of tweaks but meh.) or though I thought. 

Well, It was bigger than I imagined and needed more work, and I kinda felt like I am gonna enjoy making this, So here we are. 

## First Steps 

Starting a repo knowing full well you won't use it again is completely different than having high hopes for one, that makes it special to you.

So I started by porting what I may use from PyBoiler, long story short It needed some heavy lifting.


## Roadmap 

### Parser 
The first thing I focused on was parsing arguments to the program, for that I made a simple wrapper for argparse in the file [parser.py](artec\argparser.py). 

The main focus in that wrapper was to make it easy to modify the args whether to add or remove, Theoretically the parser should be "elegant" enough to be recycled in any other project with no hassle, In the end there's a driver function that's easy to use called (main_args).

Couple of things I had to focus on that messed up my code a little bit: 
* Custom Action to list my templates.
* Mutually exclusive arguments 

### Boiler_builder
Not the easiest part but not the hardest also, It had to accept arguments from our [parser](#parser) then decide some things : 
    
1. Did you use a template ? 
    * Yes :
        * Is the template valid ? 
            1. Yes : Use it. 
            2. No : Use default Python structure. 

    * No  : 
        * Is Source provided ? 
            1. Yes : Is valid ?
                1. Yes : Apply it.
                2. No : Use default Python structure. 
            2. No : Use default Python structure. 

Also, a major key take for me was Exceptions, We kind of ignore raising them or explaining why this exceptions happens to the user and it just leaves them lost in the application. 

The build method is fairly simple, It just iterates over the structure dictionary and creates each folder and/or file.      

### Tests 
The tests was an uncharted waters for me, So trying unittest was probably a good idea. You should have a look [here](tests/) not the best but good enough for me.

### Packaging
The hardest part also the one I learned in the most, let's start with some key takes : 
1. ```__init__.py``` is a very **important** reserved key file, It's main usage comes when a package provide an API. (_It isn't necessary here, except in tests_)
2. Your project structure should look similar to what I did here (*Also The ```__main__.py``` part isn't 100% perfect*):    
3. I figured that keeping your entry points in ```__main__.py``` makes it easier for people to figure out where is the start of your project, how does it work, etc.
```    
    .
    ├── artec
    │   ├── __main__.py
    │   ├── argparser.py
    │   ├── boiler.py
    │   ├── exceptions.py
    │   └── templates.py
    ├── CONTRIBUTING.md
    ├── LEARN.md
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── setup.py
    └── test
        ├── __init__.py
        ├── boiler_test.py
        └── parser_test.py
``` 
4. **Be Aware of relative and absolute imports.** They are a mess in packaging if your structure isn't "clean" enough. 
5. **Automate your build & deploy**, It sucks having to manage the versions and manage uploading them in order each time. 
5. [This](https://packaging.python.org/en/latest/overview/) is a very good reference.


## Finishing up
I am really enjoying this & I hope you enjoy and learn too.  






