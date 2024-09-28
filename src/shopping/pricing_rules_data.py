from src.shopping.pricing_rules import BuyXGetYFree, BulkDiscount, FreeItemWithPurchase
from src.shopping.product import Product

ipd = Product(price=549.99, rules=[BulkDiscount(5, 499.99)])
mbp = Product(price=1399.99, rules=[FreeItemWithPurchase('mbp', 'vga')])
atv = Product(price=109.50, rules=[BuyXGetYFree(2, 1)])
vga = Product(price=30.00, rules=[])

pricing_rules = {
    'ipd': ipd,
    'mbp': mbp,
    'atv': atv,
    'vga': vga
}

def getdata():
    """get pricing rules"""
    return pricing_rules