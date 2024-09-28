import unittest
from shopping import Checkout, pricing_rules

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.co = Checkout(pricing_rules)

    def test_case_1(self):
        self.co.scan('atv')
        self.co.scan('atv')
        self.co.scan('atv')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 249.00)

    def test_case_2(self):
        self.co.scan('atv')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('atv')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 2718.95)

    def test_case_3(self):
        self.co.scan('mbp')
        self.co.scan('vga')
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 1949.98)

    # Edge Test Cases
    def test_no_items_scanned(self):
        self.assertEqual(self.co.total(), 0.00)

    def test_single_item_scanned(self):
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 549.99)

    def test_multiple_items_no_discounts(self):
        self.co.scan('ipd')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 579.99)

    def test_buy_x_get_y_free(self):
        self.co.scan('atv')
        self.co.scan('atv')
        self.co.scan('atv')
        self.assertEqual(self.co.total(), 219.00)

    def test_bulk_discount(self):
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.assertEqual(self.co.total(), 2499.95)

    def test_free_item_with_purchase(self):
        self.co.scan('mbp')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 1399.99)

    def test_combination_of_discounts(self):
        self.co.scan('mbp')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('ipd')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 3899.94)

    def test_exceeding_free_items(self):
        self.co.scan('mbp')
        self.co.scan('mbp')
        self.co.scan('vga')
        self.co.scan('vga')
        self.co.scan('vga')
        self.assertEqual(self.co.total(), 2829.98)
        
        
if __name__ == '__main__':
    unittest.main()