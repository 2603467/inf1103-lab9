"""
Inventory Management System - OOP version of the Week 5 program.

Responsibilities of this module (main program):
    * Displays the menu
    * Gets user input
    * Calls the appropriate Inventory / Product methods

The data itself lives in Product objects, managed by an Inventory object.
JSON file handling is delegated to an InventoryFileHandler.
"""

from collections.abc import Callable

from products.digital_product import DigitalProduct
from inventory import Inventory
from inventory_file_handler import InventoryFileHandler
from products.physical_product import PhysicalProduct
from supplier import Supplier

INVENTORY_FILE = "inventory.json"
file_handler = InventoryFileHandler(INVENTORY_FILE)


def load_inventory() -> Inventory:
    """Load the inventory from file, or start empty."""
    inventory = file_handler.load()
    if inventory is not None:
        print(f"{INVENTORY_FILE} found.")
        print("Inventory loaded successfully.")
        return inventory

    print(f"No existing {INVENTORY_FILE}. Starting with empty inventory.")
    return Inventory()


def save_inventory(inventory: Inventory) -> None:
    """Save every Product in the inventory to file."""
    file_handler.save(inventory)
    print(f"Inventory saved successfully to {INVENTORY_FILE}.")


def read_number(prompt: str, cast: Callable[[str], float],
                minimum: float = 0) -> float | int:
    """Read a number of the requested type, at least `minimum`."""
    while True:
        raw = input(prompt)
        try:
            value = cast(raw)
        except ValueError:
            print("[Error] Please enter a valid number.")
            continue
        if value < minimum:
            print(f"[Error] Value must be at least {minimum}.")
            continue
        return value


def handle_add(inventory: Inventory) -> None:
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    if inventory.find_product(product_id) is not None:
        print("[Error] Product ID already exists.")
        return

    name = input("Product Name: ")
    price = read_number("Price: ", float)
    stock = read_number("Stock Quantity: ", int)

    print("\nSupplier details:")
    supplier_id = input("Supplier ID: ")
    supplier_name = input("Supplier Name: ")
    supplier_email = input("Supplier Contact Email: ")
    supplier = Supplier(supplier_id, supplier_name, supplier_email)

    print("\nProduct type:")
    print("1. Physical")
    print("2. Digital")
    type_choice = input("Choose type: ")

    if type_choice == "1":
        weight = read_number("\nWeight (kg): ", float, minimum=0.01)
        product = PhysicalProduct(product_id, name, price, stock, supplier,
                                  weight)
    elif type_choice == "2":
        size = read_number("\nDownload Size (MB): ", float, minimum=0.01)
        product = DigitalProduct(product_id, name, price, stock, supplier,
                                 size)
    else:
        print("\n[Error] Invalid product type.")
        return

    inventory.add_product(product)
    print("\nProduct added successfully!")


def handle_update(inventory: Inventory) -> None:
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.find_product(product_id)
    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product.name}")
    print(f"Current Stock: {product.stock}")

    new_stock = read_number("\nNew Stock Quantity: ", int)
    product.update_stock(new_stock)
    print("\nStock updated successfully!")


def handle_search(inventory: Inventory) -> None:
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.find_product(product_id)
    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found")
    print("-" * 50)
    product.display_information()
    print("-" * 50)


def print_menu() -> None:
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main() -> None:
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        print_menu()
        option = input("Enter option: ")

        if option == "1":
            inventory.display_all_products()
        elif option == "2":
            handle_add(inventory)
        elif option == "3":
            handle_update(inventory)
        elif option == "4":
            handle_search(inventory)
        elif option == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("\nInvalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()
