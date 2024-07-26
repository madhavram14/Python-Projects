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
money = 0
p = d = n = q = amt = 0

want = False
while True:
    want = input("What would you like? (espresso/latte/cappuccino/report):")
    if want == "off":
        break
    elif want == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: $ {money}")
    elif want == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            print("Please insert coins.")
            q = float(input("How many quarters?:"))
            d = float(input("How many dimes?:"))
            n = float(input("How many nickels?:"))
            p = float(input("How many pennies?:"))
            amt = 0.01 * p + n * 0.05 + d * 0.10 + q * 0.25
            if amt >= 1.50:
                print(f"Here is ${round(amt - 1.50, 2)} in change.")
                print("Here is your espresso. Enjoy!")
                resources["water"] -= 50
                resources["coffee"] -= 18
                money += 1.50
            else:
                print("Sorry that is not enough money. Money refunded.")
        else:
            if resources["water"] < 50:
                print("Sorry, there is not enough water.")
            if resources["coffee"] < 18:
                print("Sorry, there is not enough coffee.")
    elif want == "latte":
        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
            print("Please insert coins.")
            q = float(input("How many quarters?:"))
            d = float(input("How many dimes?:"))
            n = float(input("How many nickels?:"))
            p = float(input("How many pennies?:"))
            amt = 0.01 * p + n * 0.05 + d * 0.10 + q * 0.25
            if amt >= 2.50:
                print(f"Here is ${round(amt - 2.50, 2)} in change.")
                print("Here is your latte. Enjoy!")
                resources["water"] -= 200
                resources["coffee"] -= 24
                resources["milk"] -= 150
                money += 2.50
            else:
                print("Sorry that is not enough money. Money refunded.")
        else:
            if resources["water"] < 200:
                print("Sorry, there is not enough water.")
            if resources["coffee"] < 24:
                print("Sorry, there is not enough coffee.")
            if resources["milk"] < 150:
                print("Sorry, there is not enough milk.")
    elif want == "cappuccino":
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
            print("Please insert coins.")
            q = float(input("How many quarters?:"))
            d = float(input("How many dimes?:"))
            n = float(input("How many nickels?:"))
            p = float(input("How many pennies?:"))
            amt = 0.01 * p + n * 0.05 + d * 0.10 + q * 0.25
            if amt >= 3.00:
                print(f"Here is ${round(amt - 3.00, 2)} in change.")
                print("Here is your cappuccino. Enjoy!")
                resources["water"] -= 250
                resources["coffee"] -= 24
                resources["milk"] -= 100
                money += 3.00
            else:
                print("Sorry that is not enough money. Money refunded.")
        else:
            if resources["water"] < 250:
                print("Sorry, there is not enough water.")
            if resources["coffee"] < 24:
                print("Sorry, there is not enough coffee.")
            if resources["milk"] < 100:
                print("Sorry, there is not enough milk.")
