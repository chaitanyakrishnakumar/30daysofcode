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

game_pics = [rock, paper, scissors]
player_choice = int(input("🗣️wanna play 🪨📄✂️? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if 0 <= player_choice <= 2:
 print(game_pics[player_choice])

computer_choice = random.randint(0,2)
print(f"computer chose: ")
print(game_pics[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("You type invalid number, you lose.")
elif player_choice == computer_choice:
    print("it's a draw")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose")
elif player_choice > computer_choice:
    print("You win!")
elif player_choice < computer_choice:
    print("You lose")
