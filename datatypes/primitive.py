
# TODO: mungkin buat lebih rich
class PrimitiveDataTypes:
    def __init__(self, val, isConstant: bool) -> None:
        self.value = val
        self.isConstant = isConstant

    def __str__(self) -> str:
        return str(self.value)
