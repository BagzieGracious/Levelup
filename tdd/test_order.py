from unittest import TestCase
import orders 

class TestOrder(TestCase):
    def test_order(self):
        self.assertEqual(orders.check_order_status(2), True)

    def test_pending(self):
        self.assertFalse(orders.check_order_pending(2), True)

    def test_integers(self):
        self.assertEqual(orders.check_integer('1'), False)

    def test_both(self):
        self.assertEqual(orders.check_exist_both(1), False)

    def test_add_list(self):
        self.assertIn(5, orders.delivered_orders, True)
    
    def test_add_new_list(self):
        self.assertEqual(orders.check_adding_pending(2), False)