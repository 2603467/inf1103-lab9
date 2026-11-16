"""
Product class.

SRP: a Product represents and manages ONE product only.
Abstract per OCP: new product types are added by subclassing, not editing Product.
"""

from abc import ABC, abstractmethod

from supplier import Supplier


class CanBeShipped(ABC):
    """Interface-style contract for objects that can be shipped."""

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Calculate and return the shipping cost."""


class Product(ABC):
    """Represents a single product held in the inventory."""

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier):
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if not isinstance(stock, int) or isinstance(stock, bool):
            raise TypeError("Stock quantity must be an integer.")
        if stock < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier: Supplier = supplier

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def supplier(self) -> Supplier:
        return self.__supplier

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Describe how this product reaches the customer."""

    def update_stock(self, quantity: int) -> None:
        """
        Set a new stock quantity.

        The Product is the only thing that is allowed to change its own
        stock, which means it can validate the value first.
        """
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Stock quantity must be an integer.")
        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.__stock = quantity

    def display_information(self) -> None:
        """Display this product's details."""
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        print(f"Supplier: {self.__supplier.name} ({self.__supplier.contact_email})")

    def to_dict(self) -> dict:
        """Return a plain dictionary (used for JSON persistence)."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict(),
        }

    def __str__(self) -> str:
        return (
            f"ID: {self.__product_id} | Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )

    def __repr__(self) -> str:
        return (
            f"Product({self.__product_id!r}, {self.__name!r}, "
            f"{self.__price!r}, {self.__stock!r})"
        )
