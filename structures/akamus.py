from ast import operator
from utils.atokenizer import Identifier, Tokenizer
from utils.abuilder import *
from datatypes.aadt import AbstractDataTypes
from datatypes.aarray import ArrayDataTypes
from datatypes.aboolean import Boolean
from datatypes.alinked import LinkedDataTypes
from datatypes.anumber import Integer, Real
from datatypes.atext import Character, String

# TODO: buat gimana caranya jadi masuk registerz
class Kamus(Tokenizer):
    _datatype = [
        'integer', 
        'real', 
        'boolean', 
        'character', 
        'string', 
        'array'
    ]
    _reserved_keyword = [
        'KAMUS',
        'LOKAL',
        'constant'
        'of',
        'type',

        'function',
        'procedure',
        'use'
    ] + _datatype

    _reserved_operator = [':', '=', ',']
    _braces = ['[', ']']
    # pas ketemu keyword ini handle
    _special_trigger = {
        "function" : functionBuilder,
        "procedure": procedureBuilder,
        "type"     : typeBuilder
    }

    def __init__(self, r_str: str, a_line: int, a_charidx: int) -> None:
        super().__init__(r_str, self._reserved_keyword, self._reserved_operator, [], self._braces, a_line, a_charidx)
        self.a_line = a_line
        self.a_charidx = a_charidx
        self.register = {}
        self.__create_register()

    def __create_register(self):
        # ASUUUU REGISTER ADT GIMANA CARANYA ANJIINGGGG
        # TODO: creating register (Kamus)
        ktokens = list(reversed([t for t in self.tokens if t.ttype != "COMMENT"]))
        tok = ktokens.pop()

        # clean left over kamus / lokal
        if tok.value == "KAMUS":
            tok = ktokens.pop()
            if tok.value == "LOKAL":
                tok = ktokens.pop()
            ktokens.append(tok)
        ktokens.pop()
        

        while len(ktokens):
            try:
                isConstant = False
                lside = ktokens.pop()
                if lside.value == "CONSTANT":
                    isConstant = True
                    lside = ktokens.pop()

                if lside.ttype == "IDENTIFIER":
                    name = lside.value
                else:
                    raise ValueError
                
                op = ktokens.pop()
                if op.value != ":":
                    # raise error
                    pass

                rside = ktokens.pop()
                if rside.value in self._datatype:
                    dtype = rside.value
                    if dtype != "array":
                        val = None
                        if isConstant:
                            valc = ktokens.pop()
                            if valc.ttype == dtype:
                                val = valc.value
                            else:
                                TypeError(f"`{valc.value}` bertipe `{valc.ttype}` sementara `{lside.value}` bertipe `{rside.value}`")
                        if dtype == "integer":
                            self.register[name] = Integer(val, isConstant)
                        elif dtype == "real":
                            self.register[name] = Real(val, isConstant)
                        elif dtype == "boolean":
                            self.register[name] = Boolean(val, isConstant)
                        elif dtype == "character":
                            self.register[name] = Character(val, isConstant)
                        elif dtype == "string":
                            self.register[name] = String(val)
                    else:
                        # tipe data array
                        pass

                elif rside.value in self.register.keys():
                    if isinstance(self.register[rside.value], AbstractDataTypes):
                        pass
                    else:
                        raise TypeError(f"`{rside.value}` bukan sebuah tipe data!")
                else:
                    raise TypeError(f"`{rside.value}` tidak terdaftar")
                
                enter = ktokens.pop()
                if enter.ttype != "NEWLINE":
                    raise SyntaxError
                    
            except IndexError as e:
                raise SyntaxError(f"Something Something ga lengkap") from None
                
    
