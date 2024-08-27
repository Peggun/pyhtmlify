import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pyhtmlify.HTMLElements.HTMLElements import htmlElement, InputElement, IfElement, TextAreaElement


def html(*children, **attributes):
    """
    Defines an HTML document.

    Parameters:
    *children: Elements that are nested within the <html> tag.
    **attributes: HTML attributes like 'class', 'id', etc.

    Returns:
    htmlElement: An object representing the <html> tag.
    """
    return htmlElement("html", *children, **attributes)


def head(*children, **attributes):
    """
    Defines the head section of an HTML document.

    Parameters:
    *children: Elements that are nested within the <head> tag, such as <title>, <meta>, <link>.
    **attributes: HTML attributes for the <head> tag.

    Returns:
    htmlElement: An object representing the <head> tag.
    """
    return htmlElement("head", *children, **attributes)


def title(*children, **attributes):
    """
    Defines the title of the HTML document, shown in the browser's title bar or tab.

    Parameters:
    *children: The title text.
    **attributes: HTML attributes for the <title> tag.

    Returns:
    htmlElement: An object representing the <title> tag.
    """
    return htmlElement("title", *children, **attributes)


def body(*children, **attributes):
    """
    Defines the body of the HTML document.

    Parameters:
    *children: Elements that are nested within the <body> tag.
    **attributes: HTML attributes for the <body> tag.

    Returns:
    htmlElement: An object representing the <body> tag.
    """
    return htmlElement("body", *children, **attributes)


def p(*children, **attributes):
    """
    Defines a paragraph.

    Parameters:
    *children: The content inside the <p> tag.
    **attributes: HTML attributes for the <p> tag.

    Returns:
    htmlElement: An object representing the <p> tag.
    """
    return htmlElement("p", *children, **attributes)


def a(*children, **attributes):
    """
    Defines a hyperlink.

    Parameters:
    *children: The content inside the <a> tag, usually text or an image.
    **attributes: HTML attributes for the <a> tag, such as 'href'.

    Returns:
    htmlElement: An object representing the <a> tag.
    """
    return htmlElement("a", *children, **attributes)


def img(**attributes):
    """
    Defines an image.

    Parameters:
    **attributes: HTML attributes for the <img> tag, such as 'src', 'alt'.

    Returns:
    htmlElement: An object representing the <img> tag.
    """
    return htmlElement("img", **attributes)


def table(*children, **attributes):
    """
    Defines a table.

    Parameters:
    *children: The content inside the <table> tag, typically rows (<tr> tags).
    **attributes: HTML attributes for the <table> tag.

    Returns:
    htmlElement: An object representing the <table> tag.
    """
    return htmlElement("table", *children, **attributes)


def tr(*children, **attributes):
    """
    Defines a table row.

    Parameters:
    *children: The content inside the <tr> tag, typically cells (<td> or <th> tags).
    **attributes: HTML attributes for the <tr> tag.

    Returns:
    htmlElement: An object representing the <tr> tag.
    """
    return htmlElement("tr", *children, **attributes)


def td(*children, **attributes):
    """
    Defines a table cell.

    Parameters:
    *children: The content inside the <td> tag.
    **attributes: HTML attributes for the <td> tag.

    Returns:
    htmlElement: An object representing the <td> tag.
    """
    return htmlElement("td", *children, **attributes)


def th(*children, **attributes):
    """
    Defines a header cell in a table.

    Parameters:
    *children: The content inside the <th> tag.
    **attributes: HTML attributes for the <th> tag.

    Returns:
    htmlElement: An object representing the <th> tag.
    """
    return htmlElement("th", *children, **attributes)


def ul(*children, **attributes):
    """
    Defines an unordered list.

    Parameters:
    *children: List items (<li> tags) inside the <ul> tag.
    **attributes: HTML attributes for the <ul> tag.

    Returns:
    htmlElement: An object representing the <ul> tag.
    """
    return htmlElement("ul", *children, **attributes)


