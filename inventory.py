"""
Inventory class.

Single Responsibility Principle:
    An Inventory is responsible for managing a COLLECTION of Products.
    It does NOT load/save JSON, display the menu or ask for input.
"""

from collections.abc import Iterator

from products.product import Product


class Inventory:
    """Manages a collection of Product objects."""

    def __init__(self, products: list[Product] | None = None):
        self.__products: list[Product] = list(products) if products else []

    def add_product(self, product: Product) -> bool:
        """
        Add a Product to the inventory.

        Returns False if the product ID is already in use, True otherwise.
        """
        if self.find_product(product.product_id) is not None:
            return False
        self.__products.append(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        """Return the Product with the matching ID, or None."""
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def remove_product(self, product_id: str) -> bool:
        """Remove the Product with the matching ID. Returns success."""
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def display_all_products(self) -> None:
        """Display every product through the Product abstraction."""
        print("\nCurrent Inventory")
        print("-" * 50)
        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products:
                product.display_information()
                print(f"Fulfilment: {product.get_fulfilment_info()}")
        print("-" * 50)

    def all_products(self) -> list[Product]:
        """Return a copy of the products so callers cannot mutate state."""
        return list(self.__products)

    def is_empty(self) -> bool:
        return not self.__products

    def __len__(self) -> int:
        return len(self.__products)

    def __iter__(self) -> Iterator[Product]:
        return iter(self.__products)

    def __str__(self) -> str:
        return f"Inventory({len(self.__products)} products)"
