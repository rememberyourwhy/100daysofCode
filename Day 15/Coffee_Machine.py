#Start
#Ask for which type of coffee to make
#check resources if there are enough to make that cup


#Ask for inserting coins
# 4 types of coins

#Check if coins value are enough for that cup,
# if yes, give change

#reduce the amount of resources used for that cup
#print the type of coffee cup the user have chosen

#A function to check resources
#A function to reduce resources
#A function to get coins value
#A function to calculate change

import data

def check_resources(resources, coffee_type):
    req = (data.MENU[coffee_type])["ingredients"]
    for key in resources.keys():
        if resources[key] < req[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def reduce_resources(resources, coffee_type):
    req = data.MENU[coffee_type]["ingredients"]
    for key in resources.keys():
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
    if total > data.MENU[coffee_type][cost]:
        return True
    else:
        return False

def calculate_change(total, coffee_type):
    cost = data.MENU[coffee_type]["cost"]
    return total - cost


def ask_for_coffee_type():
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    return coffee_type


def ask_for_coins():
    coins_type_list = ['quarters', 'dimes', 'nickles', 'pennies']
    for type in coins_type_list:
        globals()[type] = int(input(f"how many {type}?: "))
    return quarters, dimes, nickles, pennies

def print_not_enough_money():
    print("Sorry that's not enough money. Money refunded.")
def print_changes(change):
    if change == 0:
        print("You gave just enough money for your cup")
    else:
        print(f"Here is ${change} in change.")


def print_coffee(coffee_type):
    print(f"Here is your {coffee_type}. Enjoy!")

def coffee_machine():
    resources = data.resources
    coffee_type = ask_for_coffee_type()
    if not check_resources(resources, coffee_type):
        return
    quarters, dimes, nickles, pennies = ask_for_coins()
    total = coins_value(quarters, dimes, nickles, pennies)
    if not check_money(total, coffee_type):
        print_not_enough_money()
        return
    change = calculate_change(total, coffee_type)
    print_changes(change)
    reduce_resources(resources, coffee_type)
    print_coffee(coffee_type)

coffee_machine()
    
        