def ol(*children, **attributes):
    """
    Defines an ordered list.

    Parameters:
    *children: List items (<li> tags) inside the <ol> tag.
    **attributes: HTML attributes for the <ol> tag.

    Returns:
    htmlElement: An object representing the <ol> tag.
    """
    return htmlElement("ol", *children, **attributes)


def li(*children, **attributes):
    """
    Defines a list item.

    Parameters:
    *children: The content inside the <li> tag.
    **attributes: HTML attributes for the <li> tag.

    Returns:
    htmlElement: An object representing the <li> tag.
    """
    return htmlElement("li", *children, **attributes)


def br():
    """
    Inserts a line break.

    Returns:
    htmlElement: An object representing the <br> tag.
    """
    return htmlElement("br")


def hr():
    """
    Inserts a thematic break (horizontal rule).

    Returns:
    htmlElement: An object representing the <hr> tag.
    """
    return htmlElement("hr")


def form(*children, **attributes):
    """
    Defines an HTML form for user input.

    Parameters:
    *children: Elements inside the <form> tag, typically input fields and buttons.
    **attributes: HTML attributes for the <form> tag, such as 'action' and 'method'.

    Returns:
    htmlElement: An object representing the <form> tag.
    """
    return htmlElement("form", *children, **attributes)


def div(*children, **attributes):
    """
    Defines a division or section in an HTML document.

    Parameters:
    *children: The content inside the <div> tag.
    **attributes: HTML attributes for the <div> tag.

    Returns:
    htmlElement: An object representing the <div> tag.
    """
    return htmlElement("div", *children, **attributes)


def span(*children, **attributes):
    """
    Defines an inline section of text.

    Parameters:
    *children: The content inside the <span> tag.
    **attributes: HTML attributes for the <span> tag.

    Returns:
    htmlElement: An object representing the <span> tag.
    """
    return htmlElement("span", *children, **attributes)


def header(*children, **attributes):
    """
    Defines a header section in an HTML document.

    Parameters:
    *children: The content inside the <header> tag.
    **attributes: HTML attributes for the <header> tag.

    Returns:
    htmlElement: An object representing the <header> tag.
    """
    return htmlElement("header", *children, **attributes)


def footer(*children, **attributes):
    """
    Defines a footer section in an HTML document.

    Parameters:
    *children: The content inside the <footer> tag.
    **attributes: HTML attributes for the <footer> tag.

    Returns:
    htmlElement: An object representing the <footer> tag.
    """
    return htmlElement("footer", *children, **attributes)


def section(*children, **attributes):
    """
    Defines a section in an HTML document.

    Parameters:
    *children: The content inside the <section> tag.
    **attributes: HTML attributes for the <section> tag.

    Returns:
    htmlElement: An object representing the <section> tag.
    """
    return htmlElement("section", *children, **attributes)


def article(*children, **attributes):
    """
    Defines an independent, self-contained article in an HTML document.

    Parameters:
    *children: The content inside the <article> tag.
    **attributes: HTML attributes for the <article> tag.

    Returns:
    htmlElement: An object representing the <article> tag.
    """
    return htmlElement("article", *children, **attributes)


def aside(*children, **attributes):
    """
    Defines content aside from the main content (e.g., sidebar).

    Parameters:
    *children: The content inside the <aside> tag.
    **attributes: HTML attributes for the <aside> tag.

    Returns:
    htmlElement: An object representing the <aside> tag.
    """
    return htmlElement("aside", *children, **attributes)


def main(*children, **attributes):
    """
    Defines the main content of an HTML document.

    Parameters:
    *children: The content inside the <main> tag.
    **attributes: HTML attributes for the <main> tag.

    Returns:
    htmlElement: An object representing the <main> tag.
    """
    return htmlElement("main", *children, **attributes)


def address(*children, **attributes):
    """
    Defines contact information for the author or owner of an article or document.

    Parameters:
    *children: The content inside the <address> tag.
    **attributes: HTML attributes for the <address> tag.

    Returns:
    htmlElement: An object representing the <address> tag.
    """
    return htmlElement("address", *children, **attributes)


