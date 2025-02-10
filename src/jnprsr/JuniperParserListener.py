# Generated from JuniperParser.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from jnprsr.JuniperParser import JuniperParser
else:
    from jnprsr.JuniperParser import JuniperParser


# This class defines a complete listener for a parse tree produced by JuniperParser.
class JuniperParserListener(ParseTreeListener):

    # Enter a parse tree produced by JuniperParser#braced_clause.
    def enterBraced_clause(self, ctx:JuniperParser.Braced_clauseContext):
        pass

    # Exit a parse tree produced by JuniperParser#braced_clause.
    def exitBraced_clause(self, ctx:JuniperParser.Braced_clauseContext):
        pass


    # Enter a parse tree produced by JuniperParser#bracketed_clause.
    def enterBracketed_clause(self, ctx:JuniperParser.Bracketed_clauseContext):
        pass

    # Exit a parse tree produced by JuniperParser#bracketed_clause.
    def exitBracketed_clause(self, ctx:JuniperParser.Bracketed_clauseContext):
        pass


    # Enter a parse tree produced by JuniperParser#juniper_configuration.
    def enterJuniper_configuration(self, ctx:JuniperParser.Juniper_configurationContext):
        pass

    # Exit a parse tree produced by JuniperParser#juniper_configuration.
    def exitJuniper_configuration(self, ctx:JuniperParser.Juniper_configurationContext):
        pass


    # Enter a parse tree produced by JuniperParser#statement.
    def enterStatement(self, ctx:JuniperParser.StatementContext):
        pass

    # Exit a parse tree produced by JuniperParser#statement.
    def exitStatement(self, ctx:JuniperParser.StatementContext):
        pass


    # Enter a parse tree produced by JuniperParser#terminator.
    def enterTerminator(self, ctx:JuniperParser.TerminatorContext):
        pass

    # Exit a parse tree produced by JuniperParser#terminator.
    def exitTerminator(self, ctx:JuniperParser.TerminatorContext):
        pass


    # Enter a parse tree produced by JuniperParser#word.
    def enterWord(self, ctx:JuniperParser.WordContext):
        pass

    # Exit a parse tree produced by JuniperParser#word.
    def exitWord(self, ctx:JuniperParser.WordContext):
        pass



del JuniperParser