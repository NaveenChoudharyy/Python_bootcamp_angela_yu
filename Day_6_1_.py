# Below is the solution for Reeborg's world maze
# Go to Reborg's world website and select maze and enter this code to run
# This code will help little robot to escape the maze
# There is also a zip file in this project saved as Day_6_Reeborg_world_problems
# Unzip it and go to the Reeborgs world website and click on additional options and then click on "Open world from files"
# Then select any one of the unzipped file.
# This file contains some of the scenarios where any regular code will not work but below code will work




# Trick to solve this maze is keep walking left side of the wall, where wall be in your right.
# In special cases where there is no wall either side or front or behind, In these cases first
# we have to move forward to find the wall and then turn left




"""
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear() == True:
    move()
turn_left()
while not at_goal():
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
"""
