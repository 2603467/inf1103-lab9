"""Discount strategies (Strategy pattern)."""

from discounts.bulk_discount import BulkDiscount
from discounts.discount_strategy import DiscountStrategy
from discounts.no_discount import NoDiscount
from discounts.percentage_discount import PercentageDiscount
from discounts.student_discount import StudentDiscount

__all__ = ["DiscountStrategy", "NoDiscount", "PercentageDiscount",
           "BulkDiscount", "StudentDiscount"]
