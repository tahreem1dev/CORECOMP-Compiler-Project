# lexer.py
# simple lexer for CoreLang
# tokenizes keywords, identifiers, literals, operators, separators

import re

class Token:
    def __init__(self, type, value, line=0):
        self.type = type   # token type (IDENTIFIER, INT_LITERAL, FLOAT_LITERAL, KEYWORD, OPERATOR, SEP)
        self.value = value # actual token value
        self.line = line   # line number (default 0)

class lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.tokens = []

        # language definitions
        self.keywords = ['program', 'int', 'float']
        self.operators = ['=']
        self.separators = [';', '{', '}']

    def tokenize(self):
        # split source code into words / symbols
        words = re.findall(r'\d+\.\d+|\d+|\w+|[{};=]', self.text)
        for w in words:
            # keyword
            if w in self.keywords:
                self.tokens.append(Token('KEYWORD', w))
            # operator
            elif w in self.operators:
                self.tokens.append(Token('OPERATOR', w))
            # separator
            elif w in self.separators:
                self.tokens.append(Token('SEP', w))
            # float literal
            elif re.match(r'^\d+\.\d+$', w):
                self.tokens.append(Token('FLOAT_LITERAL', w))
            # int literal
            elif re.match(r'^\d+$', w):
                self.tokens.append(Token('INT_LITERAL', w))
            # identifier
            else:
                self.tokens.append(Token('IDENTIFIER', w))
        return self.tokens

