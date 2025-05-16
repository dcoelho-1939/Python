# A function is one of the most useful objects within programming
# because they allow for creation of independent programs within a
# program that perform certain operations

# For example, let's say we have a program that will behave like a 
# calculator. One function can perform the calculation of the addition
# operation, and another function can perform the calculation of the 
# subtraction operation and so on. This is useful because it transforms
# the code into separate parts, making it more readable, understandable
# and easy to follow(since each function will have it's own logic).

# Example of a function:
def example(a, b):
    return a + b

# The example() function performs only one operation: add two numbers
# together. We can have functions to perform all sorts of operations.

# --- 

# Functions have interesting behaviour: Any variable declared inside 
# a function will exist only inside that functions and nowhere else.
# This behaviour is good because, again, allow the programmer the 
# possibility to create 'independent mini-programs' as functions, 
# without each function interfering with the program's namespace.

# Example:
x = 1
def scopeExample():
    x = 1
    x += 1
    print("The value of x is: " + str(x))

scopeExample()
print("The value of x is: " + str(x))

# The code above will show us that the x within the function is 2
# and the x outside the function is 1. Even though they both have 
# the same identifier, they are completely different variables and 
# objects. One belongs to the function and the other belongs to the 
# program globally. This happens because of the concept of scopes:
# Everything inside a block of code belongs to that block of code 
# and only that. Unless it's a variable declared outside a block of 
# code, which in this case the variable is considered global(belongs 
# to the whole program and can be accessed anywhere within it).


