import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import src.pyhtmlify.HTMLTags.tags as tags

def index():
    return tags.html(), tags.body(
        tags.if_tag("user.is_authenticated", "Welcome Back!", false_children=["Please log in."])
    )