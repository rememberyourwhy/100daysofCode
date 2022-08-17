#Password Generator Project
import random

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


def randomize_list(n):
    normal_range_list = [x for x in range(0, n)]
    max_range = len(normal_range_list)
    result_list = []
    for i in range(max_range):
        pop_element_index = random.randint(0,100) % len(normal_range_list)
        randlist_new_element = normal_range_list.pop(pop_element_index)
        result_list.append(randlist_new_element)
    return result_list


def password_order_randomizing(password_before, randomize_list):
    password_after = []
    for i in range(len(randomize_list)):
        new_element = password_before[randomize_list[i]]
        password_after.append(new_element)
    return password_after


def random_easy(nr_letters, nr_symbols, nr_numbers):
    result_list = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    input_list = [nr_letters, nr_symbols, nr_numbers]
    storage_list = [letters, numbers, symbols]
    for input_index in range(len(input_list)):
        for i in range(input_list[input_index]):
            new_element_index = random.randint(0, len(storage_list[input_index])- 1)
            new_element = storage_list[input_index][new_element_index]
            result_list.append(new_element)
    return result_list


def random_hard(password_easy):
    random_order_list = randomize_list(len(password_easy))
    result_list = password_order_randomizing(password_easy, random_order_list)
    return result_list

password_easy = random_easy(2, 2, 4)
password_hard = random_hard(password_easy)
