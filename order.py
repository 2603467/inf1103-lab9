from discounts import DiscountStrategy, NoDiscount
from order_line import OrderLine
from products.product import Product


class Order:
    """Collection of order lines with a swappable discount strategy."""

    def __init__(self, order_id: str,
                 discount: DiscountStrategy | None = None):
        self.__order_id = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount = discount if discount is not None else NoDiscount()

    @property
    def order_id(self) -> str:
        return self.__order_id

    @property
    def order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    @property
    def discount(self) -> DiscountStrategy:
        return self.__discount

    def set_discount(self, discount: DiscountStrategy) -> None:
        """Swap the discount strategy."""
        self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Create the OrderLine here; OrderLines are never passed in."""
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, index: int) -> bool:
        if 0 <= index < len(self.__order_lines):
            self.__order_lines.pop(index)
            return True
        return False

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(total)

    def display_order(self) -> None:
        print(f"Order {self.__order_id} ({self.__discount.describe()})")
        for index, line in enumerate(self.__order_lines):
            print(f"  [{index}] {line.product.name} x {line.quantity} "
                  f"= ${line.calculate_subtotal():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
