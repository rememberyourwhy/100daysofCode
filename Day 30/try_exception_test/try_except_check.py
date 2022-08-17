# step 1: Try to open file
# and print a dictionary value
# Step 2: make two exception error for file not found error and key error for dictionary
# Step 3: else: --> Run this code block if there are no error occurred
# Step 4: Finally: --> Run this code block no matter what

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["adw"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:                         # run when no error
    content = file.read()
    print(content)
finally:                      # run no matter what happen
    # noinspection PyUnboundLocalVariable
    file.close()
    print("File was closed.")


# ------------------------------------ Another examples ------------------------------------ #
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")


bmi = weight / height ** 2
print(bmi)


# -------------------------------------IndexError----------------------------------- #
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


# ------------------------------------ KeyError ------------------------------------- #
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)

