from ast import operator
from utils.atokenizer import Tokenizer
from utils.achecker import *
from utils.aexpression import *

class Algoritma(Tokenizer):
    _reserved_keyword = [
        'ALGORITMA',
        # control flow
        'if',
        'else',
        'then',
        'depends',
        'on',

        # loop
        'while',
        'do',
        'repeat',
        'times',
        'until',
        'iterate',
        'stop',
        'traversal',

        # arith op
        'div', 
        'mod',
        
        # logic op
        'not',
        'or', 
        'and',
    ]

    _keyword_operator = [
        # arith op
        'div', 
        'mod',
        
        # logic op
        'not',
        'or', 
        'and',
    ]
    _reserved_operator = [
        '<-',
        '+',
        '-', 
        '/', 
        '^',
        '->'
    ]

    _braces = ['[', ']']

    def __init__(self, register, r_str: str, a_line: int, a_charidx: int) -> None:
        super().__init__(r_str, self._reserved_keyword, self._reserved_operator, self._keyword_operator, self._braces, a_line, a_charidx)
        self.a_line = a_line
        self.a_charidx = a_charidx
        self.register = register
                
    def __call__(self):
        atokens = list(reversed([t for t in self.tokens if t.ttype != "COMMENT"]))
        tok = atokens.pop()

        # clean left over kamus / lokal
        if tok.value == "ALGORITMA":
            atokens.pop()

        print("TOKENS:")
        show_tokens(self)
        print()
        print("REGISTER AWAL:")
        show_register(self)
        print()
        try:
            while len(atokens):
                tok = atokens.pop()
                expression_list = [tok]
                while tok.ttype != "NEWLINE":
                    tok = atokens.pop()
                    expression_list.append(tok)
                self.__process_expression(expression_list)

                enter = atokens.pop()
                if enter.ttype != "NEWLINE":
                    raise SyntaxError
        except:
            pass
        
        print("REGISTER AKHIR:")
        show_register(self)
    
    def __process_expression(self, tokens: list):
        # procedure call di skip dulu
        # basic arithmetic
        
        pass