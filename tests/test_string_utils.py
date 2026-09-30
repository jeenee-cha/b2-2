import unittest

from src.string_utils import normalize_whitespace


class NormalizeWhitespaceTest(unittest.TestCase):
    def test_collapses_mixed_whitespace_and_trims_ends(self):
        self.assertEqual(normalize_whitespace("  hello\n team\tgit  "), "hello team git")

    def test_returns_empty_string_for_empty_input(self):
        self.assertEqual(normalize_whitespace(""), "")

    def test_returns_empty_string_for_whitespace_only_input(self):
        self.assertEqual(normalize_whitespace(" \n\t "), "")


if __name__ == "__main__":
    unittest.main()