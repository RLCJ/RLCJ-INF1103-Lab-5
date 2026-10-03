import json
import os

default_inventory = [                                                           # created dictonary with several products
    {"id": "8001", "name": "Sweet Madame", "price": "$9.50", "stock": 1659},
    {"id": "8002", "name": "Lavender Melon", "price": "$8.00", "stock": 11},
    {"id": "8003", "name": "Ghost Pie", "price": "$15.00", "stock": 3172},
    {"id": "8004", "name": "Beetle Soup", "price": "$5.00", "stock": 456},
    {"id": "8005", "name": "The Flood", "price": "$3.43", "stock": 343},
]

FILE_NAME = "inventory.json"


def load_inventory():                               # loads inventory from JSON file if present; otherwise creates empty inventiry

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


def display_all(inventory):         # Read (crud)
    
    print("Current Inventory")
    print("-" * 40)
    for prod in inventory:
        print(f"ID: {prod['id']} | Name: {prod['name']} | Price: {prod['price']} | Stock: {prod['stock']}")
    print("-" * 40)


def add_product(inventory):         # Create (crud)
    """Adds a new product to the inventory with auto-incremented ID (800x)."""
    # Auto-generate next ID based on highest current numeric ID
    max_id = max([int(prod["id"]) for prod in inventory], default=8000)
    new_id = str(max_id + 1)

    while True:
        name = input("Enter product name: ").strip()
        if not name:
            print("Error: Product name cannot be empty. Please try again.")
        elif name.isdigit():
            print("Error: Product name cannot be just numbers (e.g., '123'). Please enter a valid name.")
        else:
            break
    while True:
        price_input = input("Enter product price ($): ").strip()
        try:
            price = float(price_input)
            if price <= 0:
                print("Error: Price must be greater than $0.00. Please try again.")
            else:
                break
        except ValueError:
            print("Error: Invalid price. Please enter a valid decimal number (e.g., 9.99).")

    while True:
        stock_input = input("Enter initial stock: ").strip()
        if stock_input.isdigit():
            stock = int(stock_input)
            break
        print("Error: Invalid stock amount. Please enter a valid integer.")

    inventory.append({"id": new_id, "name": name, "price": f"${price:.2f}", "stock": stock})
    print(f"Product '{name}' added successfully with ID: {new_id}.\n")


def update_stock(inventory):         # Update (crud)
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


def delete_product(inventory):      # Delete (crud)
    prod_id = input("Enter Product ID to delete: ").strip()
    
    for i, prod in enumerate(inventory):
        if prod["id"] == prod_id:
            confirm = input(f"Are you sure you want to delete '{prod['name']}' (ID: {prod['id']})? (y/n): ").strip().lower()
            if confirm == 'y':
                deleted = inventory.pop(i)
                print(f"Success: Product '{deleted['name']}' (ID: {deleted['id']}) has been deleted.\n")
            else:
                print("Operation cancelled.\n")
            return

    print("Product ID not found.\n")

def print_menu():
    print("---------------- MENU ----------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Delete Product")
    print("6. Save Inventory")
    print("7. Exit")
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
            print()
            delete_product(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Inventory saved to inventory.json.\n")
        elif choice == "7":
            save_inventory(inventory)
            print("Saving inventory before exit... \n Inventory saved successfully!")
            print("Thank you for using the Inventory Management System")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    main()