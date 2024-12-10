def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")


def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    order = []  # Initialize order list
    menu_items = get_menu_items_dict(menu)  # Map menu items to numbers

    # Greeting and menu display
    print("Welcome to the Generic Take Out Restaurant.")
    print_menu_heading()
    i = 1
    for food_category, options in menu.items():
        for meal, price in options.items():
            print_menu_line(i, food_category, meal, price)
            i += 1

    while True:
        menu_selection = input("Type menu number: ")

        # Update the order based on user selection
        order = update_order(order, menu_selection, menu_items)

        another_item = input("Would you like to keep ordering? (N) to quit: ")
        if another_item.lower() == 'n':
            print("Thank you for your order.")
            prices_list = [item["Price"] * item["Quantity"] for item in order]
            order_total = round(sum(prices_list), 2)
            break

    return order, order_total


def update_order(order, menu_selection, menu_items):
    """
    Updates the order based on the user's selection.
    """
    if menu_selection.isdigit():
        menu_selection = int(menu_selection)
        if menu_selection in menu_items:
            item_name = menu_items[menu_selection]["Item name"]
            quantity = input(f"What quantity of {item_name} would you like? ")
            if not quantity.isdigit():
                quantity = 1
            order.append({
                "Item name": item_name,
                "Price": menu_items[menu_selection]["Price"],
                "Quantity": int(quantity)
            })
        else:
            print(f"{menu_selection} is not available on the menu. Please try again.")
    else:
        print("Invalid selection. Please select a valid menu item number.")

    return order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.
    """
    for item in receipt:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        print_receipt_line(item_name, price, quantity)


def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.
    """
    item_spaces = " " * (32 - len(item_name))
    price_spaces = " " * (6 - len(str(price)))
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")


def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")


def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.
    """
    item_spaces = " " * (32 - len(food_category + meal) - 3)
    i_spaces = " " * (5 if index >= 10 else 6)
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")


def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to menu numbers.
    """
    menu_items = {}
    i = 1
    for food_category, options in menu.items():
        for meal, price in options.items():
            menu_items[i] = {"Item name": f"{food_category} - {meal}", "Price": price}
            i += 1
    return menu_items


def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.
    """
    return {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }


if __name__ == "__main__":
    meals = get_menu_dictionary()
    order, total = place_order(meals)
    print("\nThis is what we are preparing for you.")
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")
    print_itemized_receipt(order)
    print_receipt_footer(total)
