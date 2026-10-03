import json
import os

default_inventory = [                                                           # created dictonary with several products
    {"id": "8001", "name": "Sweet Madame", "price": "$9.50", "stock": 1659},
    {"id": "8002", "name": "Lavender Melon", "price": "$8.00", "stock": 11},
    {"id": "8003", "name": "Ghost Pie", "price": "$15.00", "stock": 3172}
]

FILE_NAME = "inventory.json"


def load_inventory():
    """Loads inventory from JSON file if present; otherwise creates default data."""
    if os.path.exists(FILE_NAME):
        print(f"{FILE_NAME} found.")
        try:
            with open(FILE_NAME, "r") as file:
                inventory = json.load(file)
                print("Inventory loaded successfully.\n")
                return inventory
        except Exception as e:
            print(f"Error loading {FILE_NAME}: {e}. Loading default data.\n")
            return default_inventory
    else:
        print(f"{FILE_NAME} not found. Creating new inventory...\n")
        save_inventory(default_inventory)
        return default_inventory


def save_inventory(inventory):
    """Saves the current inventory list to inventory.json."""
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)


def display_all(inventory):
    """Displays current inventory matching the exact sample layout."""
    print("Current Inventory")
    print("-" * 40)
    for prod in inventory:
        print(f"ID: {prod['id']} | Name: {prod['name']} | Price: {prod['price']} | Stock: {prod['stock']}")
    print("-" * 40)


def add_product(inventory):
    """Adds a new product to the inventory with auto-incremented ID (800x)."""
    # Auto-generate next ID based on highest current numeric ID
    max_id = max([int(prod["id"]) for prod in inventory], default=8000)
    new_id = str(max_id + 1)

    name = input("Enter product name: ").strip()
    try:
        price = float(input("Enter product price: "))
        stock = int(input("Enter initial stock: "))
        inventory.append({"id": new_id, "name": name, "price": price, "stock": stock})
        print(f"Product '{name}' added successfully with ID: {new_id}.\n")
    except ValueError:
        print("Invalid price or stock amount. Operation cancelled.\n")


def update_stock(inventory):
    """Updates stock quantity for a target product ID."""
    prod_id = input("Enter product ID to update: ").strip()
    for prod in inventory:
        if prod["id"] == prod_id:
            try:
                added_stock = int(input(f"Enter stock to add for {prod['name']}: "))
                if added_stock < 0:
                    print("Stock cannot be negative.")
                    return
                prod["stock"] += added_stock
                print(f"Stock updated successfully! New Stock for {prod['name']}: {prod['stock']}\n")
                return
            except ValueError:
                print("Invalid stock number.\n")
                return
    print("Product ID not found.\n")


def search_product(inventory):
    """Searches for a product by ID or name."""
    query = input("Enter Product ID or Name to search: ").strip().lower()
    found = False
    for prod in inventory:
        if prod["id"].lower() == query or query in prod["name"].lower():
            print(f"Found -> ID: {prod['id']} | Name: {prod['name']} | Price: {prod['price']} | Stock: {prod['stock']}")
            found = True
    if not found:
        print("No matching product found.\n")


def print_menu():
    print("---------------- MENU ----------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------------------")


def main():
    print("=========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=========================================\n")

    inventory = load_inventory()

    while True:
        print_menu()
        choice = input("\nEnter option: ").strip()

        if choice == "1":
            print()
            display_all(inventory)
            print()
        elif choice == "2":
            print()
            add_product(inventory)
        elif choice == "3":
            print()
            update_stock(inventory)
        elif choice == "4":
            print()
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Inventory saved to inventory.json.\n")
        elif choice == "6":
            save_inventory(inventory)
            print("Exiting system. Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()