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


def ask_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))  # 25 cents
    dimes = int(input("How many dimes?"))  # 10 cents
    nickles = int(input("How many nickles?"))  # 5 cents
    pennies = int(input("How many pennies?"))  # 1 cent


def get_coffee():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    #creates a report
    if drink == "report":
        for k in resources:
            key = k.capitalize()
            value = resources[k]
            print(f"{key}: {value}ml")
        get_coffee()
    #checks if resources are sufficient:
    if drink == 'espresso':
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            get_coffee()
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            get_coffee()
        else:
            ask_money()
    elif drink == 'cappuccino':
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            get_coffee()
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            get_coffee()
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough coffee.")
            get_coffee()
        else:
            ask_money()
    else:
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            get_coffee()
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            get_coffee()
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough coffee.")
            get_coffee()
        else:
            ask_money()

get_coffee()

#process coins

#check if transaction is successful
change = 0
print(f"Here is ${change} in change.")
print(f"Here is your {drink}. Enjoy!")
#then restart
print("Sorry that's not enough money. Money refunded.")
#then restart