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
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to Mimi's Sweets.")

    # Print the menu header
    print_menu_heading()

    # Loop through the menu dictionary to display options
    i = 1
    for food_category, options in menu.items():
        for meal, price in options.items():
            print_menu_line(i, food_category, meal, price)
            i += 1

    while True:
        # Ask the customer for their order
        menu_selection = input("Please enter the number of the item you would like to order: ")

        # Update the order list using the update_order function
        order = update_order(order, menu_selection, menu_items)

        # Ask the customer if they want to order another item
        another_item = input("Would you like to order anything else? (Type 'y' to continue ordering or type 'n' to finish ordering): ")
        if another_item.lower() == 'n':
            print("Thank you for your order! Please come again.")
            # Calculate the total price
            prices_list = [item["Price"] * item["Quantity"] for item in order]
            order_total = round(sum(prices_list), 2)
            break
    
    # Return the order list and the total price
    return order, order_total


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    # TODO: Check if the customer typed a number
    if menu_selection.isdigit():
        # TODO: Convert the menu selection to an integer
        menu_selection = int(menu_selection)

        # TODO: Check if the menu selection is in the menu items keys
        if menu_selection in menu_items:
            # TODO: Store the item name as a variable
            item_name = menu_items[menu_selection]["Item name"]

            # TODO: Ask the customer for the quantity of the menu item
            # TODO: Use the item name variable in the question
            quantity = input(f"How many {item_name} would you like to order? ")

            # TODO: Check if the quantity is a number, default to 1 if not
            if not quantity.isdigit():
                quantity = 1

            # TODO: Add a dictionary to the order list 
            # TODO: The dictionary should include the item name, price, and quantity
            # TODO: Use the following names for the dictionary keys:
            # TODO: "Item name", "Price", "Quantity"
            order.append({
                "Item name" : item_name,
                "Price" : menu_items[menu_selection]["Price"],
                "Quantity" : int(quantity)
            })
        else:
            # TODO: When the user's input isn't valid, 
            # TODO: tell the customer that their input isn't valid
            print(f"{menu_selection} is not available on the menu. Please try again.")  
    else:
        # TODO: When the menu selection wasn't valid:
        # TODO: Print the menu selection and 
        # TODO: Tell the customer they didn't select a menu option
        print("Invalid selection. Please select a valid menu item number. ")

    # TODO: Return the updated order
    return order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Loop through the items in the customer's receipt
    for item in receipt:
        # Store the dictionary items as variables
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # Print the receipt line using the print_receipt_line function
        print_receipt_line(item_name, price, quantity)

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    meals = {
        "Cupcake": {
            "Espresso": 4,
            "Salted Caramel": 5,
            "Peanut Butter": 4
        },
        "Cookies": {
            "Chocolate Chip": 2,
            "Smores": 4
        },
        "Extras": {
            "Dog Treats": 2,
            "Cookie Assortment Box": 15,
            "Salted Caramel Jars" : 8
        }
    }
  
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)
