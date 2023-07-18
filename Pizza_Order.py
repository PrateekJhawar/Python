# Define the pizza menu
menu = {
    "Margherita": 150,
    "Pepperoni": 180,
    "Vegetarian": 190,
    "Hawaiian": 130,
    "Meat Lovers": 200
}

# Define the topping menu
toppings = {
    "Mushrooms": 20,
    "Olives": 20,
    "Onions": 15,
    "Peppers": 25,
    "Extra Cheese": 20,
    "Bacon": 20,
    "Sausage": 15,
    "Ham": 30
}

# Define a function to display the menu
def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item} - Rs {price}")

# Define a function to take the order
def take_order(menu, toppings):
    order = {}
    while True:
        display_menu(menu)
        item = input("What would you like to order? ")
        if item not in menu:
            print("Sorry, that item is not on the menu.")
            continue
        else:
            order[item] = menu[item]
        while True:
            display_menu(toppings)
            topping = input("Would you like to add a topping? (y/n) ")
            if topping.lower() == "n":
                break
            elif topping.lower() == "y":
                topping_choice = input("Which topping would you like to add? ")
                if topping_choice not in toppings:
                    print("Sorry, that topping is not available.")
                    continue
                else:
                    order[topping_choice] = toppings[topping_choice]
            else:
                print("Please enter 'y' or 'n'.")
        more = input("Would you like to order anything else? (y/n) ")
        if more.lower() == "n":
            break
    return order

# Define a function to calculate the total cost of the order
def calculate_total(order):
    total = sum(order.values())
    return total

# Define a function to take the user's details
def get_user_details():
    name = input("What is your name? ")
    phone = input("What is your phone number? ")
    address = input("What is your address? ")
    return {"name": name, "phone": phone, "address": address}

# Define the main function to run the pizza ordering system
def main():
    print("Welcome to our pizza ordering system!")
    print("------------------------------------")
    order = take_order(menu, toppings)
    total = calculate_total(order)
    user_details = get_user_details()
    print("------------------------------------")
    print("Your order:")
    for item, price in order.items():
        print(f"{item} - Rs {price}")
    print(f"Total: Rs {total}")
    print("------------------------------------")
    print("Your details:")
    print(f"Name: {user_details['name']}")
    print(f"Phone: {user_details['phone']}")
    print(f"Address: {user_details['address']}")
    print("------------------------------------")
    print("Thank you for ordering!")

# Run the main function
main()
