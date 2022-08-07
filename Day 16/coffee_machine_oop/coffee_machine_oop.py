from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu, coffee_maker, money_machine = Menu(), CoffeeMaker(), MoneyMachine()


def main(run=True):
    while run:
        order = input(f"Choose a drink from this list {menu.get_items()} ")
        if order == "off":
            run = False
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            item = menu.find_drink(order)  # a MenuItem object
            if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
            else:
                pass

main()
