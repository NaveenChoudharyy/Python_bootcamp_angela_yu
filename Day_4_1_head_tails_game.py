# Heads-Tails game
# If you choose same as computer you win else you loose.


choose_heads_or_tails = input("Choose heads or tails: ").lower()
if choose_heads_or_tails == "heads" or choose_heads_or_tails == "tails":
    import random

    ran_num = random.randint(1, 2)
    if ran_num == 1 :
        print("Heads")
    else:
        print("Tails")

    if choose_heads_or_tails == "heads" and ran_num == 1:
        print("You win")
    elif choose_heads_or_tails == "tails" and ran_num == 2:
        print("You win")
    else:
        print("You lose")

else:
    print("Please enter heads or tails. Try again.")