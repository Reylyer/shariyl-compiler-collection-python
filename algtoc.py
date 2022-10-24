from structures.akamus import Kamus
from utils.fragmenter import fragment
from structures.aprogram import Program
from structures.afunction import Function
from structures.akamus import Kamus
from structures.aalgoritma import Algoritma
import sys
# sys.tracebacklimit = 0

class Runtime:
    def __init__(self) -> None:
        self._global_register = {}
        self.__entry = None
        self._load()
        self._run()

    def _load(self):
        frags = list(reversed(fragment("test.alg")))
        while len(frags):
            isProgram = False
            sect = frags.pop()
            if sect[0].startswith("program"):
                header = Program(*sect)
                isProgram = True
            else:
                raise SyntaxError

            sect = frags.pop()
            if sect[0].startswith("KAMUS"):
                kamus = Kamus(*sect)
            else:
                raise SyntaxError

            sect = frags.pop()
            if sect[0].startswith("ALGORITMA"):
                algoritma = Algoritma({**self._global_register, **kamus.register}, *sect)
                # algoritma.show_tokens()
            else:
                raise SyntaxError

            header.attach_kamus(kamus)
            header.attach_algoritma(algoritma)
            if isProgram:
                self.__entry = header
            else:
                self._global_register[header.name] = header

    def _run(self):
        if self.__entry:
            self.__entry.run()

if __name__ == "__main__":
    # t = Kamus(open("test.alg").read(), 0, 0)
    # try:
    #     t.show_tokens()
    #     t.show_register()
    # except SyntaxError as e:
    #     print(e)
    # except ValueError:
    #     pass
    a = Runtime()