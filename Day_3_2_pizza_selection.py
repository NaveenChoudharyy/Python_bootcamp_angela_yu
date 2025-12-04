size = input("What size pizza do you want? s, m or l: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Dou you want extra cheese on your pizza? y or n: ")
bill = 0
if (size.lower() == "s" or size.lower() == "m" or
    size.lower() == "l") and (pepperoni.lower() == "y" or
                              pepperoni.lower() == "n") and (extra_cheese.lower() == "y" or
                                                             extra_cheese.lower() == "n"):
    if size.lower() == "s":
        bill += 15
        if pepperoni.lower() == "y":
            bill += 2
    elif size.lower() == "m":
        bill += 20
        if pepperoni.lower() == "y":
            bill += 3
    elif size.lower() == "l":
        bill += 25
        if pepperoni.lower() == "y":
            bill += 3
    if extra_cheese.lower() == "y":
        bill += 1
        print(f"Your bill amount is ${bill}")
    else:
        print(f"Your bill amount is ${bill}")
else:
    print("Please enter a valid input. Try again.")

