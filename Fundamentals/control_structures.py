# ifs & loops

# ---

# the if statement allows the programmer to control what gets
# executed based on a condition and what does not get executed.

# For example, if a hypothetical condition within the program 
# is false then the program will do something, and if this 
# condition is true, then the program will do another thing.

# Example:
flag = False

if flag == False:
    print("This line was executed")
    print("And this line as well")
else:
    print("The condition was true so this line was executed instead.")

# This is very useful to control things in a program and to make it 
# act dinamically.

# We also have another type of 'if' statement, where we focus on 
# one specific object and specify actions for specific values of 
# that object.

# For example, imagine that we receive an input from the user where
# this input will have three values(1, 2 and 3). Then, we can do the
# following:

user_input = 1

match user_input:
    case 1:
        print("The user input was one.")
    case 2:
        print("The user input was two.")
    case 3:
        print("The user input was three.")
    case _:
        print("The user provided invalid input.")

# This second type of 'if' statement is not that used but sometimes can
# come in handy

# ---

# Loops allow us to perform one block of code many times.

# For example, imagine we have a database with thousands of names where 
# all names are in upper case, and we need to change them to lower case.
# Instead of having to type thousands of times the same line of code, 
# we can create a loop:

for i in range(1, 1001):
    print("Name changed successfully.")

# This line of code will be executed 1000 times.

# There's also another type of loop in python:
# The while loop. This loop will be executed as long as a condition
# is true.

x = 1
while x <= 10:
    print(x)
    x += 1

# the loop above will be executed 10 times because when x > 10 then x <= 10 is False
