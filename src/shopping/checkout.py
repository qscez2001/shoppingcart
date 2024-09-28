from typing import Dict
from decimal import Decimal
from src.shopping.product import Product


class Checkout:
    def __init__(self, rules: Dict[str, Product]) -> None:
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
        total_price = Decimal('0.0')
        for item, quantity in self.cart.items():
            product = self.pricing_rules[item]
            price = Decimal(str(product.price))
            rules = product.rules
            item_total = Decimal(quantity) * price
            for rule in rules:
                item_total = Decimal(rule.apply(item, quantity, price, self.cart))
            total_price += item_total
        total_price = round(total_price, 2)
        return float(total_price)