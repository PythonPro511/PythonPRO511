import unittest  # для запуска из терминала находясь в текущей директории

from discount_funcs import calculate_discount


class TestCalculateDiscount(unittest.TestCase):

    def test_basic_discount(self):
        self.assertEqual(calculate_discount('basic', 100), 95.0)

    def test_silver_discount(self):
        self.assertEqual(calculate_discount('silver', 100), 90.0)

    def test_gold_discount(self):
        self.assertEqual(calculate_discount('gold', 100), 85.0)

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            calculate_discount('platinum', 100)