def nav(*children, **attributes):
    """
    Defines a set of navigation links.

    Parameters:
    *children: The content inside the <nav> tag, usually <a> elements.
    **attributes: HTML attributes for the <nav> tag.

    Returns:
    htmlElement: An object representing the <nav> tag.
    """
    return htmlElement("nav", *children, **attributes)



def h1(*children, **attributes):
    """
    Defines the highest level heading, typically used as the main title of a document.

    Parameters:
    *children: The content inside the <h1> tag.
    **attributes: HTML attributes for the <h1> tag.

    Returns:
    htmlElement: An object representing the <h1> tag.
    """
    return htmlElement("h1", *children, **attributes)


def h2(*children, **attributes):
    """
    Defines a second-level heading, used for subsections within a document.

    Parameters:
    *children: The content inside the <h2> tag.
    **attributes: HTML attributes for the <h2> tag.

    Returns:
    htmlElement: An object representing the <h2> tag.
    """
    return htmlElement("h2", *children, **attributes)


def h3(*children, **attributes):
    """
    Defines a third-level heading, used for smaller subsections within a document.

    Parameters:
    *children: The content inside the <h3> tag.
    **attributes: HTML attributes for the <h3> tag.

    Returns:
    htmlElement: An object representing the <h3> tag.
    """
    return htmlElement("h3", *children, **attributes)


def h4(*children, **attributes):
    """
    Defines a fourth-level heading, used for minor subsections within a document.

    Parameters:
    *children: The content inside the <h4> tag.
    **attributes: HTML attributes for the <h4> tag.

    Returns:
    htmlElement: An object representing the <h4> tag.
    """
    return htmlElement("h4", *children, **attributes)


def h5(*children, **attributes):
    """
    Defines a fifth-level heading, used for very minor subsections within a document.

    Parameters:
    *children: The content inside the <h5> tag.
    **attributes: HTML attributes for the <h5> tag.

    Returns:
    htmlElement: An object representing the <h5> tag.
    """
    return htmlElement("h5", *children, **attributes)


def h6(*children, **attributes):
    """
    Defines the lowest level heading, used for the smallest subsections within a document.

    Parameters:
    *children: The content inside the <h6> tag.
    **attributes: HTML attributes for the <h6> tag.

    Returns:
    htmlElement: An object representing the <h6> tag.
    """
    return htmlElement("h6", *children, **attributes)


def doctype():
    """
    Declares the document type and version of HTML being used.

    Parameters:
    None
    
    Returns:
    htmlElement: An object representing the <!DOCTYPE html> declaration.
    """
    return htmlElement("!DOCTYPE html")


def input(**attributes):
    """
    Defines an input field where the user can enter data.

    Parameters:
    **attributes: HTML attributes for the <input> tag, such as 'type', 'name', 'value'.

    Returns:
    InputElement: An object representing the <input> tag.
    """
    return InputElement("input", **attributes)


def textarea(*children, **attributes):
    """
    Defines a multi-line text input control.

    Parameters:
    *children: The default content inside the <textarea> tag.
    **attributes: HTML attributes for the <textarea> tag, such as 'name', 'rows', 'cols'.

    Returns:
    TextAreaElement: An object representing the <textarea> tag.
    """
    return TextAreaElement("textarea", *children, **attributes)


def button(*children, **attributes):
    """
    Defines a clickable button.

    Parameters:
    *children: The content inside the <button> tag, usually text or an icon.
    **attributes: HTML attributes for the <button> tag, such as 'type', 'value'.

    Returns:
    htmlElement: An object representing the <button> tag.
    """
    return htmlElement("button", *children, **attributes)


def label(*children, **attributes):
    """
    Defines a label for an <input> element.

    Parameters:
    *children: The text content inside the <label> tag.
    **attributes: HTML attributes for the <label> tag, such as 'for'.

    Returns:
    htmlElement: An object representing the <label> tag.
    """
    return htmlElement("label", *children, **attributes)


