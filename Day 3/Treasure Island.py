"""This game is based on "Choose Your Own Adventure" books"""
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
first_choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")
if first_choice == "left":
    second_choice = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across ")
    if second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if third_choice == "yellow":
            print("You won the game")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")