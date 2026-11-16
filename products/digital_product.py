from products.product import Product
from supplier import Supplier


class DigitalProduct(Product):
    """A product delivered digitally, with a download size but no weight."""

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        if download_size <= 0:
            raise ValueError("Download size must be positive.")
        self.__download_size = download_size

    @property
    def download_size(self) -> float:
        return self.__download_size

    def get_fulfilment_info(self) -> str:
        return f"{self.name} is delivered digitally ({self.__download_size} MB download)."

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "DigitalProduct":
        return cls(data["id"], data["name"], data["price"], data["stock"],
                   Supplier.from_dict(data["supplier"]), data["download_size"])

    def __str__(self) -> str:
        return f"{super().__str__()} | Download Size: {self.__download_size} MB"

    def __repr__(self) -> str:
        return f"DigitalProduct({self.product_id!r}, {self.name!r}, " \
               f"{self.price!r}, {self.stock!r}, {self.__download_size!r})"
