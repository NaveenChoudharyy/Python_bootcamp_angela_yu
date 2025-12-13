# Code for a working calculator
# I have used recursion (def inside same def)

calc_logo = """

      Calculator
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""




def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1/num_2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def enter_num_1():
    while True:
        try:
            n1 = float(input("\nEnter a number: \n"))
            return n1
        except ValueError:
            print("Invalid input. You can only enter numbers.\n")


def select_operation():
    while True:
        operation_selected = input("\nPlease select one of the following operations: '+', '-', '*', '/'\n")
        if operation_selected in operations.keys():
            return operation_selected
        else:
            print("Invalid input. You can only select from one of the following operations: '+', '-', '*', '/'\n")

def enter_num_2():
    while True:
        try:
            n2 = float(input("\nEnter a number: \n"))
            return n2
        except ValueError:
            print("Invalid input. You can only enter numbers.\n")

def first_calc():
    n1 = enter_num_1()
    oper = select_operation()
    n2 = enter_num_2()
    n3 = 0

    if oper == "/" and n2 == 0:
        print("Infinity! Division by zero")
        return None

    else:
        n3 += operations[oper](n1, n2)
        print(f"{n1} {oper} {n2} = {n3}")
        return n3

def next_calc(previous_result):
    oper_next = select_operation()
    n2_next = enter_num_2()
    n3 = 0

    if oper_next == "/" and n2_next == 0:
        print("Infinity! Division by zero")
        return None

    n3 += operations[oper_next](previous_result, n2_next)
    print(f"{previous_result} {oper_next} {n2_next} = {n3}")
    return n3


def calculator():
    print(calc_logo)
    prev_result = first_calc()
    while True:

        if prev_result is None:
            print("Error encountered. Resetting calculator.\n")
            prev_result = first_calc()
            continue

        cont_or_not = input(
            f"\n Type 'y' to continue with previous answer '{prev_result}' or 'n' for new calculation and any other key to quit.\n").lower()
        if cont_or_not.lower() == "y":
            prev_result = next_calc(prev_result)
        elif cont_or_not.lower() == "n":
            print("\nResetting calculator.\n")
            calculator() # Recursion
        else:
            print("Thank you for visiting.")
            break