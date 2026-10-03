def calculate_tax(amount):
    tax = amount * 0.10
    return tax                                          # Calculate 10% tax


def process_delivery(current_total, new_value):     
    return current_total + new_value                    # Calculates and returns the updated total inventory

                                                    
def get_valid_input():                                  # Handle user input and validate it
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        return "quit"

                                                        # Input validation using .isdigit()
    if not user_input.isdigit():
        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Error: Stock quantity cannot be negative. Please try again.")
        else:
            print("Error: Invalid entry. Please enter a positive whole number.")
        return None

    return int(user_input)


def generate_report(total_units, failed_attempts, delivery_history):
    print("\n" + "=" * 30)
    print("DELIVERY SUMMARY")
    print("=" * 30)
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")          # Prints the final summary report
    print(f"Transaction History ({len (delivery_history)} entries): {delivery_history}")


def save_report(total_units, failed_attempts, delivery_history):
    with open("inventory.txt", "w") as report_file:
        report_file.write(f"Total Deliveries Processed: {total_units}\n")
        report_file.write(f"Number of Failed/Rejected Entries: {failed_attempts}\n")
        report_file.write(f"Transaction History ({len(delivery_history)} entries): {delivery_history}\n")
    print("Report saved to 'inventory.txt'.")                               # Saves the output to a txt file


def save_inventory(total_units, failed_attempts, delivery_history):
    with open("inventory.txt", "w") as report_file:
        report_file.write(f"Total Deliveries Processed: {total_units}\n")
        report_file.write(f"Number of Failed/Rejected Entries: {failed_attempts}\n")
        report_file.write(f"Transaction History ({len(delivery_history)} entries): {delivery_history}\n")
    print("Inventory saved to 'inventory.txt'.")                            # Saves the inventory output to a txt file


def load_inventory():
    try:
        with open("inventory.txt", "r") as report_file:
            lines = report_file.readlines()
            total_units = int(lines[0].split(": ")[1])
            failed_attempts = int(lines[1].split(": ")[1])
            delivery_history = eval(lines[2].split(": ")[1])
        return total_units, failed_attempts, delivery_history
    except FileNotFoundError:
        print("No existing inventory found.")
        return 0, 0, []
    except Exception as e:
        print(f"Error loading inventory: {e}")
        return 0, 0, []





def main():
    failed_entries = 0
    total_tax_collected = 0.0                                                   # Initialize inventory and counters to zero
    total_inventory, failed_attempts, delivery_history = load_inventory()       # Load existing inventory if available

    # 2. Continuous loop
    while True:
        delivery_amount = get_valid_input()

        # Handle exit signal
        if delivery_amount == "quit":
            break

        # Handle invalid inputs
        if delivery_amount is None:
            failed_entries += 1
            continue

        # 3. Handle valid delivery
        delivery_history.append(delivery_amount)  # Store delivery amount and tax in history
        total_inventory = process_delivery(total_inventory, delivery_amount)
        delivery_tax = calculate_tax(delivery_amount)
        total_tax_collected += delivery_tax
        print(f"Accepted: +{delivery_amount} units | Tax (10%): ${delivery_tax:.2f} | Current Total: {total_inventory}")
        # displays 2 decimal places for tax collected


    generate_report(total_inventory, failed_entries, delivery_history)                          # Generates the final report
    save_report(total_inventory, failed_entries, delivery_history)                              # Saves the report to a text file
    save_inventory(total_inventory, failed_entries, delivery_history)                           # Saves the inventory to a text file

if __name__ == "__main__":
    main()