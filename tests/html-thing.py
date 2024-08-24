import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyhtmlify.HTMLTags.tags import *


def index():
    return div(
        head(title("My Web Page")),
        body(
            header(h1("Welcome to My Website")),
            nav(a("Home", href="/"), a("About", href="/about")),
            main(
                p("This is the main content of the page."),
                div(
                    p("Some more content inside a div."),
                    img(src="image.jpg", alt="An image"),
                ),
            ),
            footer(p("© 2024 My Website")),
        ),
    )


# Render the HTML
html_content = str(index())
