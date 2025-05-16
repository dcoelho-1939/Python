def add(a, b):
    return a + b

def subtract(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b 
    except ZeroDivisionError:
        print("Error: Division by zero.")

while True:
    print("\nType 'quit' at any time to quit")

    uinput = input("Type a first number: ")
    if not uinput.isnumeric():
        break

    uinput2 = input("Type another number: ")
    if not uinput2.isnumeric() :
        break

    op = input("Type the desired operation[+. -, *, /]: ")
    if op == 'quit':
        break

    uinput = int(uinput)
    uinput2 = int(uinput2)

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

