parser grammar JuniperParser;

options {
  tokenVocab = JuniperLexer;
}

braced_clause
:
  OPEN_BRACE statement* CLOSE_BRACE
;

bracketed_clause
:
  OPEN_BRACKET word+ CLOSE_BRACKET
;

juniper_configuration
:
  statement+ EOF
;

statement
:
  (
    INACTIVE
    | REPLACE
  )? words += word+
  (
    braced_clause
    |
    (
      bracketed_clause terminator
    )
    | terminator
  )
;

terminator
:
  SEMICOLON
;

word
:
  WORD
;