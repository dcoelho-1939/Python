def add(a, b):
    return a + b

def subtract(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    uinput = int(input("Type a first number: "))
    uinput2 = int(input("Type another number: "))
    op = input("Type the desired operation[+. -, *, /]: ")

    match op:
        case "+":
            print(add(uinput, uinput2))
        case "-":
            print(subtract(uinput, uinput2))
        case "*":
            print(multiply(uinput, uinput2))
        case "/":
            print(divide(uinput, uinput2))
        case _:
            print("Invalid input... try again.")