def select(*children, **attributes):
    """
    Defines a drop-down list.

    Parameters:
    *children: The <option> elements inside the <select> tag.
    **attributes: HTML attributes for the <select> tag, such as 'name', 'multiple'.

    Returns:
    htmlElement: An object representing the <select> tag.
    """
    return htmlElement("select", *children, **attributes)


def option(*children, **attributes):
    """
    Defines an option in a <select> drop-down list.

    Parameters:
    *children: The text content inside the <option> tag.
    **attributes: HTML attributes for the <option> tag, such as 'value', 'selected'.

    Returns:
    htmlElement: An object representing the <option> tag.
    """
    return htmlElement("option", *children, **attributes)


def meta(**attributes):
    """
    Defines metadata about an HTML document, such as charset, viewport, or author.

    Parameters:
    **attributes: HTML attributes for the <meta> tag, such as 'charset', 'name', 'content'.

    Returns:
    htmlElement: An object representing the <meta> tag.
    """
    return htmlElement("meta", **attributes)


def link(**attributes):
    """
    Defines a relationship between the current document and an external resource, typically used for linking to stylesheets.

    Parameters:
    **attributes: HTML attributes for the <link> tag, such as 'rel', 'href', 'type'.

    Returns:
    htmlElement: An object representing the <link> tag.
    """
    return htmlElement("link", **attributes)


def script(*children, **attributes):
    """
    Defines client-side JavaScript code or links to an external JavaScript file.

    Parameters:
    *children: The JavaScript code inside the <script> tag.
    **attributes: HTML attributes for the <script> tag, such as 'src', 'type'.

    Returns:
    htmlElement: An object representing the <script> tag.
    """
    return htmlElement("script", *children, **attributes)


def style(*children, **attributes):
    """
    Defines style information for an HTML document, typically CSS.

    Parameters:
    *children: The CSS code inside the <style> tag.
    **attributes: HTML attributes for the <style> tag, such as 'type'.

    Returns:
    htmlElement: An object representing the <style> tag.
    """
    return htmlElement("style", *children, **attributes)


def noscript(*children, **attributes):
    """
    Defines alternative content to be displayed if the user's browser does not support JavaScript.

    Parameters:
    *children: The content inside the <noscript> tag.
    **attributes: HTML attributes for the <noscript> tag.

    Returns:
    htmlElement: An object representing the <noscript> tag.
    """
    return htmlElement("noscript", *children, **attributes)


def if_tag(condition, *true_children, false_children=None):
    """
    Conditionally renders elements based on a given condition.

    Parameters:
    condition (bool): The condition to evaluate.
    *true_children: Elements to render if the condition is True.
    false_children: Elements to render if the condition is False.

    Returns:
    IfElement: An object that renders either true_children or false_children based on the condition.
    """
    return IfElement(condition, *true_children, false_children=false_children)

def abbr(*children, **attributes):
    """
    Defines an abbreviation or acronym.

    Parameters:
    *children: The content inside the <abbr> tag.
    **attributes: HTML attributes for the <abbr> tag.

    Returns:
    htmlElement: An object representing the <abbr> tag.
    """
    return htmlElement("abbr", *children, **attributes)


def area(**attributes):
    """
    Defines an area inside an image map.

    Parameters:
    **attributes: HTML attributes for the <area> tag, such as 'shape', 'coords', 'href'.

    Returns:
    htmlElement: An object representing the <area> tag.
    """
    return htmlElement("area", **attributes)


def article(*children, **attributes):
    """
    Defines an independent, self-contained article in an HTML document.

    Parameters:
    *children: The content inside the <article> tag.
    **attributes: HTML attributes for the <article> tag.

    Returns:
    htmlElement: An object representing the <article> tag.
    """
    return htmlElement("article", *children, **attributes)


def audio(*children, **attributes):
    """
    Defines embedded sound content.

    Parameters:
    *children: Elements like <source> inside the <audio> tag.
    **attributes: HTML attributes for the <audio> tag.

    Returns:
    htmlElement: An object representing the <audio> tag.
    """
    return htmlElement("audio", *children, **attributes)


