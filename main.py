from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymchn = MoneyMachine()

is_on = True
while is_on:
    user_input = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffeemaker.report()
        moneymchn.report()
    else:
        order = menu.find_drink(user_input)
        if coffeemaker.is_resource_sufficient(order) and moneymchn.make_payment(order.cost):
            coffeemaker.make_coffee(order)
