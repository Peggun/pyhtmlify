import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.HTMLTags.tags import *


def index():
    return div()


# Render the HTML
html_content = str(index())
