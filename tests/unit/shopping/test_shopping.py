import unittest
from src.shopping.checkout import Checkout
from src.shopping.pricing_rules_data import getdata

class TestCheckout(unittest.TestCase):
    def setUp(self):
        """Set up a new Checkout instance before each test."""
        # self.co = Checkout(pricing_rules)
        self.pricing_rules = getdata()
        self.co = Checkout(self.pricing_rules)

    def test_buy_x_get_y_free(self):
        """Test the BuyXGetYFree discount rule."""
        self.co.scan('atv')
        self.co.scan('atv')
        self.co.scan('atv')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 249.00)

    def test_bulk_discount(self):
        """Test the BulkDiscount rule."""
        self.co.scan('atv')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('atv')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 2718.95)

    def test_free_item_with_purchase(self):
        """Test the FreeItemWithPurchase rule."""
        self.co.scan('mbp')
        self.co.scan('vga')
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 1949.98)

    def test_no_items_scanned(self):
        """Test that the total is zero when no items are scanned."""
        self.assertEqual(self.co.total(), 0.00)

    def test_single_item_scanned(self):
        """Test the total for a single item."""
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 549.99)

    def test_multiple_items_no_discounts(self):
        """Test the total for multiple items without discounts."""
        self.co.scan('ipd')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 579.99)

    def test_buy_x_get_y_free_discount(self):
        """Test the BuyXGetYFree discount rule."""
        self.co.scan('atv')
        self.co.scan('atv')
        self.co.scan('atv')
        self.assertEqual(self.co.total(), 219.00)

    def test_bulk_discount_applied(self):
        """Test the BulkDiscount rule."""
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 2499.95)

    def test_free_item_with_purchase_applied(self):
        """Test the FreeItemWithPurchase rule."""
        self.co.scan('mbp')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 1399.99)

    def test_combination_of_discounts(self):
        """Test a combination of different discount rules."""
        self.co.scan('mbp')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 3899.94)

    def test_exceeding_free_items(self):
        """Test exceeding the number of free items."""
        self.co.scan('mbp')
        self.co.scan('mbp')
        self.co.scan('vga')
        self.co.scan('vga')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 2829.98)
        
        
if __name__ == '__main__':
    unittest.main()