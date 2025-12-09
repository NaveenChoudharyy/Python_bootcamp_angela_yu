# Caeser Ciphar

list_1 = "abcdefghijklmnopqrstuvwxyz123456789 0.,"
list_2 = "5 m,lp6k1onjibh4uv0gy8cft3xdresz7a.w2q9"


def encode(input_string):

    encoded_string = ""

    for i in input_string:
        for j, k in enumerate(list_1):
            if i == k:
                encoded_string += list_2[j]

    return encoded_string


def decode(input_string):

    decoded_string = ""

    for i in input_string:
        for j, k in enumerate(list_2):
            if i == k:
                decoded_string += list_1[j]

    return decoded_string


print("Hello Buddy")

input_string = input("What is your massage :\n")
input_string = input_string.lower()

encoding = input("Do you want to encode or decode:\n")
encoding = encoding.lower()

loop_ends = False


if encoding == "encode":
    output = encode(input_string)

elif encoding == "decode":
    output = decode(input_string)

else:
    print("Looks like you are enemy trying to learn this system. Good luck.")



if encoding not in ["encode", "decode"]:
    loop_ends = True
else:
    pin = input("please enter your pin:\n")

    if not pin.isdigit():
        print("Please enter a number.")
        loop_ends = True

    else:

        pin = int(pin)
        pin = pin % len(output)

        if encoding == "encode":
            output = output[pin:] + output[:pin]
            print(output)

        elif encoding == "decode":
            output = output[-pin:] + output[:-pin]
            print(output)

        else:
            print("You can only enter a number.")
