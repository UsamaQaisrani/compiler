import sys
from lexer import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.symbols = set()
        self.labelsDecalred = set()
        self.labelsGotoed = set()
        self.currToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()

    def checkToken(self, kind):
        return kind == self.currToken.kind
    
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    def match(self, kind):
        if not self.checkToken(kind):
            self.abort(f"Expected {kind.name}, got {self.currToken.kind.name}")
        self.nextToken()

    def nextToken(self):
        self.currToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def abort(self, message):
        sys.exit(f"Error. {message}")

    def program(self):
        print("PROGRAM")
        
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        while not self.checkToken(TokenType.EOF):
            self.statement()

        for label in self.labelsGotoed:
            if label not in self.labelsDecalred:
                self.abort(f"Attempting to GOTO undeclared label: {label}")
    
    def statement(self):
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                self.nextToken()
            else:
                self.expression()

        elif self.checkToken(TokenType.IF):
            print("STATEMENT-IF")
            self.nextToken()
            self.comparison()
            self.match(TokenType.THEN)
            self.nl()
            while not self.checkToken(TokenType.ENDIF):
                self.statement()
            self.match(TokenType.ENDIF)
        elif self.checkToken(TokenType.WHILE):

            print("STATEMENT-WHILE")
            self.nextToken()
            self.comparison()
            self.match(TokenType.REPEAT)
            self.nl()
            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()
            self.match(TokenType.ENDWHILE)

        elif self.checkToken(TokenType.LABEL):
            print("STATEMENT-LABEL")
            self.nextToken()
            if self.currToken.text in self.labelsDecalred:
                self.abort(f"Label already exists: {self.currToken.text}")
            self.labelsDecalred.add(self.currToken.text)
            self.match(TokenType.IDENT)

        elif self.checkToken(TokenType.GOTO):
            print("STATEMENT-GOTO")
            self.nextToken()
            self.labelsGotoed.add(self.currToken.text)
            self.match(TokenType.IDENT)

        elif self.checkToken(TokenType.LET):
            print("STATEMENT-LET")
            self.nextToken()
            if self.currToken.text not in self.symbols:
                self.symbols.add(self.currToken.text)
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            self.expression()

        elif self.checkToken(TokenType.INPUT):
            print("STATEMENT-INPUT")
            self.nextToken()
            if self.currToken.text not in self.symbols:
                self.symbols.add(self.currToken.text)
            self.match(TokenType.IDENT)
        else:
            self.abort(f"Invalid statement at {self.currToken.text} ({self.currToken.kind.name})")

        self.nl()

    def expression(self):
        print("EXPRESSION")
        self.term()
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()
            self.term()

    def term(self):
        print("TERM")
        self.unary()
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.nextToken()
            self.unary()

    def unary(self):
        print("UNARY")
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()
        self.primary()

    def primary(self):
        print(f"PRIMARY ({self.currToken.text})")
        if self.checkToken(TokenType.NUMBER):
            self.nextToken()
        elif self.checkToken(TokenType.IDENT):
            if self.currToken.text not in self.symbols:
                self.abort(f"Referencing variable before assignment: {self.currToken.text}")
            self.nextToken()
        else:
            self.abort(f"Unexpected token at: {self.currToken.text}")


    def comparison(self):
        print("COMPARISON")
        self.expression()

        if self.isComparisonOperator():
            self.nextToken()
            self.expression()
        else:
            self.abort(f"Expected comparision operator at: {self.currToken.text}")

        while self.isComparisonOperator():
            self.nextToken()
            self.expression()

    def isComparisonOperator(self):
        return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)

    def nl(self):
        print("NEWLINE")
        self.match(TokenType.NEWLINE)
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
