import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import src.pyhtmlify.HTMLTags.tags as tags


# Example data for lists and tables
items = ["Item 1", "Item 2", "Item 3"]
table_data = [["Row 1 Col 1", "Row 1 Col 2"], ["Row 2 Col 1", "Row 2 Col 2"]]

def index():
    return tags.html(
        tags.head(
            tags.title("Comprehensive HTML Page"),
            tags.meta(charset="UTF-8"),
            tags.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            tags.link(rel="stylesheet", href="styles.css")
        ),
        tags.body(
            tags.header(
                tags.h1("Comprehensive HTML Page"),
                tags.nav(
                    tags.ul(
                        tags.li(tags.a("Home", href="#home")),
                        tags.li(tags.a("About", href="#about")),
                        tags.li(tags.a("Contact", href="#contact"))
                    )
                )
            ),
            tags.main(
                tags.section(
                    tags.h2("Introduction"),
                    tags.p("This is an example of a comprehensive HTML page using all elements.")
                ),
                tags.section(
                    tags.h3("Lists"),
                    tags.h4("Unordered List"),
                    tags.ul(*[tags.li(item) for item in items]),
                    tags.h4("Ordered List"),
                    tags.ol(*[tags.li(item) for item in items])
                ),
                tags.section(
                    tags.h3("Table"),
                    tags.table(
                        tags.tr(tags.th("Column 1"), tags.th("Column 2")),
                        *[tags.tr(tags.td(cell1), tags.td(cell2)) for cell1, cell2 in table_data]
                    )
                ),
                tags.section(
                    tags.h3("Form Example"),
                    tags.form(
                        tags.label("Name:", for_="name"),
                        tags.input(type="text", id="name", name="name"),
                        tags.br(),
                        tags.label("Message:", for_="message"),
                        tags.textarea(id="message", name="message")("Your message here..."),
                        tags.br(),
                        tags.button("Submit", type="submit")
                    )
                ),
                tags.article(
                    tags.h3("Article Section"),
                    tags.p("This is an article within the main content."),
                    tags.img(src="image.jpg", alt="Example Image"),
                    tags.hr()
                ),
                tags.aside(
                    tags.h4("Aside Section"),
                    tags.p("This is an aside section, usually for additional content or advertisements.")
                )
            ),
            tags.footer(
                tags.address(
                    tags.p("1234 Example St."),
                    tags.p("City, State, ZIP")
                ),
                tags.p("© 2024 Your Company")
            ),
            tags.script("console.log('This is a test script in pyhtmlify');"),
            tags.style("body { font-family: Arial, sans-serif; }"),
            tags.noscript("Your browser does not support JavaScript.")
        )
    )
