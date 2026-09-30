import unittest

from src.list_utils import unique_preserve_order


class UniquePreserveOrderTest(unittest.TestCase):
    def test_removes_duplicates_while_preserving_order(self):
        values = [3, 1, 3, 2, 1]

        result = unique_preserve_order(values)

        self.assertEqual(result, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
