from abc import ABC, abstractmethod
from typing import Dict

class PricingRule(ABC):
    @abstractmethod
    def apply(self, item: str, quantity: int, price: float, cart: Dict[str, int]) -> float:
        """Apply the pricing rule to the given item."""
        pass

class BuyXGetYFree(PricingRule):
    def __init__(self, x: int, y: int) -> None:
        """
        Initialize the BuyXGetYFree rule.

        :param x: Number of items to buy to get the free items.
        :param y: Number of free items.
        """
        self.x = x
        self.y = y

    def apply(self, item: str, quantity: int, price: float, cart: Dict[str, int]) -> float:
        """
        Apply the BuyXGetYFree rule.

        :param item: The item to which the rule is applied.
        :param quantity: The quantity of the item.
        :param price: The price of the item.
        :param cart: The current state of the cart.
        :return: The total price after applying the rule.
        """
        free_items = (quantity // (self.x + self.y)) * self.y
        return (quantity - free_items) * price

class BulkDiscount(PricingRule):
    def __init__(self, min_quantity: int, discounted_price: float) -> None:
        """
        Initialize the BulkDiscount rule.

        :param min_quantity: Minimum quantity to qualify for the discount.
        :param discounted_price: Discounted price per item.
        """
        self.min_quantity = min_quantity
        self.discounted_price = discounted_price

    def apply(self, item: str, quantity: int, price: float, cart: Dict[str, int]) -> float:
        """
        Apply the BulkDiscount rule.

        :param item: The item to which the rule is applied.
        :param quantity: The quantity of the item.
        :param price: The price of the item.
        :param cart: The current state of the cart.
        :return: The total price after applying the rule.
        """
        if quantity >= self.min_quantity:
            return quantity * self.discounted_price
        return quantity * price

class FreeItemWithPurchase(PricingRule):
    def __init__(self, required_item: str, free_item: str) -> None:
        """
        Initialize the FreeItemWithPurchase rule.

        :param required_item: The item required to get the free item.
        :param free_item: The free item.
        """
        self.required_item = required_item
        self.free_item = free_item

    def apply(self, item: str, quantity: int, price: float, cart: Dict[str, int]) -> float:
        """
        Apply the FreeItemWithPurchase rule.

        :param item: The item to which the rule is applied.
        :param quantity: The quantity of the item.
        :param price: The price of the item.
        :param cart: The current state of the cart.
        :return: The total price after applying the rule.
        """
        if item == self.required_item and self.free_item in cart:
            free_items = min(cart[self.free_item], cart[self.required_item])
            cart[self.free_item] -= free_items
            return quantity * price
        return quantity * price