MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_resource():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}gm")
    print(f"Money: ${resources['money']}")


def check_resource(u_order):
    if u_order == "espresso":
        if MENU[u_order]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU[u_order]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
    elif u_order == "latte" or u_order == "cappuccino":
        if MENU[u_order]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU[u_order]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif MENU[u_order]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
    return True


def process_coins():
    print("Please insert the coins.")
    qtr = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nkl = int(input("how many nickels?: "))
    pns = int(input("how many pennies?: "))
    coin_amt = 0.25 * qtr + 0.1 * dime + 0.05 * nkl + 0.01 * pns
    return coin_amt


def check_txn(odr, coin_amt):
    if MENU[odr]["cost"] > coin_amt:
        print("Sorry that's not enough money. Money refunded.")
        return -1
    elif coin_amt >= MENU[odr]["cost"]:
        balance = coin_amt - MENU[odr]["cost"]
        resources["money"] += MENU[odr]["cost"]
        return balance


def update_resource(odr):
    if odr == "espresso":
        resources["water"] -= MENU[odr]["ingredients"]["water"]
        resources["coffee"] -= MENU[odr]["ingredients"]["coffee"]
    elif odr == "latte" or odr == "cappuccino":
        resources["water"] -= MENU[odr]["ingredients"]["water"]
        resources["milk"] -= MENU[odr]["ingredients"]["milk"]
        resources["coffee"] -= MENU[odr]["ingredients"]["coffee"]


def coffee_machine():
    turn_off = False
    while not turn_off:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "report":
            print_resource()
        elif order == "off":
            turn_off = True
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            if not check_resource(order):
                turn_off = True
            else:
                c_amt = process_coins()
                ret = check_txn(odr=order, coin_amt=c_amt)
                if ret == -1:
                    """"""
                else:
                    print(f"Here is ${round(ret,2)} in change.")
                    update_resource(order)
                    print(f"Here if your {order} ☕. Enjoy!")


coffee_machine()
