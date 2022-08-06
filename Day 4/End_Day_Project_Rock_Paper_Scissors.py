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

all_move = [rock, paper, scissors]

user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(all_move[user_move])

print("Computer choose:")
computer_move = random.randint(0, 2)
print(all_move[computer_move])

if user_move == computer_move:
    print("Draw")
elif all_move[user_move - 1] == all_move[computer_move] :
    print("You win")
else:
    print("You lose")
