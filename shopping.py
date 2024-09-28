from abc import ABC, abstractmethod
from typing import Dict, List

class CheckoutInterface(ABC):
    @abstractmethod
    def scan(self, item: str) -> None:
        """Scan an item and add it to the cart."""
        pass

    @abstractmethod
    def total(self) -> float:
        """Calculate the total price of all items in the cart."""
        pass

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

class Checkout(CheckoutInterface):
    def __init__(self, rules: Dict[str, Dict[str, List[PricingRule]]]) -> None:
        """
        Initialize the Checkout system.

        :param rules: The pricing rules for the items.
        """
        self.pricing_rules = rules
        self.cart = {}

    def scan(self, item: str) -> None:
        """
        Scan an item and add it to the cart.

        :param item: The item to be scanned.
        """
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def total(self) -> float:
        """
        Calculate the total price of all items in the cart.

        :return: The total price.
        """
        total_price = 0.0
        for item, quantity in self.cart.items():
            price = self.pricing_rules[item]['price']
            rules = self.pricing_rules[item].get('rules', [])
            item_total = quantity * price
            for rule in rules:
                item_total = rule.apply(item, quantity, price, self.cart)
            total_price += item_total
        total_price = round(total_price, 2)
        return total_price

pricing_rules = {
    'ipd': {
        'price': 549.99,
        'rules': [BulkDiscount(5, 499.99)]
    },
    'mbp': {
        'price': 1399.99,
        'rules': [FreeItemWithPurchase('mbp', 'vga')]
    },
    'atv': {
        'price': 109.50,
        'rules': [BuyXGetYFree(2, 1)]
    },
    'vga': {
        'price': 30.00,
        'rules': []
    }
}