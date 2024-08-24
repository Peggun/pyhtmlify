import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import src.pyhtmlify.HTMLTags.tags as tags

def index():
    return tags.div(
        tags.h1("Welcome to My Website"),
        tags.input(type="text", placeholder="Enter your name"),
    )


# Render the HTML
html_content = str(index())
