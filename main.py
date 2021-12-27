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


def get_menu_choice(available_resources, money_collected):
    menu_values = list(MENU)
    choices = ('/'.join(menu_values))
    choice = input(f"What would you like? ({choices}): ")
    if choice in menu_values:
        return choice          # the choice is a dictionary key for MENU
    elif choice == "off":
        exit()
    elif choice == "report":
        print(f"Water: {available_resources['water']}ml")
        print(f"Milk: {available_resources['milk']}ml")
        print(f"Coffee: {available_resources['coffee']}g")
        print(f"Money: ${money_collected}")
    else:
        print("Invalid selection. Try again.")
        return "invalid"


def deposit_money():
    print("Please insert coins.")
    money = int(input("how many quarters?: ")) * 0.25
    money += int(input("how many dimes?: ")) * 0.10
    money += int(input("how many nickles?: ")) * 0.05
    money += int(input("how many pennies?: ")) * 0.01
    return money


def customer_menu(available_resources, money_collected):
    selection = None
    while selection == "invalid" or selection is None:
        selection = get_menu_choice(available_resources, money_collected)
    return selection


def check_ingredients(available_resources, ingredients):
    # print(available_resources)
    for each_item in ingredients:
        if available_resources[each_item] < ingredients[each_item]:
            print(f"There is not enough {each_item}.")
            return False
    ''' the above lines do the same thing as the older version lines
    try:
        if available_resources['water'] < ingredients['water']:
            print("There is not enough water.")
            return False
    except KeyError:
        ignore = True
    try:
        if available_resources['milk'] < ingredients['milk']:
            print("There is not enough milk.")
            return False
    except KeyError:
        ignore = True
    try:
        if available_resources['coffee'] < ingredients['coffee']:
            print("There is not enough coffee.")
            return False
    except KeyError:
        ignore = True
    '''
    return True


def deduct_ingredients(available_resources, ingredients):
    for each_item in ingredients:
        available_resources[each_item] -= ingredients[each_item]
    ''' the above lines do the same thing as the older version lines   
    try:
        available_resources['water'] -= ingredients['water']
    except KeyError:
        ignore = True
    try:
        available_resources['milk'] -= ingredients['milk']
    except KeyError:
        ignore = True
    try:
        available_resources['coffee'] -= ingredients['coffee']
    except KeyError:
        ignore = True
    # print(available_resources)
    '''
    return available_resources


def main(machine_resources, money_collected):
    money_collected = float(money_collected)
    while True:
        customer_choice = customer_menu(machine_resources, money_collected)
        enough_resources_available = check_ingredients(machine_resources, MENU[customer_choice]['ingredients'])
        if not enough_resources_available:
            main(machine_resources, money_collected)
        collected_money = deposit_money()
        if collected_money >= MENU[customer_choice]['cost']:
            print(f"Here is ${round(collected_money - MENU[customer_choice]['cost'], 2)} in change.")
            machine_resources = deduct_ingredients(machine_resources, MENU[customer_choice]['ingredients'])
            money_collected += MENU[customer_choice]['cost']
            print(f"Here is your {customer_choice} ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")


main(resources, 0)
