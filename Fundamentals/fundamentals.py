# Fundamentals: Syntax, variables and data types

# --- 

# In python, white spaces really matters:
if 5 > 1:
    print("This is indented.")

# they define blocks of code just like curly brackets({}) do


# ---


# The python interpreter actually automatically detects which data type
# the variable is, without the need for explicit declaration of types:
x = 1
y = "Davi"
z = True

# With every example above, the data type was never declared. This is 
# perfectly fine in python 


# We can also perform casting with each data type just as any other P.L.:
x = str(x)
print(type(x)) # -> now x is type string not int

# We can also get the type of a variable with the built-in function 'type()':
print(type(y)) # -> return 'str' which means a string 

# We can also perform complex declarations of variables:
# to perform this, the number of variables must be equivalent to the number of
# values.
a, b = "Hello", "World"
print(a) # -> Hello
print(b) # -> World

# Or even:
i = j = k = "All equal"
print(i)
print(j)
print(k)

# There's also a type of unpacking of values:
names = ["Davi", "Nayara", "Liara"]
f, g, h = names 
print(f) # -> Davi
print(g) # -> Nayara
print(h) # -> Liara

# All of these declaration types are useful for building code faster and more 
# efficiently


# ---


# Data types:

# Text => str(string)
# Numeric => int(integer), float(decimal numbers), complex(complex numbers)
# Sequence types => list, tuple, range
# Mapping types => dict
# Set types => set, frozenset
# Boolean => bool 
# Binary types => bytes, bytearray, memoryview
# NoneType => NoneType

# You can get the type of an object with the built-in function type():
x = "A string"
print(type(x)) # -> str
x = 1
print(type(x)) # -> int
x = 3.14
print(type(x)) # -> float
x = 1j 
print(type(x)) # -> complex
x = [1, 2, 3]
print(type(x)) # -> list
x = (1, 2, 3)
print(type(x)) # -> tuple
x = range(1, 11)
print(type(x)) # -> range
x = {"name": "Davi"}
print(type(x)) # -> dict
x = {"Davi", "Nayara", "Liara"}
print(type(x)) # -> set
x = frozenset({"Davi", "Nayara", "Liara"})
print(type(x)) # -> frozenset
x = True
print(type(x)) # -> bool 
x = b"Hello"
print(type(x)) # -> bytes
x = bytearray(5)
print(type(x)) # -> bytearray
x = memoryview(bytes(5))
print(type(x)) # -> memoryview
x = None
print(type(x)) # -> NoneType

# For each data type you have a built-in function that cast one type to the other
# if the opearation is possible!
