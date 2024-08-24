import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyhtmlify.HTMLElement.HTMLElement import htmlElement


def html(*children, **attributes):
    return htmlElement("html", *children, **attributes)


def head(*children, **attributes):
    return htmlElement("head", *children, **attributes)


def title(*children, **attributes):
    return htmlElement("title", *children, **attributes)


def body(*children, **attributes):
    return htmlElement("body", *children, **attributes)


def p(*children, **attributes):
    return htmlElement("p", *children, **attributes)


def a(*children, **attributes):
    return htmlElement("a", *children, **attributes)


def img(**attributes):
    return htmlElement("img", **attributes)


def table(*children, **attributes):
    return htmlElement("table", *children, **attributes)


def tr(*children, **attributes):
    return htmlElement("tr", *children, **attributes)


def td(*children, **attributes):
    return htmlElement("td", *children, **attributes)


def th(*children, **attributes):
    return htmlElement("th", *children, **attributes)


def ul(*children, **attributes):
    return htmlElement("ul", *children, **attributes)


def ol(*children, **attributes):
    return htmlElement("ol", *children, **attributes)


def li(*children, **attributes):
    return htmlElement("li", *children, **attributes)


def br():
    return htmlElement("br")


def hr():
    return htmlElement("hr")


def form(*children, **attributes):
    return htmlElement("form", *children, **attributes)


def div(*children, **attributes):
    return htmlElement("div", *children, **attributes)


def span(*children, **attributes):
    return htmlElement("span", *children, **attributes)


def header(*children, **attributes):
    return htmlElement("header", *children, **attributes)


def footer(*children, **attributes):
    return htmlElement("footer", *children, **attributes)


def section(*children, **attributes):
    return htmlElement("section", *children, **attributes)


def article(*children, **attributes):
    return htmlElement("article", *children, **attributes)


def aside(*children, **attributes):
    return htmlElement("aside", *children, **attributes)


def main(*children, **attributes):
    return htmlElement("main", *children, **attributes)


def address(*children, **attributes):
    return htmlElement("address", *children, **attributes)


def nav(*children, **attributes):
    return htmlElement("nav", *children, **attributes)


def h1(*children, **attributes):
    return htmlElement("h1", *children, **attributes)


def h2(*children, **attributes):
    return htmlElement("h2", *children, **attributes)


def h3(*children, **attributes):
    return htmlElement("h3", *children, **attributes)


def h4(*children, **attributes):
    return htmlElement("h4", *children, **attributes)


def h5(*children, **attributes):
    return htmlElement("h5", *children, **attributes)


def h6(*children, **attributes):
    return htmlElement("h6", *children, **attributes)


def doctype(*children, **attributes):
    return htmlElement("!DOCTYPE html", *children, **attributes)


def input(**attributes):
    class InputElement(htmlElement):
        def __str__(self):
            attr_str = " ".join(
                f'{k.replace("_", "-")}="{v}"' for k, v in self.attributes.items()
            )
            return f"<{self.tag} {attr_str} />"

    return InputElement("input", **attributes)


def textarea(*children, **attributes):
    class TextAreaElement(htmlElement):
        def __init__(self, tag, *children, **attributes):
            super().__init__(tag, *children, **attributes)
            self.children = list(self.children)  # Ensure children is a list

        def __call__(self, *children):
            self.children.extend(children)
            return self

    return TextAreaElement("textarea", *children, **attributes)


def button(*children, **attributes):
    return htmlElement("button", *children, **attributes)


def label(*children, **attributes):
    return htmlElement("label", *children, **attributes)


def select(*children, **attributes):
    return htmlElement("select", *children, **attributes)


def option(*children, **attributes):
    return htmlElement("option", *children, **attributes)


def meta(**attributes):
    return htmlElement("meta", **attributes)


def link(**attributes):
    return htmlElement("link", **attributes)


def script(*children, **attributes):
    return htmlElement("script", *children, **attributes)


def style(*children, **attributes):
    return htmlElement("style", *children, **attributes)


def noscript(*children, **attributes):
    return htmlElement("noscript", *children, **attributes)
