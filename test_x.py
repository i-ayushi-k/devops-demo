"""Unit tests for x.py."""

import unittest

from x import add


class TestAdd(unittest.TestCase):
    """Test the add function."""

    def test_add(self):
        """Test addition of two numbers."""
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()