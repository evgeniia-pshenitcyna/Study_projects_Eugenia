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
}


# TODO: 1. process coins
# TODO: 2. check if transaction is successful
def ask_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))  # 25 cents
    dimes = int(input("How many dimes?"))  # 10 cents
    nickles = int(input("How many nickles?"))  # 5 cents
    pennies = int(input("How many pennies?"))  # 1 cent
    amount = 25 * quarters + 10 * dimes + 5 * nickles + pennies
    return amount

# change = 0
# print(f"Here is ${change} in change.")
# print(f"Here is your {drink}. Enjoy!")
# then restart
# print("Sorry that's not enough money. Money refunded.")
# then restart

def get_coffee():
    machine_active = True
    while machine_active:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        # switches machine off:
        if drink == 'off':
            machine_active = False
        # creates a report
        elif drink == "report":
            for k in resources:
                key = k.capitalize()
                value = resources[k]
                print(f"{key}: {value}ml")
        # checks if resources are sufficient:
        elif drink == 'espresso':
            if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
            elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            else:
                amount_paid = ask_money()
                drink_price = MENU["espresso"]["cost"]*100
                if amount_paid > drink_price:
                    change = round((amount_paid - drink_price)*100, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {drink}. Enjoy!")
                elif amount_paid < drink_price:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    print(f"Here is your {drink}. Enjoy!")
        elif drink == 'cappuccino':
            if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
            elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Sorry there is not enough coffee.")
            else:
                amount_paid = ask_money()
                drink_price = MENU["cappuccino"]["cost"] * 100
                if amount_paid > drink_price:
                    change = round((amount_paid - drink_price) * 100, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {drink}. Enjoy!")
                elif amount_paid < drink_price:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    print(f"Here is your {drink}. Enjoy!")
        else:
            if resources["water"] < MENU["latte"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
            elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
                print("Sorry there is not enough coffee.")
            else:
                amount_paid = ask_money()
                drink_price = MENU["cappuccino"]["cost"] * 100
                if amount_paid > drink_price:
                    change = round((amount_paid - drink_price) * 100, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {drink}. Enjoy!")
                elif amount_paid < drink_price:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    print(f"Here is your {drink}. Enjoy!")


get_coffee()
