
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
    return num_1/num_2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

start_new_calc = True
while start_new_calc:
    n1 = input("\nEnter the number 1 : \n")

    if n1.count(".") <= 1 or n1.count("-") <= 1:

        if n1.lstrip("-").replace(".", "", 1).isdecimal():
            n1 = float(n1)

            calc_done = True
            while calc_done:

                print("\nPlease choose one of the following operations:"
                      " '+' for addition"
                      " '-' for subtraction"
                      " '*' for multiplication"
                      " '/' for division\n")
                operation_choice = input("\nEnter your choice: \n")

                if not operation_choice in operations.keys():
                    print("\nInvalid choice, You can only choose one of the following operations ('+', '-', '*', '/'):")

                else:

                    n2 = input("\nEnter the number 2 : \n")

                    if n2.count(".") <= 1 or n2.count("-") <= 1:
                        if not n2.lstrip("-").replace(".", "", 1).isdecimal():
                            print("\nInvalid input. You can only enter numbers.")
                            calc_done = False

                        elif n2.lstrip("-").replace(".", "", 1).isdecimal():
                            n2 = float(n2)

                            if n2 == 0 and operation_choice == "/":
                                print("infinity")
                                calc_done = False

                            else:

                                calc_value = operations[operation_choice](n1, n2)
                                print(f"\n {n1} {operation_choice} {n2} = {calc_value}")

                                print("\nDo you want to continue? 'y' for yes, 'n' for no or any other key to quit.")

                                more_calc = input("\nEnter your choice: \n")
                                if more_calc.lower() == "y":
                                    calc_done = True
                                    n1 = calc_value

                                elif more_calc.lower() == "n":
                                    calc_done = False

                                else:
                                    print("\nThank you for playing!")
                                    calc_done = False
                                    start_new_calc = False
                        else:
                            print("\nInvalid input. You can only enter numbers with single '.' and single '-'.")
                            calc_done = True

                    else:
                        print("Invalid input. You can only enter numbers with single '.' and single '-'.")
                        calc_done = False
                        start_new_calc = False
        else:
            print("Invalid input. You can only enter numbers with single '.' and single '-'.")
            start_new_calc = True
    else:
        print("Invalid input. You can only enter numbers with single '.' and single '-'.")
        start_new_calc = True