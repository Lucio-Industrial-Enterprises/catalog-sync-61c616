import unittest

from warehouse.quantity import parse_quantity


class QuantityParserTests(unittest.TestCase):
    def test_valid_quantity(self):
        self.assertEqual(parse_quantity("5"), 5)

    def test_whitespace_trimmed(self):
        self.assertEqual(parse_quantity("  10  "), 10)

    def test_zero_quantity(self):
        """Zero is a valid (non-negative) quantity."""
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_quantity_raises(self):
        """Negative values must be rejected with ValueError."""
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_negative_quantity_large_raises(self):
        """Regression: large negative values are also rejected."""
        with self.assertRaises(ValueError):
            parse_quantity("-100")
