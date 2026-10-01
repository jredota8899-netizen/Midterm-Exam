FILE_NAME = "sales_log.txt"

#DISPLAY THE MENO
def display_menu():
    """Display the main menu."""
    print("=" * 39)
    print("        SALES RECORD MANAGEMENT")
    print("=" * 39)
    print("1. add sales record")
    print("2. View All Record & Summary Statistics")
    print("3. Clear All Sales")
    print("4. Exit System")
    print("=" * 39)


#ADD RECORDS
def addSaleRecord():
    """Get sale information and save it to the sales log."""
    print("\n--- Add Sale Record ---")

    item_name = input("Enter item name: ").strip()

    if not item_name:
        print("Item name cannot be empty.")
        return

    # Validate and convert quantity to an integer.
    try:
        quantity = int(input("Enter quantity sold: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        return

    # Validate and convert price to a float.
    try:
        price_per_unit = float(input("Enter price per unit: "))

        if price_per_unit < 0:
            print("Price cannot be negative.")
            return
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    # Calculate
    total_amount = quantity * price_per_unit

    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(
                f"{item_name},{quantity},{price_per_unit:.2f},"
                f"{total_amount:.2f}\n"
            )

        print("Sale record saved successfully.")

    except OSError as error:
        print(f"Error saving the sale record: {error}")

def viewRecord():
    exit()


def clearSalesData():
    print("Thank you for using the Sales Record Management System.")
    exit()


def main():
    """Run the Sales Record Management System."""
    while True:
        display_menu()

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            addSaleRecord()

        elif choice == "2":
            viewRecord()

        elif choice == "3":
            clearSalesData()

        elif choice == "4":
            print(
                "Thank you for using the Sales Record Management System."
            )
            break

        else:
            print("Invalid option. Please select a number from 1 to 4.")


# Start the program.
if __name__ == "__main__":
    main()