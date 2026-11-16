"""
InventoryFileHandler class.

Single Responsibility Principle:
    This class is responsible ONLY for reading/writing the inventory
    JSON file. It never talks to the user and never manages the menu.
"""

import json
import os

from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct
from product import Product

# Maps the JSON "type" identifier to its product class.
PRODUCT_TYPES: dict[str, type[Product]] = {
    "physical": PhysicalProduct,
    "digital": DigitalProduct,
}

class InventoryFileHandler:
    """Loads and saves an Inventory to a JSON file."""

    def __init__(self, filename: str):
        self.__filename = filename

    @property
    def filename(self) -> str:
        return self.__filename

    def load(self) -> Inventory | None:
        """Return an Inventory built from the JSON file, or None if absent."""
        if not os.path.exists(self.__filename):
            return None
        with open(self.__filename) as f:
            data = json.load(f)
        return Inventory([PRODUCT_TYPES[item["type"]].from_dict(item)
                          for item in data])

    def save(self, inventory: Inventory) -> None:
        """Write every Product in the inventory to the JSON file."""
        data = [product.to_dict() for product in inventory.all_products()]
        with open(self.__filename, "w") as f:
            json.dump(data, f, indent=4)
