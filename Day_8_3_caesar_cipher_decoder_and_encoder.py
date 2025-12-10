# caesar cipher decoder

letter_list = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm~!@#$%^&*( )_+=-0987654321`{}|\"':;/?.><,"
letter_list = list(letter_list)
print("Welcome to the programme.\n")


# Programme to encrypt the message
def encrypt(message, key, encode_or_decode):
    new_encoded_msg = ""

    for i in message:
        shifted_position = letter_list.index(i) + int(key)
        shifted_position = shifted_position % len(letter_list)
        new_encoded_msg += letter_list[shifted_position]

    return print(new_encoded_msg)


# Programme to decrypt the message
def decrypt(message, key, encode_or_decode):
    new_decoded_msg = ""

    for i in message:
        shifted_position = letter_list.index(i) - int(key)
        shifted_position = shifted_position % len(letter_list)
        new_decoded_msg += letter_list[shifted_position]

    return print(new_decoded_msg)


loop_ends = False  # Will use this in while loop. while loop will not end till loop_ends = True

while not loop_ends:
    user_message = input("Please enter a message: \n")
    user_key = input("Please enter a key: \n")  # Key can only be a number

    if user_key.isdigit():
        user_encode_or_decode = input("Please enter encode or decode: \n")
        user_encode_or_decode = user_encode_or_decode.lower()

        if user_encode_or_decode == "encode":
            encrypt(message=user_message, key=user_key, encode_or_decode=user_encode_or_decode)
        elif user_encode_or_decode == "decode":
            decrypt(message=user_message, key=user_key, encode_or_decode=user_encode_or_decode)
        else:
            print("Please enter encode or decode: \n")

    else:
        print("'Key' can only be a number. Please try again.")

    # To continue this loop if user wants to encrypt or decrypt another message
    exit_or_continue = input(
        "\nWould you like to encrypt or decrypt another message? Type 'y' for yes and any other keyword for no.\n")
    exit_or_continue = exit_or_continue.lower()

    if exit_or_continue == "y":
        loop_ends = False  # To continue the loop
    else:
        loop_ends = True  # To end the loop
