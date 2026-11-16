"""Product type hierarchy."""

from products.digital_product import DigitalProduct
from products.physical_product import PhysicalProduct
from products.product import CanBeShipped, Product
from products.product_factory import ProductFactory

__all__ = ["Product", "PhysicalProduct", "DigitalProduct",
           "CanBeShipped", "ProductFactory"]
