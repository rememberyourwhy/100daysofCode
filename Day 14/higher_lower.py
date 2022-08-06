import random
import game_data
import art


def random_a_person(avoid = None):
    data_list = game_data.data
    index = random.randint(0, len(data_list) - 1)
    if data_list[index] == avoid:
        return random_a_person(avoid)
    else:
        return data_list[index]


def print_person_info(person):
    # input type(person) = dictionary
    return (f"{person['name']}, {a_or_an(person['description'])} {person['description']}, from {person['country']}")


def a_or_an(person_description):
    if person_description[0].lower() in "aioeu":
        return "an"
    else:
        return "a"

def make_a_guess(person_a, person_b):
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    guess_not = "a" if guess == "b" else "b"
    guess_to_person = {"a": person_a, "b": person_b }
    guess_person = guess_to_person[guess]
    guess_not_person = guess_to_person[guess_not]
    if guess_person['follower_count'] > guess_not_person['follower_count']:
        return True, guess_not
    else:
        return False, guess_not

def part_guess():
    point = 0
    person_a = random_a_person()
    person_b = random_a_person(person_a)
    run = True
    while run:
        print(f"Compare A: {print_person_info(person_a)}")
        print(art.vs)
        print(f"Against B: {print_person_info(person_b)}")
        result = make_a_guess(person_a, person_b)
        if result[0]:
            point += 1
            print("Your guess is right")
            print(f"Your point is {point}")
            if result[1] == "a":
                person_a = random_a_person(person_a)
            else:
                person_b = random_a_person(person_b)
        else:
            print("Your guess is wrong")
            print(f"Your final point is {point}")
            run = False


def higher_lower():
    print(art.logo)
    print("Welcome to higher lower game")
    part_guess()


higher_lower()
