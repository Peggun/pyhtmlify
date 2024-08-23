# pyhtmlify

pyhtmlify is a Python package that allows you to write HTML code with Pure Python. This package was mainly made for the [osd Project](https://github.com/Peggun/osd) for simplicity. Heres how to do it. This package isn't completely finished, as we are still adding heaps of stuff and more HTML tags to this project.

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
import pyhtmlify as ph

def index():
    return ph.div(
        ph.h1("Welcome to My Website"),
        ph.input(type="text", placeholder="Enter your name"),
    )

# Render the HTML
html_content = str(index())
```

That is all you need for the script side. Now onto the html conversion

## 3. PY to HTML Conversion
To convert python index functions into html documents, pyhtml comes with a pyhtml command to use. In the terminal, to generate html code for all the html- files, run 
```py
pyhtmlify generate -o folder
```
The -o flag specifies the output folder, and there are some other flags and commands that are coming up. 
However, you you dont use the -o flag, the program automatically defaults to /html. All file names of the html files are the same name as the python script.

## 4. Contribution
If you would like to contribute to this project, please check out the issues and contact me at peggundev@gmail.com, or come check out osd and join the discord community!