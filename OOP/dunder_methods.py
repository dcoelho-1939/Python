# In python we have something called "dunder methods".
# They stand for "double underscore methods".

# These methods are special built-in methods within python, that 
# allow the programmer to customize native behaviour. For example,
# we can define a specific behaviour inside a class for the 
# operation of printing an object on the screen:

class Example:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello, my name is {self.name}."

example1 = Example("Davi")
print(example1)

# So now, everytime we print an object from the Example class, it'll have a 
# little customized message with it.

# We can also do that with a lot of other things, like operations and so on...
