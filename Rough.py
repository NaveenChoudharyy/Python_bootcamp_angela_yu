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
print(calc_logo)


def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    return num_1 / num_2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

start_new_calc = True
while start_new_calc:
    n1 = input("\nEnter the number 1 : \n")

    # FIX 1: Use 'and'. Use lstrip('-') to check digits IGNORING the leading minus.
    # This prevents '1-2' from passing because the middle '-' won't be stripped.
    if n1.count(".") <= 1 and n1.count("-") <= 1 and n1.lstrip("-").replace(".", "", 1).isdecimal():
        n1 = float(n1)
        calc_done = True

        while calc_done:
            print("\nPlease choose one of the following operations: +, -, *, /")
            operation_choice = input("Enter your choice: \n")

            if operation_choice not in operations:
                print("\nInvalid choice.")
            else:
                n2 = input("\nEnter the number 2 : \n")

                # FIX 1: Same check for n2
                if n2.count(".") <= 1 and n2.count("-") <= 1 and n2.lstrip("-").replace(".", "", 1).isdecimal():
                    n2 = float(n2)

                    if n2 == 0 and operation_choice == "/":
                        print("Error: Cannot divide by zero.")
                        # Do not set calc_done=False, let them retry
                    else:
                        calc_value = operations[operation_choice](n1, n2)
                        print(f"\n {n1} {operation_choice} {n2} = {calc_value}")

                        print("\nType 'y' to continue, 'n' for new calc, other key to quit.")
                        more_calc = input("Enter your choice: \n")

                        if more_calc.lower() == "y":
                            n1 = calc_value
                        elif more_calc.lower() == "n":
                            calc_done = False
                        else:
                            print("\nThank you for playing!")
                            calc_done = False
                            start_new_calc = False
                else:
                    print("\nInvalid input. You can only enter numbers.")
                    # FIX 2: Do not set start_new_calc = False. 
                    # Just let the loop repeat so they can try n2 again.
    else:
        print("Invalid input. You can only enter numbers.")
        # Loop automatically restarts