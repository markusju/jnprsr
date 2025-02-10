# Generated from JuniperParser.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,1,1,1,1,4,1,24,8,1,11,1,12,
        1,25,1,1,1,1,1,2,4,2,31,8,2,11,2,12,2,32,1,2,1,2,1,3,3,3,38,8,3,
        1,3,4,3,41,8,3,11,3,12,3,42,1,3,1,3,1,3,1,3,1,3,3,3,50,8,3,1,4,1,
        4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,2,0,1,1,5,5,56,0,12,1,0,0,0,
        2,21,1,0,0,0,4,30,1,0,0,0,6,37,1,0,0,0,8,51,1,0,0,0,10,53,1,0,0,
        0,12,16,5,8,0,0,13,15,3,6,3,0,14,13,1,0,0,0,15,18,1,0,0,0,16,14,
        1,0,0,0,16,17,1,0,0,0,17,19,1,0,0,0,18,16,1,0,0,0,19,20,5,2,0,0,
        20,1,1,0,0,0,21,23,5,9,0,0,22,24,3,10,5,0,23,22,1,0,0,0,24,25,1,
        0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,3,0,0,28,
        3,1,0,0,0,29,31,3,6,3,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,
        0,32,33,1,0,0,0,33,34,1,0,0,0,34,35,5,0,0,1,35,5,1,0,0,0,36,38,7,
        0,0,0,37,36,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,41,3,10,5,0,40,
        39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,49,1,0,0,
        0,44,50,3,0,0,0,45,46,3,2,1,0,46,47,3,8,4,0,47,50,1,0,0,0,48,50,
        3,8,4,0,49,44,1,0,0,0,49,45,1,0,0,0,49,48,1,0,0,0,50,7,1,0,0,0,51,
        52,5,11,0,0,52,9,1,0,0,0,53,54,5,12,0,0,54,11,1,0,0,0,6,16,25,32,
        37,42,49
    ]

class JuniperParser ( Parser ):

    grammarFileName = "JuniperParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'replace:'", "'}'", "']'", "')'", "'inactive:'", 
                     "<INVALID>", "<INVALID>", "'{'", "'['", "'('", "';'" ]

    symbolicNames = [ "<INVALID>", "REPLACE", "CLOSE_BRACE", "CLOSE_BRACKET", 
                      "CLOSE_PAREN", "INACTIVE", "LINE_COMMENT", "MULTILINE_COMMENT", 
                      "OPEN_BRACE", "OPEN_BRACKET", "OPEN_PAREN", "SEMICOLON", 
                      "WORD", "WS" ]

    RULE_braced_clause = 0
    RULE_bracketed_clause = 1
    RULE_juniper_configuration = 2
    RULE_statement = 3
    RULE_terminator = 4
    RULE_word = 5

    ruleNames =  [ "braced_clause", "bracketed_clause", "juniper_configuration", 
                   "statement", "terminator", "word" ]

    EOF = Token.EOF
    REPLACE=1
    CLOSE_BRACE=2
    CLOSE_BRACKET=3
    CLOSE_PAREN=4
    INACTIVE=5
    LINE_COMMENT=6
    MULTILINE_COMMENT=7
    OPEN_BRACE=8
    OPEN_BRACKET=9
    OPEN_PAREN=10
    SEMICOLON=11
    WORD=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Braced_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(JuniperParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(JuniperParser.CLOSE_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuniperParser.StatementContext)
            else:
                return self.getTypedRuleContext(JuniperParser.StatementContext,i)


        def getRuleIndex(self):
            return JuniperParser.RULE_braced_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBraced_clause" ):
                listener.enterBraced_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBraced_clause" ):
                listener.exitBraced_clause(self)




    def braced_clause(self):

        localctx = JuniperParser.Braced_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_braced_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(JuniperParser.OPEN_BRACE)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JuniperParser.REPLACE) | (1 << JuniperParser.INACTIVE) | (1 << JuniperParser.WORD))) != 0):
                self.state = 13
                self.statement()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(JuniperParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bracketed_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(JuniperParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(JuniperParser.CLOSE_BRACKET, 0)

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuniperParser.WordContext)
            else:
                return self.getTypedRuleContext(JuniperParser.WordContext,i)


        def getRuleIndex(self):
            return JuniperParser.RULE_bracketed_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracketed_clause" ):
                listener.enterBracketed_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracketed_clause" ):
                listener.exitBracketed_clause(self)




    def bracketed_clause(self):

        localctx = JuniperParser.Bracketed_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bracketed_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(JuniperParser.OPEN_BRACKET)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.word()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==JuniperParser.WORD):
                    break

            self.state = 27
            self.match(JuniperParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Juniper_configurationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(JuniperParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuniperParser.StatementContext)
            else:
                return self.getTypedRuleContext(JuniperParser.StatementContext,i)


        def getRuleIndex(self):
            return JuniperParser.RULE_juniper_configuration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJuniper_configuration" ):
                listener.enterJuniper_configuration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJuniper_configuration" ):
                listener.exitJuniper_configuration(self)




    def juniper_configuration(self):

        localctx = JuniperParser.Juniper_configurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_juniper_configuration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self.statement()
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JuniperParser.REPLACE) | (1 << JuniperParser.INACTIVE) | (1 << JuniperParser.WORD))) != 0)):
                    break

            self.state = 34
            self.match(JuniperParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._word = None # WordContext
            self.words = list() # of WordContexts

        def braced_clause(self):
            return self.getTypedRuleContext(JuniperParser.Braced_clauseContext,0)


        def terminator(self):
            return self.getTypedRuleContext(JuniperParser.TerminatorContext,0)


        def INACTIVE(self):
            return self.getToken(JuniperParser.INACTIVE, 0)

        def REPLACE(self):
            return self.getToken(JuniperParser.REPLACE, 0)

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JuniperParser.WordContext)
            else:
                return self.getTypedRuleContext(JuniperParser.WordContext,i)


        def bracketed_clause(self):
            return self.getTypedRuleContext(JuniperParser.Bracketed_clauseContext,0)


        def getRuleIndex(self):
            return JuniperParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = JuniperParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JuniperParser.REPLACE or _la==JuniperParser.INACTIVE:
                self.state = 36
                _la = self._input.LA(1)
                if not(_la==JuniperParser.REPLACE or _la==JuniperParser.INACTIVE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                localctx._word = self.word()
                localctx.words.append(localctx._word)
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==JuniperParser.WORD):
                    break

            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JuniperParser.OPEN_BRACE]:
                self.state = 44
                self.braced_clause()
                pass
            elif token in [JuniperParser.OPEN_BRACKET]:
                self.state = 45
                self.bracketed_clause()
                self.state = 46
                self.terminator()
                pass
            elif token in [JuniperParser.SEMICOLON]:
                self.state = 48
                self.terminator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(JuniperParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return JuniperParser.RULE_terminator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminator" ):
                listener.enterTerminator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminator" ):
                listener.exitTerminator(self)




    def terminator(self):

        localctx = JuniperParser.TerminatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_terminator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(JuniperParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(JuniperParser.WORD, 0)

        def getRuleIndex(self):
            return JuniperParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWord" ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWord" ):
                listener.exitWord(self)




    def word(self):

        localctx = JuniperParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(JuniperParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





