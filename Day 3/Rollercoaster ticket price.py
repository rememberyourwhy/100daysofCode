print("Welcome to the rollercoaster")
height = int(input("What is your height? "))

#check if your customer's height is >= 120 to get the right price for their ticket

# if height >= 120:
#     print("You are high enough to buy the ticket")
#     age = int(input("Now tell us your age? "))
#     if age < 12:
#         print("You have to pay 5$ for your ticket")
#     elif age >= 12 and age < 18:
#         print("You have to pay 7$ for your ticket")
#     else:
#         print("You have to pay 12$ for your ticket")
#
# else:
#     print("You are not high enough to buy ticket for the rollercoaster")

#use dictionary:
def age_to_price(age):
    age_to_price_dict = {"0 - 12": 5 ,
                        "12 - 18": 7 ,
                        "18 - 1024": 12}
    for key in age_to_price_dict:
        for index in range(len(key)):
            if key[index] == "-":
                start_age = int(key[:index])
                end_age = int(key[index + 1:])
        if age > start_age and age <= end_age:
            return age_to_price_dict[key]
if height >= 120:
    print("You are high enough to buy the ticket")
    age = int(input("Now tell us your age "))
    bill = age_to_price(age)
    if int(input("Do you want to give extra 3$ for a photo ")) == 0:
        print(f"So you dont want, you have to pay {bill}$")
    else:
        print(f"So you want a photo taken, you have to pay {bill + 3}$ in total")
else:
    print("You are not high enough to buy the ticket")


