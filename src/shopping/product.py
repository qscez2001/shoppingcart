from typing import List
from src.shopping.pricing_rules import PricingRule

class Product:
    def __init__(self, price, rules=None):
        self.price = price
        self.rules = rules if rules else []