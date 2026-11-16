"""Factory pattern: centralised Product creation."""

from products.digital_product import DigitalProduct
from products.physical_product import PhysicalProduct
from products.product import Product
from supplier import Supplier


class ProductFactory:

    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock: int, supplier: Supplier, size: float) -> Product:
        """Create a Product.

        `size` is weight (kg) for physical, download size (MB) for digital.
        """
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock,
                                   supplier, size)
        if product_type == "digital":
            return DigitalProduct(product_id, name, price, stock,
                                  supplier, size)
        raise ValueError(f"Unknown product type: {product_type}")
