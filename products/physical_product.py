from products.product import CanBeShipped, Product
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    """A product that physically exists and can be shipped."""

    SHIPPING_RATE_PER_KG = 2.50

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        if weight <= 0:
            raise ValueError("Weight must be positive.")
        self.__weight = weight

    @property
    def weight(self) -> float:
        return self.__weight

    def get_fulfilment_info(self) -> str:
        return f"{self.name} requires physical shipping ({self.__weight} kg)."

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "PhysicalProduct":
        return cls(data["id"], data["name"], data["price"], data["stock"],
                   Supplier.from_dict(data["supplier"]), data["weight"])

    def calculate_shipping_cost(self) -> float:
        return self.__weight * self.SHIPPING_RATE_PER_KG

    def __str__(self) -> str:
        return f"{super().__str__()} | Weight: {self.__weight} kg"

    def __repr__(self) -> str:
        return f"PhysicalProduct({self.product_id!r}, {self.name!r}, " \
               f"{self.price!r}, {self.stock!r}, {self.__weight!r})"
