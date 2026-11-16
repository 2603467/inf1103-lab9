"""Abstract base class for discount strategies (Strategy pattern)."""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Contract: apply() maps an order total to its discounted total."""

    @abstractmethod
    def apply(self, total: float) -> float:
        """Return the discounted total."""

    @abstractmethod
    def describe(self) -> str:
        """Return a short description of the discount."""
