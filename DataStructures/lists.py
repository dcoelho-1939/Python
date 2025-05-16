# Lists are ways of storing more than one information in one single variable.
# It behaves literally like a normal list in real life.

# List items are ordered, changeable and can be duplicates.
# The ordered part comes from indexes:
example = ["Davi", "Nayara", "Liara"]
print(example[0]) # -> Davi 
print(example[1]) # -> Nayara
print(example[2]) # -> Liara

# changeable:
example[0] = "David"
print(example)

# duplicates:
example.append("Liara")
print(example)

# Lists come from arrays. The difference is that with lists are dynamic
# arrays, where it can increase in size or decrease with the execution of the 
# program, as well as contain different data types.

# We can perform all sorts of operations with a list, such as 
# loop through it, list comprehensions, and a bunch of methods and properties.


