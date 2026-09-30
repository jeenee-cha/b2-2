import unittest

from src.math_utils import clamp


class ClampTest(unittest.TestCase):
    def test_returns_value_inside_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_returns_minimum_for_value_below_range(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_returns_maximum_for_value_above_range(self):
        self.assertEqual(clamp(15, 0, 10), 10)


if __name__ == "__main__":
    unittest.main()
