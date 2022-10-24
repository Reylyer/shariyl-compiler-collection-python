from structures.akamus import Kamus
from structures.aalgoritma import Algoritma

class Program:
    def __init__(self, r_str: str, a_line: int, a_charidx: int) -> None:
        self.a_line = a_line
        self.a_charidx = a_charidx
        
        self.name = 'test'
        self.register = {}
        self.kamus = None
        self.algoritma = None

    def attach_kamus(self, kamus: Kamus):
        self.kamus = kamus
    
    def attach_algoritma(self, algoritma: Algoritma):
        self.algoritma = algoritma

    def run(self) -> None:
        if self.algoritma != None:
            self.algoritma()
    