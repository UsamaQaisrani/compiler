from lexer_token import *

class Lexer:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.getTokens()

    def getTokens(self):
        for match in token_regex.finditer(self.source):
            token_text = match.group(0)
            token_type_name = match.lastgroup
            assert token_type_name is not None, 'Matched token has no group name!'
            token_type = TokenType[token_type_name] 
            token = Token(token_text, token_type)
            self.tokens.append(token)
            print(token.kind, token.text)


            


        

