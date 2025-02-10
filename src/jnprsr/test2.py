from JuniperParser import JuniperParser

class JunosFlattenedTreeNode:
    def __init__(self, path: list, terminalNode: str):
        self._path = path
        self._terminalNode = terminalNode

    def getPath(self):
        return self._path

    def getTerminalNode(self):
        return self._terminalNode

    def __eq__(self, other):
        if isinstance(other, JunosFlattenedTreeNode):
            return self.getTerminalNode() == other.getTerminalNode() and self.getPath() == other.getPath()

        return False

    def __hash__(self):
        buf = ""
        for el in self.getPath():
            buf += el

        return hash(buf+self.getTerminalNode())

    def __str__(self):
        return str(self.getPath()) + " " + str(self.getTerminalNode())

    def __repr__(self):
        return self.__str__()


def flatten(configTree):
    flattenedNodes = []

    def _flatten(tree, path):
        if isinstance(tree, JuniperParser.StatementContext):
            if any(isinstance(x, JuniperParser.TerminatorContext) for x in tree.getChildren()):
                buf = ""
                for elb in tree.getChildren():

                    if isinstance(elb, JuniperParser.TerminatorContext):
                        continue

                    # Special treatment for brackets
                    if isinstance(elb, JuniperParser.Bracketed_clauseContext):
                        for elc in elb.getChildren():
                            buf += elc.getText()
                            buf += " "
                    else:
                        buf += elb.getText()
                        buf += " "

                flatNode = JunosFlattenedTreeNode(path, buf.strip())
                flattenedNodes.append(flatNode)
        for ela in tree.getChildren():
            if isinstance(ela, JuniperParser.Braced_clauseContext) or isinstance(ela, JuniperParser.StatementContext):

                # Determine Path in Tree
                if isinstance(ela, JuniperParser.Braced_clauseContext):
                    buf = ""
                    for elc in ela.parentCtx.getChildren():

                        # Gather all word elements in the parent context
                        if isinstance(elc, JuniperParser.WordContext):
                            buf += elc.getText()
                            buf += " "

                    path.append(buf.strip())

                # Warning: Python is pass-by-reference. Deep copy is needed for the path traversal to work correctly...
                _flatten(ela, list(path))
            else:
                continue

    _flatten(configTree, [])
    return flattenedNodes


class JunosTreeBuilder:
    def __init__(self):
        self.tree = {}
        self.pointer = None

    def addFlattenedNode(self, node: JunosFlattenedTreeNode):
        self.pointer = self.tree

        for ela in node.getPath():
            if ela in self.pointer.keys():
                self.pointer = self.pointer[ela]
            else:
                self.pointer[ela] = {}
                self.pointer = self.pointer[ela]

        # Get all config elements on this level
        keys = self.pointer.keys()
        # Split new Terminal node
        terminalNodeElements = node.getTerminalNode().split(" ")

        # This is to ensure a proper 'load merge'
        if len(terminalNodeElements) == 2 and False:
            for elb in keys:
                if terminalNodeElements[0] in elb:
                    if (elb.split(" "))[0] == terminalNodeElements[0]:
                        # Delete existing config statement with prefix
                        del self.pointer[elb]
                        self.pointer[node.getTerminalNode()] = {}
                        return

        self.pointer[node.getTerminalNode()] = {}

    def _getConf(self, conf):
        buf = ""
        for ela in conf.keys():
            if bool(conf[ela]):
                # Recursion!
                buf += ela + " { \n" + self._getConf(conf[ela]) + "}\n"
            else:
                buf += ela + ";\n"
        return buf

    def get(self):
        return self._getConf(self.tree)