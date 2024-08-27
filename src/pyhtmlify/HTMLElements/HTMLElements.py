import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class htmlElement:
    def __init__(self, tag, *children, **attributes):
        self.tag = tag
        self.children = children  # Store children as is
        self.attributes = attributes

    def __str__(self):
        # Create the attribute string
        attr_str = " ".join(
            f'{k.replace("_", "")}="{v}"' for k, v in self.attributes.items()
        ).strip()

        # Recursively convert children to strings
        children_str = "".join(str(child) for child in self.children)

        # Special case for DOCTYPE
        if self.tag.lower() == "!doctype html":
            return "<!DOCTYPE html>"

        # Handle self-closing tags
        if not self.children:
            return f"<{self.tag} {attr_str} />".strip()
        else:
            return f"<{self.tag} {attr_str}>{children_str}</{self.tag}>".strip()

        
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
        self.condition = condition
        self.true_children = list(true_children)
        self.false_children = list(false_children) if false_children else []

    def __str__(self):
        true_block = "".join(str(child) for child in self.true_children)
        false_block = "".join(str(child) for child in self.false_children)

        if false_block:
            return f"{{% if {self.condition} %}}{true_block}{{% else %}}{false_block}{{% endif %}}"
        else:
            return f"{{% if {self.condition} %}}{true_block}{{% endif %}}"

    def __repr__(self):
        return self.__str__()
        