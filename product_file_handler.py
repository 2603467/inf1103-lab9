"""Load Products from a CSV file (Factory pattern + exception handling)."""

import csv

from inventory import Inventory
from products import ProductFactory
from supplier import Supplier

# CSV has no size column; kg for physical, MB for digital.
DEFAULT_PRODUCT_SIZE = 1.0


def load_products(path: str, inventory: Inventory,
                  supplier: Supplier) -> None:
    """Load products from a CSV file via the factory, skipping bad rows."""
    loaded = 0
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  # skip header row
            for row in reader:
                try:
                    product = ProductFactory.create(
                        row[0], row[1], row[2], float(row[3]), int(row[4]),
                        supplier, DEFAULT_PRODUCT_SIZE)
                except ValueError as error:
                    print(f"[Error] Skipping row {row}: {error}")
                    continue
                if inventory.add_product(product):
                    loaded += 1
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
