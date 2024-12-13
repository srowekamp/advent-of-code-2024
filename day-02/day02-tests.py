import unittest
from day02 import safe, safe_with_dampener


class TestSafetyMethod(unittest.TestCase):
    def test_1(self):
        self.assertFalse(safe([1, 2, 7, 8, 9]))

    def test_2(self):
        self.assertFalse(safe([8, 6, 4, 4, 1]))

    def test_3(self):
        self.assertTrue(safe([7, 6, 4, 2, 1]))

    def test_4(self):
        self.assertTrue(safe([1, 3, 6, 7, 9]))


class TestSafetyWithDamper(unittest.TestCase):
    def test_1(self):
        self.assertTrue(safe_with_dampener([7, 6, 4, 2, 1]))

    def test_2(self):
        self.assertFalse(safe_with_dampener([1, 2, 7, 8, 9]))

    def test_3(self):
        self.assertFalse(safe_with_dampener([9, 7, 6, 2, 1]))

    def test_4(self):
        self.assertTrue(safe_with_dampener([1, 3, 2, 4, 5]))

    def test_5(self):
        self.assertTrue(safe_with_dampener([8, 6, 4, 4, 1]))

    def test_6(self):
        self.assertTrue(safe_with_dampener([1, 3, 6, 7, 9]))

if __name__ == '__main__':
    unittest.main()
