# def greet(name):
#     print("Hi")
#     print("Guys")
#     print(f"{name}")
#
#
# greet("naveen")

# def userid(username, dob):
#     print(f"Your userid is {username}_{dob}")
#
# print(userid(dob ="Naveen",username= "10051997"))

def calculate_love_score(partner_1, partner_2):
    # for TRUE

    name = partner_1 + partner_2
    name = name.strip().lower()
    name = list(name)

    true = list("true")
    love = list("love")

    true_word = {"t": 0, "r": 0, "u": 0, "e": 0}
    love_word = {"l": 0, "o": 0, "v": 0, "e": 0}

    for i in true:
        for j in name:
            if i == j:
                true_word[i] += 1


    for i in love:
        for j in name:
            if i == j:
                love_word[i] += 1


    return print(f"Love Score = {str(sum(true_word.values())) + str(sum(love_word.values()))}")

# calculate_love_score("naveen", "choudhary")
