"""Fixed percentage off, e.g. PercentageDiscount(10) takes 10% off."""

from discounts.discount_strategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
    """Takes a fixed percentage off any total."""

    def __init__(self, percentage: float):
        if percentage <= 0:
            raise ValueError("Percentage must be greater than zero.")
        self.__percentage = percentage

    @property
    def percentage(self) -> float:
        return self.__percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.__percentage / 100)

    def describe(self) -> str:
        return f"{self.__percentage:g}% discount"
