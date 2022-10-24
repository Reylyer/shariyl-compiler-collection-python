from mimetypes import init
import re

class PushBackStream:
    def __init__(self, source, raw = False) -> None:
        self.data = source if raw else open(source, 'r').read()
        self.data = list(reversed(self.data))
        self.pos = 0
        self.line = 0

    def push(self, c):
        self.data += c
        if c == '\n':
            self.line -= 1
        self.pos -= 1
    
    def pop(self) -> str: # type:ignore
        if len(self.data) == 0:
            return ""
        self.data, retval = self.data[:-1], self.data[-1]
        self.pos += 1
        if retval == '\n':
            self.line += 1
        return retval


class Identifier:
    def __init__(self, *, name, dtype, value = None) -> None:
        self.name = name
        self.dtype = dtype
        self.value = value
        self.isConstant = value == None

class Token:
    def __init__(self, ttype, val, line: int, charidx: int) -> None:
        self.ttype = ttype
        self.value = val
        self.line = line
        self.charidx = charidx

class Tokenizer:
    def __init__(self, 
                 r_str: str, 
                 reserved_keyword: list, 
                 reserved_operator: list, 
                 keyword_operator: list,
                 special: list, 
                 a_line: int, 
                 a_charidx: int) -> None:
        self.r_str = r_str
        self._reserved_keyword = reserved_keyword
        self._reserved_operator = reserved_operator
        self._keyword_operator = keyword_operator
        self._special = special
        self.a_line = a_line
        self.a_charidx = a_charidx
        self.line = 0
        self.charidx = 0
        self.tokens = []

        self.stream = PushBackStream(self.r_str, raw=True)
        self.__tokenize()

    def __fetch_word(self):
        ch = self.stream.pop()
        word = ""

        while ch.isalnum() or ch == ".":
            word += ch
            ch = self.stream.pop()
        self.stream.push(ch)
        if word:
            if word in self._reserved_keyword:
                type = "OPERATOR" if word in self._keyword_operator else "KEYWORD"
                self.tokens.append(Token(type, word, self.stream.line, self.stream.pos - len(word)))
            elif word[0].isdigit():
                try:
                    num = int(word)
                    self.tokens.append(Token("INTEGER", num, self.stream.line, self.stream.pos - len(word)))
                except ValueError:
                    try:
                        num = float(word)
                        self.tokens.append(Token("REAL", num, self.stream.line, self.stream.pos - len(word)))
                    except:
                        # syntax error illegal identifier name e.g. 1dx | 0long
                        pass
            else:
                self.tokens.append(Token("IDENTIFIER", word, self.stream.line, self.stream.pos - len(word)))

    def __fetch_operator(self):
        # badly hardcoded
        first_op = self.stream.pop()
        ssecond_op = self.stream.pop()
        if ssecond_op not in "->":
            self.stream.push(ssecond_op)
            ssecond_op = ""
        first_op += ssecond_op           

        if first_op in self._reserved_operator:
            self.tokens.append(Token("OPERATOR", first_op, self.stream.line, self.stream.pos - len(first_op)))
        elif first_op in self._special:
            self.tokens.append(Token("BRACES", first_op, self.stream.line, self.stream.pos - len(first_op)))
        else:
            # syntax error illegal no operator or just ignore completely
            pass

    def __fetch_comment(self):
        ch = self.stream.pop()
        comment = ""
        while ch != '}':
            comment += ch
            ch = self.stream.pop()
        comment += ch
        self.tokens.append(Token("COMMENT", comment, self.stream.line, self.stream.pos - len(comment)))

    def __tokenize(self):
        while True:
            c = self.stream.pop()
            if c.isalnum():
                self.stream.push(c)
                self.__fetch_word()
            elif c == ' ':
                continue
            elif c == '\n':
                self.tokens.append(Token("NEWLINE", c, self.stream.line, self.stream.pos - 1))
            elif c == '{':
                self.stream.push(c)
                self.__fetch_comment()
            elif c == '':
                break
            else:
                self.stream.push(c)
                self.__fetch_operator()




