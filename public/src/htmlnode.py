class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props != None:
            props_html = ""
            for prop in self.props: 
                props_html += f' {prop}="{self.props[prop]}"'
            return props_html
        return ""

    def __repr__(self):
        return(f"\n"
            f"HTML Node...\n"
            f"Tag: {self.tag}\n"
            f"Value: {self.value}\n"
            f"Children: {self.children}\n"
            f"Properties: {self.props}\n"
        )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return(f"\n"
            f"LEAF Node...\n"
            f"Tag: {self.tag}\n"
            f"Value: {self.value}\n"
            f"Properties: {self.props}\n"
        )
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        html = ""
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
    
    def __repr__(self):
        return(f"\n"
            f"PARENT Node...\n"
            f"Tag: {self.tag}\n"
            f"Children: {self.children}\n"
            f"Properties: {self.props}\n"
        )