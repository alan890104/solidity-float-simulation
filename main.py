# Simulation solidity float operation
from typing import Union

class Float:
    precision: int = 64

    def __new__(cls,  v: int) -> "Float":
        """
        input value is int, but it is float representation
        """
        if isinstance(v,int):
            return super().__new__(cls)
        else:
            raise TypeError("value must be int (float representation already)")

    def __init__(self, v:int) -> None:
        self.value =v

    @classmethod
    def from_number(cls: "Float", x: Union[float, int, str]) -> "Float":
        x = int(float(x) * 2 ** cls.precision)
        return Float(x)

    def __add__(self, other: "Float") -> "Float":
        return Float((self.value + other.value))
    
    def __sub__(self, other: "Float") -> "Float":
        return Float((self.value - other.value) )
    
    def __mul__(self, other: "Float") -> "Float":
        return Float((self.value * other.value) >> self.precision)
    
    def __truediv__(self, other: "Float") -> "Float":
        return Float(((self.value << self.precision) // other.value))

    def __str__(self) -> str:
        return str(self.value / 2**self.precision)
    
if __name__ == "__main__":
    x = 0.25
    y = 10
    print("=====================================")
    print("x =", x)
    print("y =", y)
    print("=====================================")
    print("Human readable value:")
    a, b = Float.from_number(x), Float.from_number(y)
    print("a + b =", (a + b))
    print("a - b =", (a - b))
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("=====================================")
    print(f"Actual stroing value (multiplies 2^{a.precision}):")
    print("a + b =", (a + b).value)
    print("a - b =", (a - b).value)
    print("a * b =", (a * b).value)
    print("a / b =", (a / b).value)