def b(*children, **attributes):
    """
    Defines bold text.

    Parameters:
    *children: The content inside the <b> tag.
    **attributes: HTML attributes for the <b> tag.

    Returns:
    htmlElement: An object representing the <b> tag.
    """
    return htmlElement("b", *children, **attributes)


def bdi(*children, **attributes):
    """
    Defines text that is isolated from its surrounding for bidirectional text formatting.

    Parameters:
    *children: The content inside the <bdi> tag.
    **attributes: HTML attributes for the <bdi> tag.

    Returns:
    htmlElement: An object representing the <bdi> tag.
    """
    return htmlElement("bdi", *children, **attributes)


def bdo(*children, **attributes):
    """
    Overrides the current text direction.

    Parameters:
    *children: The content inside the <bdo> tag.
    **attributes: HTML attributes for the <bdo> tag.

    Returns:
    htmlElement: An object representing the <bdo> tag.
    """
    return htmlElement("bdo", *children, **attributes)


def canvas(*children, **attributes):
    """
    Defines graphics in JavaScript.

    Parameters:
    *children: The content inside the <canvas> tag, typically JavaScript.
    **attributes: HTML attributes for the <canvas> tag.

    Returns:
    htmlElement: An object representing the <canvas> tag.
    """
    return htmlElement("canvas", *children, **attributes)


def cite(*children, **attributes):
    """
    Defines the title of a work.

    Parameters:
    *children: The content inside the <cite> tag.
    **attributes: HTML attributes for the <cite> tag.

    Returns:
    htmlElement: An object representing the <cite> tag.
    """
    return htmlElement("cite", *children, **attributes)


def code(*children, **attributes):
    """
    Defines a piece of computer code.

    Parameters:
    *children: The content inside the <code> tag.
    **attributes: HTML attributes for the <code> tag.

    Returns:
    htmlElement: An object representing the <code> tag.
    """
    return htmlElement("code", *children, **attributes)


def data(*children, **attributes):
    """
    Links a piece of content to a machine-readable translation.

    Parameters:
    *children: The content inside the <data> tag.
    **attributes: HTML attributes for the <data> tag.

    Returns:
    htmlElement: An object representing the <data> tag.
    """
    return htmlElement("data", *children, **attributes)


def datalist(*children, **attributes):
    """
    Specifies a list of pre-defined options for input controls.

    Parameters:
    *children: The content inside the <datalist> tag, typically <option> elements.
    **attributes: HTML attributes for the <datalist> tag.

    Returns:
    htmlElement: An object representing the <datalist> tag.
    """
    return htmlElement("datalist", *children, **attributes)


def details(*children, **attributes):
    """
    Defines additional details that the user can view or hide.

    Parameters:
    *children: The content inside the <details> tag.
    **attributes: HTML attributes for the <details> tag.

    Returns:
    htmlElement: An object representing the <details> tag.
    """
    return htmlElement("details", *children, **attributes)


def dialog(*children, **attributes):
    """
    Defines a dialog box or window.

    Parameters:
    *children: The content inside the <dialog> tag.
    **attributes: HTML attributes for the <dialog> tag.

    Returns:
    htmlElement: An object representing the <dialog> tag.
    """
    return htmlElement("dialog", *children, **attributes)


def figure(*children, **attributes):
    """
    Specifies self-contained content, typically with a caption.

    Parameters:
    *children: The content inside the <figure> tag.
    **attributes: HTML attributes for the <figure> tag.

    Returns:
    htmlElement: An object representing the <figure> tag.
    """
    return htmlElement("figure", *children, **attributes)


def figcaption(*children, **attributes):
    """
    Defines a caption for a <figure> element.

    Parameters:
    *children: The content inside the <figcaption> tag.
    **attributes: HTML attributes for the <figcaption> tag.

    Returns:
    htmlElement: An object representing the <figcaption> tag.
    """
    return htmlElement("figcaption", *children, **attributes)


