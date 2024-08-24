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