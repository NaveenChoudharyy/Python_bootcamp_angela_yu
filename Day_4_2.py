# pick a card game
import random

friends = ["Naveen", "Ravi", "Rahul", "Himanshu atkan", "Himanshu kanda"]

# Method 1
ran_num = random.randint(0,len(friends)-1)
print(friends[ran_num])

# Method 2
print(random.choice(friends))
