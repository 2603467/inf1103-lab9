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

from inventory import Inventory
from inventory_file_handler import InventoryFileHandler
from product_file_handler import load_products
from products import ProductFactory
from supplier import Supplier

INVENTORY_FILE = "inventory.json"
PRODUCTS_FILE = "products.csv"
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


def get_positive_float(prompt: str) -> float:
    """Keep asking until the user enters a positive number."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")
            continue
        if value <= 0:
            print("Please enter a number greater than zero.")
            continue
        return value


def load_products_menu(inventory: Inventory) -> None:
    load_products(PRODUCTS_FILE, inventory,
                  Supplier("S1", "Default Supplier",
                           "supplier@example.com"))


def handle_add(inventory: Inventory) -> None:
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    if inventory.find_product(product_id) is not None:
        print("[Error] Product ID already exists.")
        return

    name = input("Product Name: ")
    price = get_positive_float("Price: ")
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
        product_type = "physical"
        size_prompt = "\nWeight (kg): "
    elif type_choice == "2":
        product_type = "digital"
        size_prompt = "\nDownload Size (MB): "
    else:
        print("\n[Error] Invalid product type.")
        return

    size = read_number(size_prompt, float, minimum=0.01)

    try:
        product = ProductFactory.create(product_type, product_id, name,
                                        price, stock, supplier, size)
    except ValueError as error:
        print(f"\n[Error] Could not create product: {error}")
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
    print("6. Load Products from CSV")
    print("7. Exit")
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
            print("\nLoading products from CSV...")
            load_products_menu(inventory)
        elif option == "7":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("\nInvalid option. Please enter 1-7.")


if __name__ == "__main__":
    main()
