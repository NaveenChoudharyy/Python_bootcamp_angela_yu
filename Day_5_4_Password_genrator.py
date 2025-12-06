# Password Generator


"""
Learnings:
1. output += output is slower than appending the list
2. Don't use int(input())
3. random.shuffle(anything) gives none as output so don't store this in any variable instead just print(anything)
"""




"""---------------------------------------------------MY answer---------------------------------------------------"""




import random

alphabets = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789") # As the numbers is double-quoted commas these will be treated as string
symbols = list("!@#$%^&*")

input_num_of_alphabet = input("How many alphabets you want in your password : \n")
input_num_of_numbers = input("How many numbers you want in your password : \n")
input_num_of_symbols = input("How many symbols you want in your password : \n")



if input_num_of_alphabet.isdigit() and input_num_of_numbers.isdigit() and input_num_of_symbols.isdigit():

    output = ""
    input_num_of_alphabet = int(input_num_of_alphabet)
    input_num_of_numbers = int(input_num_of_numbers)
    input_num_of_symbols = int(input_num_of_symbols)

    for i in range(0, input_num_of_alphabet):
        output += random.choice(alphabets)
    for j in range(0, input_num_of_numbers):
        output += random.choice(numbers)
    for k in range(0, input_num_of_symbols):
        output += random.choice(symbols)

    output = list(output)
    random.shuffle(output)
    output = ''.join(output)
    print(output)
else:
    print("Please enter a valid input. Input should be a number. Try again.")






'''---------------------------------------------------GPT answer---------------------------------------------------'''






import random

alphabets = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789") # As the numbers is double-quoted commas these will be treated as string
symbols = list("!@#$%^&*")

input_num_of_alphabet = input("How many alphabets you want in your password : ")
input_num_of_numbers = input("How many numbers you want in your password : ")
input_num_of_symbols = input("How many symbols you want in your password : ")

if input_num_of_alphabet.isdigit() == True and input_num_of_numbers.isdigit() == True and input_num_of_symbols.isdigit() == True:

    output = []
    input_num_of_alphabet = int(input_num_of_alphabet)
    input_num_of_numbers = int(input_num_of_numbers)
    input_num_of_symbols = int(input_num_of_symbols)

    alphabets = random.choices(alphabets,k=input_num_of_alphabet)
    numbers = random.choices(numbers, k=input_num_of_numbers)
    symbols = random.choices(symbols, k=input_num_of_symbols)

    output.extend(alphabets)
    output.extend(numbers)
    output.extend(symbols)
    random.shuffle(output)
    output = ''.join(output)
    print(output)

else:
    print("Please enter a valid input. Input should be a number. Try again.")