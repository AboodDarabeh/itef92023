def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y

def calculator() :
    opening = "Welcome to the calculator"
    print(opening.title())


    print("""
    1- addition
    2- subtraction
    3- multiply
    4- division""")

    operation = int(input("choose the number of the operation: "))
    if operation > 4 or operation < 1 :
        print("number invalid")
        return
    num1 = int(input("enter number 1 :"))
    num2 = int(input("enter number 2 :"))


    if operation == 1 :
        print(add(num1, num2))
    elif operation == 2 :
        print(sub(num1, num2))
    elif operation == 3 :
        print(mul(num1, num2))
    elif operation == 4 :
        if num2 == 0 :
            print("you can't divide by zero")
            return
        print(div(num1, num2))

calculator()