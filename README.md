# pyhtmlify

<p align="center">
<a href="https://pepy.tech/project/pyhtmlify"><img alt="Downloads" src="https://static.pepy.tech/badge/pyhtmlify">
<a style="text-decoration:none" href="https://github.com/Peggun/pyhtmlify/action/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/Peggun/pyhtmlify/ci.yml?label=pyhtmlify%20CI" alt="pyhtmlify CI" /></a>

pyhtmlify is a Python package that allows you to write HTML code with Pure Python. This package was mainly made for the [osd Project](https://github.com/Peggun/osd) for simplicity. Heres how to use it. This package isn't completely finished, as we are still adding heaps of stuff and more HTML tags to this project.

## 1. Installation
You can install pyhtml using pip
```py
pip install pyhtmlify
```
This will install the latest version of pyhtmlify.

## 2. How to use
pyhtmlify is quite easy to use. It is similar to html, but without all of the <> and other things involved. To do so, make a python file starting with html- and pyhtml will pick it up.

For pyhtml to pick up the file to generate the html code for you, you need to have a index function inside of your script. Like this for example:
```py
import pyhtmlify.HTMLTags.tags as ph

def index():
    return ph.div(
        ph.h1("Welcome to My Website"),
        ph.input(type="text", placeholder="Enter your name"),
    )
```

That is all you need for the script side. Now onto the html conversion

## 3. PY to HTML Conversion
To convert python index functions into html documents, pyhtmlify comes with a pyhtmlify command to use. In the terminal, to generate html code for all the html-*.py files, run 
```py
pyhtmlify generate -f folder
```
The -f flag specifies the output folder, and there are some other flags and commands that are coming up. 
However, you you dont use the -f flag, the program automatically defaults to /html. All file names of the html files are the same name as the python script.

There is also a find command
```py
pyhtmlify find -f folder
```
This command finds all possible files to generate and tell you the file and the file path to it. If the -f flag isnt used, it will scan the entire working directory.

## 4. Contribution
If you would like to contribute to this project, please check out the issues and contact me at peggundev@gmail.com, or come check out osd and join the discord community!
