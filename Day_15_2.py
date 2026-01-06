from Day_15_1 import menu

print(menu)


def user_order():
    order_input = input("What would you like? (espresso/latte/cappuccino):\n")
    while order_input not in (list(menu.keys()) + ['report', 'off']):
        print("\nPlease enter espresso/latte/cappuccino.")
        order_input = input("What would you like? (espresso/latte/cappuccino):\n")

#user_order()