from enum import Enum
import re

class Token:
    def __init__(self, tokenText, tokenKind) -> None:
        self.text = tokenText
        self.kind = tokenKind

    def __repr__(self):
        return f'Token({self.kind.name}, {self.text})'

class TokenType(Enum):
    STRING = 'STRING'
    NUMBER = 'NUMBER'
    DIGIT = 'DIGIT'
    IDENTIFIER = 'IDENTIFIER'
    OPERATOR = 'OPERATOR'

token_regex = re.compile(
    r'(?P<STRING>"[^"]*")|' +
    r'(?P<NUMBER>[0-9]+)|' +
    r'(?P<DIGIT>[1-9][0-9]*|0)|' +
    r'(?P<IDENTIFIER>[A-Za-z_$][A-Za-z0-9_$]*)|' +
    r'(?P<OPERATOR>\+|\-|\*|/|==|!=|<=|>=|<|>|=|;)'
)

