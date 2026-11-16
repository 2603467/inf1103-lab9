"""Product type hierarchy."""

from products.digital_product import DigitalProduct
from products.physical_product import PhysicalProduct
from products.product import CanBeShipped, Product

__all__ = ["Product", "PhysicalProduct", "DigitalProduct", "CanBeShipped"]
