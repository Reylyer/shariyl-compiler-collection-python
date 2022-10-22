from .utils.atokenizer import Tokenizer

class Algoritma(Tokenizer):
    _reserved_keyword = [
        'ALGORITMA',
        'if',
        'else',
        'then',

        'depends',
        'on',
        'while',
        'do',
        'repeat',
        'times',
        'until',
        'iterate',
        'stop',
        'traversal',
    ]

    _reserved_operator = [
        '<-',
        '+',
        '-', 
        '/', 
        'div', 
        'mod', 
        '^',

        'not',
        'or', 
        'and',

        '->'
        ]

    _braces = ['[', ']']

    def __init__(self, register, r_str: str, a_line: int, a_charidx: int) -> None:
        super().__init__(r_str, self._reserved_keyword, self._reserved_operator, self._braces, a_line, a_charidx)
        self.a_line = a_line
        self.a_charidx = a_charidx
        self.register = register
                
    def show_tokens(self) -> None:
        for idx, tok in enumerate(self.ktokens):
            print(f"{idx: <4}{tok.ttype: <12} {tok.line}:{tok.charidx} {tok.value}")

    def show_register(self) -> None:
        for idx, (identifier, reg) in enumerate(self.register.items()):
            print(f"{idx: <4}{identifier:<10}: {reg.type} = {reg.value}")
