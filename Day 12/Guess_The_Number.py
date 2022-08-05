# First start the game
# Ask user to choose level of difficulty
# Start the game
# Give them guesses
# When they do a guess, tell them if its high or low

# Function:
# Make a Guess
    # get input from user
    # check guess
        # reduce their number of guesses
        # return if they got the right number
    # give output
# level of difficulty

# Main function
    # start the game
    # get input for level of difficulty
    # run guess function

import random


def get_random_number():
    return random.randint(0, 100)


def level_of_difficulty():
    level = input("Do you want to play in \"easy\" or \"hard\" mode? ")
    return "easy" if level == "easy" else "hard"


def guess(level, num_right):
    level_dict = {"easy": 10, "hard": 5}
    number_of_guesses = level_dict[level]
    while number_of_guesses > 0:
        num_guess = int(input("Make a guess "))
        temp_result, number_of_guesses, comment = check_guess(num_guess, num_right, number_of_guesses)
        if temp_result: # win condition
            print(f"Your guess is {comment}")
            print(f"You got it right after {level_dict[level] - number_of_guesses} guess(es)")
            return
        else:
            # print(f"Your guess is {temp_result}")
            print(f"Its {comment}")
            print(f"You have {number_of_guesses} guess(es) left")
    # lose condition
    print("Game over")
    print(f"The number is {num_right}")


def check_guess(num_guess, num_right, number_of_guesses):
    if num_guess == num_right:
        return [True, number_of_guesses, "right"]
    else:
        return [False, number_of_guesses - 1, "too high"] if num_guess > num_right else [False, number_of_guesses - 1, "too low"]


def main_game():
    level = level_of_difficulty()
    num_right = get_random_number()
    guess(level, num_right)

main_game()
