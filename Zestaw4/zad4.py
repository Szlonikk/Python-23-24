from functools import singledispatch, singledispatchmethod
from math import ceil


@singledispatch
def divide(x, y):
    print(f"Unsupported types for division: {type(x)} and {type(y)}")

@divide.register(int)
@divide.register(float)
def _divide_numeric(x, y):
    if y != 0:
        result = x / y
        print(f"The result of dividing {x} by {y} is: {result}")
    else:
        print("Cannot divide by zero!")

@divide.register(str)
def _divide_string(x, y):
    if y in x:
        result = x.split(y)
        print(f"The result of dividing the string '{x}' by '{y}' is: {result}")
    else:
        print(f"The string '{y}' is not found in '{x}'")


divide(10, 2)

divide(5, 0)   


divide("hello world", " ")

divide(True, 3.14)  

@singledispatch
def pole (arg):
	return "Unknown overload"

@pole.register
def _(a:int, b:int):
	return a * b

@pole.register
def _(a:float, b:float):
	return ceil (a) * ceil (b)

@pole.register
def _(a:tuple):
	return int (a[0]) * int (a[1])

print (pole ("pies"))
print (pole (2, 5))
print (pole (19.1, 15.0))
print (pole (("7", "6")))