def kbd(*children, **attributes):
    """
    Defines keyboard input.

    Parameters:
    *children: The content inside the <kbd> tag.
    **attributes: HTML attributes for the <kbd> tag.

    Returns:
    htmlElement: An object representing the <kbd> tag.
    """
    return htmlElement("kbd", *children, **attributes)


def mark(*children, **attributes):
    """
    Defines marked/highlighted text.

    Parameters:
    *children: The content inside the <mark> tag.
    **attributes: HTML attributes for the <mark> tag.

    Returns:
    htmlElement: An object representing the <mark> tag.
    """
    return htmlElement("mark", *children, **attributes)


def progress(*children, **attributes):
    """
    Represents the progress of a task.

    Parameters:
    *children: The content inside the <progress> tag.
    **attributes: HTML attributes for the <progress> tag, such as 'max', 'value'.

    Returns:
    htmlElement: An object representing the <progress> tag.
    """
    return htmlElement("progress", *children, **attributes)


def ruby(*children, **attributes):
    """
    Defines a ruby annotation.

    Parameters:
    *children: The content inside the <ruby> tag, typically <rt> and <rp> elements.
    **attributes: HTML attributes for the <ruby> tag.

    Returns:
    htmlElement: An object representing the <ruby> tag.
    """
    return htmlElement("ruby", *children, **attributes)


def rt(*children, **attributes):
    """
    Defines an explanation/pronunciation of characters (for East Asian typography).

    Parameters:
    *children: The content inside the <rt> tag.
    **attributes: HTML attributes for the <rt> tag.

    Returns:
    htmlElement: An object representing the <rt> tag.
    """
    return htmlElement("rt", *children, **attributes)


def rp(*children, **attributes):
    """
    Defines what to show in browsers that do not support ruby annotations.

    Parameters:
    *children: The content inside the <rp> tag.
    **attributes: HTML attributes for the <rp> tag.

    Returns:
    htmlElement: An object representing the <rp> tag.
    """
    return htmlElement("rp", *children, **attributes)


def s(*children, **attributes):
    """
    Defines text that is no longer correct.

    Parameters:
    *children: The content inside the <s> tag.
    **attributes: HTML attributes for the <s> tag.

    Returns:
    htmlElement: An object representing the <s> tag.
    """
    return htmlElement("s", *children, **attributes)


def samp(*children, **attributes):
    """
    Defines sample output from a computer program.

    Parameters:
    *children: The content inside the <samp> tag.
    **attributes: HTML attributes for the <samp> tag.

    Returns:
    htmlElement: An object representing the <samp> tag.
    """
    return htmlElement("samp", *children, **attributes)


def summary(*children, **attributes):
    """
    Defines a visible heading for a <details> element.

    Parameters:
    *children: The content inside the <summary> tag.
    **attributes: HTML attributes for the <summary> tag.

    Returns:
    htmlElement: An object representing the <summary> tag.
    """
    return htmlElement("summary", *children, **attributes)


def time(*children, **attributes):
    """
    Defines a specific time/date.

    Parameters:
    *children: The content inside the <time> tag.
    **attributes: HTML attributes for the <time> tag.

    Returns:
    htmlElement: An object representing the <time> tag.
    """
    return htmlElement("time", *children, **attributes)


def track(**attributes):
    """
    Defines text tracks for <video> and <audio> elements.

    Parameters:
    **attributes: HTML attributes for the <track> tag, such as 'kind', 'src', 'srclang', 'label'.

    Returns:
    htmlElement: An object representing the <track> tag.
    """
    return htmlElement("track", **attributes)


def var(*children, **attributes):
    """
    Defines a variable in programming or in a mathematical expression.

    Parameters:
    *children: The content inside the <var> tag.
    **attributes: HTML attributes for the <var> tag.

    Returns:
    htmlElement: An object representing the <var> tag.
    """
    return htmlElement("var", *children, **attributes)


def wbr():
    """
    Specifies a possible line-break.

    Returns:
    htmlElement: An object representing the <wbr> tag.
    """
    return htmlElement("wbr")