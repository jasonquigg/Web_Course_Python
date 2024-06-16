import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Image Stuffies
game_images = [rock, paper, scissors]

# Gets players Choice
player_choice = int(input("Please choose 0 for Rock, 1 for Paper or 2 for Scissors: \nPlayer Choice = "))

# Checks if players choice is valid and prints picture / continues code if it is.
if player_choice > 2 or player_choice < 0:
    print("You typed an invalid number, You LOOSE!")
else:
    print(game_images[player_choice])

    # Gets Computer Choice
    computer_choice = random.randint(0, 2)
    print(f"Computer Choose: {computer_choice}")
    print(game_images[computer_choice])

    # Logic for who wins
    if player_choice == 0 and computer_choice == 2:
        print("You WIN!")
    elif computer_choice == 0 and player_choice == 2:
        print("You LOOSE!")
    elif computer_choice > player_choice:
        print("You LOOSE!")
    elif player_choice > computer_choice:
        print("You WIN!")
    elif computer_choice == player_choice:
        print("You DRAW!")
