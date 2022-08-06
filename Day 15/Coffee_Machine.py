# Start
# Ask for which type of coffee to make
# check resources if there are enough to make that cup


# Ask for inserting coins
# 4 types of coins

# Check if coins value are enough for that cup,
# if yes, give change

# reduce the amount of resources used for that cup
# print the type of coffee cup the user have chosen

# A function to check resources
# A function to reduce resources
# A function to get coins value
# A function to calculate change

import data
# from varname import nameof


def check_resources(resources, coffee_type):
    req = (data.MENU[coffee_type])["ingredients"]
    for key in resources.keys():
        if key in req:
            if resources[key] < req[key]:
                print(f"Sorry there is not enough {key}.")
                return False
        else:
            pass
    return True


def reduce_resources(resources, coffee_type):
    req = data.MENU[coffee_type]["ingredients"]
    for key in resources.keys():
        if key in req:
            resources[key] -= req[key]
    return resources


def coins_value(quarter, dime, nickel, penny):
    coins_to_value = {
        "quarter": 0.25,
        "dime": 0.1,
        "nickel": 0.05,
        "penny": 0.01
    }
    total = 0
    for key in coins_to_value.keys():
        total += locals()[key] * coins_to_value[key]
    return total


def check_money(total, coffee_type):
    if total > data.MENU[coffee_type]['cost']:
        return True
    else:
        return False


def calculate_change(total, coffee_type):
    cost = data.MENU[coffee_type]["cost"]
    return total - cost


def ask_for_coffee_type():
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    return coffee_type




def print_not_enough_money():
    print("Sorry that's not enough money. Money refunded.")


def print_changes(change):
    if change == 0:
        print("You gave just enough money for your cup")
    else:
        print(f"Here is ${change} in change.")


def print_coffee(coffee_type):
    print(f"Here is your {coffee_type}. Enjoy!")


def make_a_coffee(resources):
    coffee_type = ask_for_coffee_type()
    # Special condition to turn off or check resources
    if coffee_type == "off":
        return
    if coffee_type == "report":
        print(resources)
        return
    # Check if there are enough resources to make a cup of coffee
    if not check_resources(resources, coffee_type):
        return
    # input coins and get their total value
    quarters, dimes, nickles, pennies = ask_for_coins()
    total = coins_value(quarters, dimes, nickles, pennies)
    # Check if the coins put in is enough for a cup of coffee
    if not check_money(total, coffee_type):
        print_not_enough_money()
        return
    # Calculate change and print
    change = calculate_change(total, coffee_type)
    print_changes(change)
    # Reduce resources and print out that coffee is made
    reduce_resources(resources, coffee_type)
    print_coffee(coffee_type)


def coffee_machine(run=True):
    resources = data.resources
    while run:
        make_a_coffee(resources)


# coffee_machine()

def ask_for_coins_varname_package():
    # I don't know why this public computer doesn't let me use console or terminal
    # that is why I haven't tested this code
    quarters, dimes, nickles, pennies = [None for _ in range(0, 4)]
    coins_type_list = [quarters, dimes, nickles, pennies]
    for coins_type in coins_type_list:
        coins_type = int(input(f"how many {varname.nameof(coins_type)}?: "))
    return quarters, dimes, nickles, pennies

def ask_for_coins_locals():
    """This function get 4 type of coins input from user and return number of each type they gave"""
    #tried to use locals() but didnt work, that's why i use globals here
    coins_type_list = ['quarters', 'dimes', 'nickles', 'pennies']
    for coins_type in coins_type_list:
        globals()[coins_type] = int(input(f"how many {coins_type}?: "))  # This line
    return quarters, dimes, nickles, pennies

def ask_for_coins_dict():
    coins_dict = {
        "quarters": None,
        "dimes": None,
        "nickles": None,
        "pennies": None
    }
    for coins_type in coins_dict.keys():
        coins_dict[coins_type] = int(input(f"how many {coins_type}?: "))
    return list(coins_dict.values())

# The three one above are all bad, can just use
def ask_for_coins_pro():
    return [int(input(f"how many {coins_type}?: ")) for coins_type in ['quarters', 'dimes', 'nickles', 'pennies']]

print(ask_for_coins_pro())