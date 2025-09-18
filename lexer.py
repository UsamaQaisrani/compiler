import enum, sys

class Lexer:
    def __init__(self, source):
        self.source = source
        self.currChar = ""
        self.currPos = -1
        self.nextChar()

    def nextChar(self):
        self.currPos += 1
        if self.currPos >= len(self.source):
            self.currChar = "\0" #EOF
        else:
            self.currChar = self.source[self.currPos]

    def peek(self):
        if self.currPos + 1 >= len(self.source):
            return "\0"
        else:
            return self.source[self.currPos+1]
    
    def abort(self, message):
        sys.exit(f"Lexing error. {message}")

    def skipWhiteSpace(self):
        while self.currChar == " " or self.currChar == "\t" or self.currChar == "\r":
            self.nextChar()

    def skipComment(self):
        pass

    def getToken(self):
        self.skipWhiteSpace()
        token = None
        if self.currChar == "+":
            token = Token(self.currChar, TokenType.PLUS)
        elif self.currChar == "-":
            token = Token(self.currChar, TokenType.MINUS)
        elif self.currChar == "*":
            token = Token(self.currChar, TokenType.ASTERISK)
        elif self.currChar == "/":
            token = Token(self.currChar, TokenType.SLASH)
        elif self.currChar == "\n":
            token = Token(self.currChar, TokenType.NEWLINE)
        elif self.currChar == "\0":
            token = Token(self.currChar, TokenType.EOF)
        else:
            self.abort(f"Unkown token: {self.currChar}")

        self.nextChar()
        return token
        
class Token:
    def __init__(self, tokenText, tokenKind) -> None:
        self.text = tokenText
        self.kind = tokenKind

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3

    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111

    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211

