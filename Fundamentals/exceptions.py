# an exception is an error inside the program.
# when this error is not "handled" the program will crash
# abruptly in a non user friendly manner.

# To deal with this, we take care of that problem by using 
# the try... except block. This block will work as follows:

# The try block contains all code that may result in an 
# error. The except block contains the response code when 
# an error happens, and it will be activated when the 
# interpreter detects the error.

# For example: When we try dividing by 0 in a computer program
# we have a classical DivisionByZero Error.
try:
    1 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# This code can be interpreted as this:
# Try to execute 1 divided by 0(which will lead to an error).
# Catch the error and right after that print out the message.

# This is useful because instead of crashing the program in a 
# weird way for a user, we can simply tell the user what happened
# with a simple massage and not with those horrific error messages.
