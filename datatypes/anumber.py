from datatypes.primitive import PrimitiveDataTypes

# TODO: testing number

class Integer(PrimitiveDataTypes):
    def __init__(self, dInteger, isConstant: bool) -> None:
        super().__init__(dInteger, isConstant)

    @property
    def type(self):
        return "INTEGER"

    def __add__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value + int(other.value)) # type: ignore
        else:
            # raise error invalid operation
            pass
    
    def __sub__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value - int(other.value)) # type: ignore
        else:
            # raise error invalid operation
            pass
    
    def __div__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value // int(other.value)) # type: ignore
        else:
            # raise error invalid operation
            pass

    def __truediv__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value // int(other.value)) # type: ignore
        else:
            # raise error invalid operation
            pass
    
    def __mod__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value % other.value) # type: ignore
        else:
            # raise error invalid operation
            pass

    def __power__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value ** other.value) # type: ignore
        else:
            # raise error invalid operation
            pass


class Real(PrimitiveDataTypes):
    def __init__(self, dReal, isConstant: bool) -> None:
        super().__init__(dReal, isConstant)

    @property
    def type(self):
        return "REAL"

    def __add__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value + other.value) # type: ignore
        else:
            # raise error invalid operation
            pass
    
    def __sub__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value - other.value) # type: ignore
        else:
            # raise error invalid operation
            pass
    
    def __div__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value / other.value) # type: ignore
        else:
            # raise error invalid operation
            pass

    def __truediv__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value // other.value) # type: ignore
        else:
            # raise error invalid operation
            pass
    
    def __mod__(self, other):
        # raise error invalid operation
        pass

    def __power__(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value ** other.value) # type: ignore
        else:
            # raise error invalid operation
            pass