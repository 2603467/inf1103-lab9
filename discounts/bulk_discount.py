"""Flat amount off above a threshold, e.g. BulkDiscount(200, 20)."""

from discounts.discount_strategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):
    """Takes `amount` off any total of `threshold` or more."""

    def __init__(self, threshold: float, amount: float):
        if threshold < 0:
            raise ValueError("Threshold cannot be negative.")
        if amount <= 0:
            raise ValueError("Discount amount must be greater than zero.")
        self.__threshold = threshold
        self.__amount = amount

    @property
    def threshold(self) -> float:
        return self.__threshold

    @property
    def amount(self) -> float:
        return self.__amount

    def apply(self, total: float) -> float:
        return total - self.__amount if total >= self.__threshold else total

    def describe(self) -> str:
        return f"{self.__amount:g} off totals of {self.__threshold:g}+"
