"""Default strategy: total unchanged."""

from discounts.discount_strategy import DiscountStrategy


class NoDiscount(DiscountStrategy):
    """Applies no discount."""

    def apply(self, total: float) -> float:
        return total

    def describe(self) -> str:
        return "No discount"
