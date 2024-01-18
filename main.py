import os

from art import logo_1, logo_2


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    """
    :return:
    This function is the main calculator function, it calls the math \
    operation functions.
    """

    print(logo_1)
    print(logo_2)

    num_1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation (+, -, *, /): ")
        num_2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}.\n"
                 f"Or, type 'n' to start a new calculation: ") == 'y':
            num_1 = answer
        else:
            should_continue = False
            clear()
            calculator()  # recursion


calculator()
