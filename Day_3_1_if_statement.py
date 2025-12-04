# If else statement

height_input = input("Please enter your height in cm : ")
if height_input.isdigit():
    height = int(float(height_input))
    bill = 0
    if height >= 100:
        age_input = input("Please enter your age : ")
        if age_input.isdigit():
            age = int(float(age_input))
            if age >= 21:
                bill += 15
                print("Adult ticket is $15")
            elif age >= 18:
                bill += 10
                print("Youth ticket is $10")
            elif age >= 12:
                bill += 5
                print("Child ticket is $5")
            if bill > 0:
                wants_photo = input("Would you like to have a photo? (Y/N) : ")
                if wants_photo == 'Y':
                    bill += 10
                    print(f"Your bill will be ${bill}")
                else:
                    print(f"Your bill will be ${bill}")
            else:
                print("Sorry you have to grow older before you ride. Thank you!")
        else:
            print("Please enter a valid input. Try again.")
    else:
        print("Sorry you have to grow taller before you ride. Thank you!")
else:
    print("Please enter a valid input. Try again.")