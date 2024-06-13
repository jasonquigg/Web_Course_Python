print('''     Welcome to Treasure Island.
Your Mission is to find the treasure.''')

left_right = input("Would you like to start by going left or right? ")
left_right = left_right.lower()

if left_right == "left":
    swim_wait = input("Would you like to start by swimming or to wait? ")
    swim_wait = swim_wait.lower()

    if swim_wait == "wait":
        which_door = input("Which door do you want to go through, Red, Yellow or Blue? ")
        which_door = which_door.lower()

        if which_door == "red":
            print("You walked into a room with oxygen tanks and tried to light a torch??? BOOM YOUR DEAD.. - GAME OVER!")
        if which_door == "blue":
            print("CONGRATS, You found FLUFFY... But unfortunately he was hungry, Your dead. = GAME OVER!")
        if which_door == "yellow":
            print("Well done, You win :) now fuck off.")

        else:
            print("its not hard just type red blue or yellow....")

    else:
        print("You choose to swim, but forgot u cant u idiot and drowned... Good job - GAME OVER!")

else:
    print("You went Right, Your Dead you fell into a hole and broke your neck. - GAME OVER!")
