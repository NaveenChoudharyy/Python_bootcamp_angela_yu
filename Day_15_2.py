import pandas as pd

from Day_15_1 import menu, inventory, coins


def user_order():
    order_input = input("What would you like? (espresso/latte/cappuccino):\n")
    while order_input not in (list(menu.keys()) + ['report', 'off']):
        print("\nPlease enter espresso/latte/cappuccino.")
        order_input = input("What would you like? (espresso/latte/cappuccino):\n")
    return order_input

user_order = user_order()


def coins_input():
    while True:
        try:
            input_quarters = int(input("How many quarters: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            input_dime = int(input("How many dimes: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            input_nickels = int(input("How many nickels: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            input_pennies = int(input("How many pennies: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    return input_quarters, input_dime, input_nickels, input_pennies



def total_money(input_quarters, input_dime, input_nickels, input_pennies):
    total_money = (coins["quarter"] * input_quarters +
                   coins["dime"] * input_dime +
                   coins["nickel"] * input_nickels +
                   coins["penny"] * input_pennies)
    return total_money






if user_order == 'off':
    print("")
    print("Machine is turned off.")

elif user_order == 'report':
    print("")
    print(pd.Series(inventory))

else:
    if user_order == 'espresso':
        if (inventory["water"] > menu[user_order]["ingredients"]["water"] and
                inventory["coffee"] > menu[user_order]["ingredients"]["coffee"]):
            print("Please insert the coins: ")
            input_quarters, input_dime, input_nickels, input_pennies = coins_input()
            total_money = round(total_money(input_quarters, input_dime, input_nickels, input_pennies), 2)
            print(f"Total money inserted: {total_money}")
            print(f"Cost of {user_order}: {menu[user_order]['cost']}")
            if total_money > menu[user_order]['cost']:
                print(f"Money refunded : {round(total_money - menu[user_order]['cost'], 2)}")

            else:
                print("\nInsufficient money. please try again.")

        else:
            print("\nSorry, we don't have sufficient inventory.")

    elif user_order in ['latte', 'cappuccino']:
        if (inventory["water"] > menu[user_order]["ingredients"]["water"] and
                inventory["coffee"] > menu[user_order]["ingredients"]["coffee"] and
                inventory["milk"] > menu[user_order]["ingredients"]["milk"]):
            print("Please insert the coins: ")
            input_quarters, input_dime, input_nickels, input_pennies = coins_input()
            total_money = round(total_money(input_quarters, input_dime, input_nickels, input_pennies), 2)
            print(f"Total money inserted: {total_money}")
            print(f"Cost of {user_order}: {menu[user_order]['cost']}")
            if total_money > menu[user_order]['cost']:
                print(f"Money refunded : {round(total_money - menu[user_order]['cost'], 2)}")

            else:
                print("\nInsufficient money. please try again.")

        else:
            print("\nSorry, we don't have sufficient inventory.")






