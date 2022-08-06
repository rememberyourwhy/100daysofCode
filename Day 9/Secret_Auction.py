import os
#os.system('clear')
def add_new_bidder(name_bid):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    name_bid[name] = bid
    return name_bid

def get_highest_bid(name_bid):
    highest_bid = list(list(name_bid.items())[0])
    for key, value in name_bid.items():
        if value > highest_bid[1]:
            highest_bid = [key, value]
    return highest_bid

def secret_auction():
    name_bid = {}
    run = True
    while run:
        add_new_bidder(name_bid)
        check = input("Are there any other bidders? Type 'yes' or 'no'. \n")
        run = (lambda check : True if check == "yes" else False)(check)
        os.system('cls')
    highest_bid = get_highest_bid(name_bid)
    print(f"The winner is {highest_bid[0]} with a bid of ${highest_bid[1]}")

secret_auction()

