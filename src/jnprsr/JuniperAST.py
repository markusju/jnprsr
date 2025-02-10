from jnprsr.JuniperParserListener import JuniperParserListener
from jnprsr.JuniperParser import JuniperParser
from anytree import Node, NodeMixin
from anytree.node.util import _repr

class JuniperASTNode(NodeMixin, object):
    def __init__(self, name, parent=None):
        self.name = name
        self.key = ""
        self.value = ""
        self.parent = parent
        self.separator = " "
        super(JuniperASTNode, self).__init__()

    def is_juniper_bracketed_clause(self):
        return "[" in self.name and "]" in self.name

    def is_juniper_leaf_node(self):
        return self.is_leaf

    def is_juniper_container_node(self):
        return not self.is_leaf

    def append_value(self, value):
        if not self.is_juniper_bracketed_clause():
            raise ValueError("Can only be used on bracketed clauses")
        self.value += value
        self.name = self.key + " [" + self.value + " ]"

    def __repr__(self):
        args = ["%r" % " ".join([""] + [str(node.name) for node in self.path])]
        return _repr(self, args=args, nameblacklist=["name", "value", "key"])

class JuniperAST(JuniperParserListener):
    """
    This Class inherits from the JuniperParserListener created by ANTLR4.
    We are hooking onto various methods called during tree traversal to print out the config.
    A buffer used inside the class collects the configuration tree reconstructed from the the tree.
    """
    def __init__(self):
        self.root = JuniperASTNode("root")
        self.point = self.root
        self.depth = 0
        self.in_bracketed_clause = False

        # Enter a parse tree produced by JuniperParser#braced_clause.
    def enterBraced_clause(self, ctx: JuniperParser.Braced_clauseContext):
        pass

        # Exit a parse tree produced by JuniperParser#braced_clause.

    def exitBraced_clause(self, ctx: JuniperParser.Braced_clauseContext):
        #pass
        self.point = self.point.parent

        # Enter a parse tree produced by JuniperParser#bracketed_clause.

    def enterBracketed_clause(self, ctx: JuniperParser.Bracketed_clauseContext):
        self.point.name += " ["
        # Exit a parse tree produced by JuniperParser#bracketed_clause.

    def exitBracketed_clause(self, ctx: JuniperParser.Bracketed_clauseContext):
        self.point.name += " ]"
        # Enter a parse tree produced by JuniperParser#juniper_configuration.

    def enterJuniper_configuration(self, ctx: JuniperParser.Juniper_configurationContext):
        pass

        # Exit a parse tree produced by JuniperParser#juniper_configuration.

    def exitJuniper_configuration(self, ctx: JuniperParser.Juniper_configurationContext):
        pass

        # Enter a parse tree produced by JuniperParser#statement.

    def enterStatement(self, ctx: JuniperParser.StatementContext):
        node = JuniperASTNode(name="", parent=self.point)
        self.point = node
        # Exit a parse tree produced by JuniperParser#statement.

    def exitStatement(self, ctx: JuniperParser.StatementContext):
        pass
        # Enter a parse tree produced by JuniperParser#terminator.

    def enterTerminator(self, ctx: JuniperParser.TerminatorContext):
        pass
        # Exit a parse tree produced by JuniperParser#terminator.

    def exitTerminator(self, ctx: JuniperParser.TerminatorContext):
        self.point = self.point.parent
        # Enter a parse tree produced by JuniperParser#word.

    def enterWord(self, ctx: JuniperParser.WordContext):
        if self.in_bracketed_clause:
            node = JuniperASTNode(name="", parent=self.point)
            self.point = node

        if len(self.point.name) < 1:
            self.point.name += ctx.getText()
            self.point.key = ctx.getText()
        else:
            self.point.name += " " + ctx.getText()
            self.point.value += " " + ctx.getText()

        if self.in_bracketed_clause:
            self.point = self.point.parent
        # Exit a parse tree produced by JuniperParser#word.

    def exitWord(self, ctx: JuniperParser.WordContext):
        pass


