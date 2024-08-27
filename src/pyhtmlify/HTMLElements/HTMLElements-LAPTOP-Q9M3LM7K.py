import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class htmlElement:
    def __init__(self, tag, *children, **attributes):
        self.tag = tag
        self.children = children
        self.attributes = attributes

    def __str__(self):
        attr_str = " ".join(
            f'{k.replace("_", "")}="{v}"' for k, v in self.attributes.items()
        )
        children_str = "".join(str(child) for child in self.children)
        if self.tag == "!DOCTYPE html":
            return f"<!{self.tag}>"
        elif not self.children:
            return f"<{self.tag} {attr_str} />"
        else:
            return f"<{self.tag} {attr_str}>{children_str}</{self.tag}>"
        
class TextAreaElement(htmlElement):
        def __init__(self, tag, *children, **attributes):
            super().__init__(tag, *children, **attributes)
            self.children = list(self.children)  # Ensure children is a list

        def __call__(self, *children):
            self.children.extend(children)
            return self
        
class InputElement(htmlElement):
        def __str__(self):
            attr_str = " ".join(
                f'{k.replace("_", "-")}="{v}"' for k, v in self.attributes.items()
            )
            return f"<{self.tag} {attr_str} />"
        
class IfElement(htmlElement):
    def __init__(self, condition, *true_children, false_children=None):
        super().__init__("div")  # Use a generic div as a container
        self.children = []  # Initialize children as an empty list
        if condition:
            self.children.extend(list(true_children))  # Convert to list before extending
        elif false_children:
            self.children.extend(list(false_children))  # Convert to list before extending

    def __str__(self):
        return "".join(str(child) for child in self.children)