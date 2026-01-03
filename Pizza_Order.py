# ----------------- Data -----------------

menu = {
    "Margherita": 150,
    "Pepperoni": 180,
    "Vegetarian": 190,
    "Paneer Tikka": 130,
    "Meat Lovers": 200
}

toppings_menu = {
    "Mushrooms": 20,
    "Olives": 20,
    "Onions": 15,
    "Peppers": 25,
    "Extra Cheese": 20,
    "Bacon": 20,
    "Sausage": 15,
    "Ham": 30
}

# ----------------- Helper Functions -----------------

def display_menu(title, items):
    print(f"\n{title}:")
    for item, price in items.items():
        print(f"  {item} - Rs {price}")


def get_choice(prompt, valid_options):
    """For yes/no or fixed options."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print("Invalid input. Try again.")


# ----------------- Core Functions -----------------

def take_pizza_order():
    order = []

    while True:
        display_menu("Pizza Menu", menu)
        pizza = input("\nEnter pizza name: ").strip()

        if pizza not in menu:
            print("Pizza not found. Try again.")
            continue

        # Store pizza + toppings
        pizza_entry = {
            "pizza": pizza,
            "base_price": menu[pizza],
            "toppings": []
        }

        # Add toppings
        add_toppings = get_choice("Add toppings? (y/n): ", ["y", "n"])
        if add_toppings == "y":
            while True:
                display_menu("Toppings Menu", toppings_menu)
                topping = input("Choose a topping: ").strip()

                if topping not in toppings_menu:
                    print("Topping not available.")
                    continue

                pizza_entry["toppings"].append(topping)

                more = get_choice("Add another topping? (y/n): ", ["y", "n"])
                if more == "n":
                    break

        order.append(pizza_entry)

        # More pizzas?
        more_pizza = get_choice("Order another pizza? (y/n): ", ["y", "n"])
        if more_pizza == "n":
            break

    return order


def calculate_total(order):
    total = 0
    for item in order:
        total += item["base_price"]
        for topping in item["toppings"]:
            total += toppings_menu[topping]
    return total


def get_user_details():
    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()
    address = input("Enter your address: ").strip()
    return {"name": name, "phone": phone, "address": address}


# ----------------- Main -----------------

def main():
    print("Welcome to the Pizza Ordering System")
    print("------------------------------------")

    order = take_pizza_order()
    total = calculate_total(order)
    user = get_user_details()

    print("\n------------ ORDER SUMMARY ------------")

    for item in order:
        print(f"\nPizza: {item['pizza']} - Rs {item['base_price']}")
        if item["toppings"]:
            print("  Toppings:")
            for t in item["toppings"]:
                print(f"    - {t} (Rs {toppings_menu[t]})")
        else:
            print("  No toppings added")

    print(f"\nTotal Amount: Rs {total}")

    print("\n------------- CUSTOMER ----------------")
    print(f"Name: {user['name']}")
    print(f"Phone: {user['phone']}")
    print(f"Address: {user['address']}")
    print("---------------------------------------")
    print("Thank you for ordering!")


main()
