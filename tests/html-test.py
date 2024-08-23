import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.HTMLTags.tags import *


def index():
    return div(
        h1("Welcome to My Website"),
        input(type="text", placeholder="Enter your name"),
    )


# Render the HTML
html_content = str(index())
