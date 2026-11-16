"""Fourth strategy, added without changing Order (Open/Closed Principle)."""

from discounts.discount_strategy import DiscountStrategy


class StudentDiscount(DiscountStrategy):
    """5% student discount."""

    STUDENT_RATE = 5

    def apply(self, total: float) -> float:
        return total * (1 - self.STUDENT_RATE / 100)

    def describe(self) -> str:
        return f"{self.STUDENT_RATE:g}% student discount"
