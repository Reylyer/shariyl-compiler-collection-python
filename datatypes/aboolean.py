from datatypes.primitive import PrimitiveDataTypes

# TODO: Kelarin Boolean
class Boolean(PrimitiveDataTypes):
    def __init__(self, val, isConstant: bool) -> None:
        super().__init__(val, isConstant)
