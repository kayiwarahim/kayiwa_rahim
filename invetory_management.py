def display_inventory(inventory):
    """Displays the current inventory."""
    if not inventory:
        print("No inventory available at the moment")
    else:
        print("\nProduct Name\tQuantity")
        for name in inventory:
            print(f"{name}\t\t{inventory[name]}")

def add_product(inventory):
    """Adds a new product to the inventory."""
    name = input("Enter product name: ")
    if name in inventory:
        print("Product already exists. Try updating it.")
    else:
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                inventory[name] = quantity
                print("Product entered successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid number for quantity.")

def update_quantity(inventory):
    """Updates the quantity of an existing product."""
    name = input("Enter product name to update: ")
    if name in inventory:
        try:
            change = int(input("Enter quantity to add or subtract(e.g -3 or 5): "))
            inventory[name] += change
            if inventory[name] < 0:
                 print(f"Warning: Quantity for {name} is now negative ({inventory[name]}).")
            print("Quantity updated.")
        except ValueError:
            print("Invalid input. Please enter a valid number for change in quantity.")
    else:
        print("Product not found")

def remove_product(inventory):
    """Removes a product from the inventory."""
    name = input("Enter product name to remove: ")
    if name in inventory:
        del inventory[name]
        print("Product removed")
    else:
        print("Product not found")

inventory = {}

menu_options = [
    "Display Inventory",
    "Add Product",
    "Update Product Quantity",
    "Remove product",
    "Exit"
]

while True:
    print("\nInventory Management System")
    for i, option in enumerate(menu_options):
        print(f"{i+1}. {option}")

    try:
        choice = int(input(f"Enter your choice (Between 1-{len(menu_options)}): "))

        if choice == 1:
            display_inventory(inventory)
        elif choice == 2:
            add_product(inventory)
        elif choice == 3:
            update_quantity(inventory)
        elif choice == 4:
            remove_product(inventory)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print(f"Invalid choice. Please choose a number between 1 and {len(menu_options)}.")
    except ValueError:
        print("Invalid input. Please enter a number.")