class JuniperASTRenderer():
    def __init__(self):
        self.indent = "    "
        self.buffer = ""

    def render(self, node):
        self.buffer = ""
        self.__render(node, level=-1)
        return self.buffer

    def __render(self, node, level):
        # Skip artificial root node
        if level > -1:
            self.buffer += self.indent * level + node.name
            if node.children:
                self.buffer += " {\n"
            else:
                self.buffer += ";\n"
        # Recursion!
        children = [self.__render(child, level=level+1) for child in node.children]
        # Skip closing bracket of artificial root node
        if children and level > -1:
            self.buffer += self.indent * level + "}\n"