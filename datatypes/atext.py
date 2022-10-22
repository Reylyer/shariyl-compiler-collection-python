from datatypes.primitive import PrimitiveDataTypes
from datatypes.aarray import ArrayDataTypes

#TODO: kelarin char ma string

class Character(PrimitiveDataTypes):
    def __init__(self, val, isConstant: bool) -> None:
        super().__init__(val, isConstant)

    @property
    def type(self):
        return "CHARACTER"

class String(ArrayDataTypes):
    def __init__(self, val) -> None:
        super().__init__()
        self.wadah = val
        self.size = len(val)
    
    @property
    def type(self):
        return "STRING"