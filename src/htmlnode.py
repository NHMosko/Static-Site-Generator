from functools import reduce

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props:
            return f" {" ".join(f'{k}="{v}"' for k, v in self.props.items())}"
        return ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value:
            if self.tag:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            return self.value   
        raise ValueError("All leaf nodes must have a value")

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag:
            if self.children:
                final_text = f"<{self.tag}>"
                for child in self.children:
                    final_text += child.to_html()
                return final_text + f"</{self.tag}>"
            raise ValueError("Parent node needs children")
        raise ValueError("Parent node needs a tag")
