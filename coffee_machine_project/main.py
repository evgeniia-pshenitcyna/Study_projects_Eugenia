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


def ask_money():
    """Returns total calculated amount from inserted coins"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))  # 25 cents
    dimes = int(input("How many dimes?"))  # 10 cents
    nickles = int(input("How many nickles?"))  # 5 cents
    pennies = int(input("How many pennies?"))  # 1 cent
    amount = 25 * quarters + 10 * dimes + 5 * nickles + pennies
    return amount


def deduct_resources(drink):
    """Reduces the number of resources available based on the selected drink"""
    for key in MENU:
        if key == drink:
            resources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
            resources["money"] = resources["money"] + MENU[drink]["cost"]
            if drink != "espresso":
                resources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]


def calculate_amount(drink, amount_paid):
    """Checks if user paid enough money for a drink and print if they have a drink, change or refund"""
    if drink == "latte":
        drink_price = MENU["latte"]["cost"] * 100
    elif drink == "cappuccino":
        drink_price = MENU["cappuccino"]["cost"] * 100
    else:
        drink_price = MENU["espresso"]["cost"] * 100
    if amount_paid > drink_price:
        change = round((amount_paid - drink_price) / 100, 2)
        print(f"Here is ${change} in change.")
        deduct_resources(drink)
        print(f"Here is your {drink}. Enjoy!")
        print(u'\u2615')
    elif amount_paid < drink_price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        deduct_resources(drink)
        print(f"Here is your {drink}. Enjoy!")
        print(u'\u2615')


def resource_sufficient(drink):
    for key in MENU:
        if key == drink:
            for ingredient in MENU[drink]["ingredients"]:
                missing_ingredient = 0
                if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    missing_ingredient += 1
                if missing_ingredient > 0:
                    return False
                else:
                    return True


def get_coffee():
    """Main function that keeps asking for what coffee customer wants unless it gets switched off with secret word"""
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
                if key == 'Water' or key == 'Milk':
                    print(f"{key}: {value}ml")
                elif key == 'Coffee':
                    print(f"{key}: {value}g")
                else:
                    print(f"{key}: ${value}")
        # checks if resources are sufficient:
        else:
            is_enough = resource_sufficient(drink)
            if is_enough:
                amount_paid = ask_money()
                calculate_amount(drink, amount_paid)


get_coffee()
