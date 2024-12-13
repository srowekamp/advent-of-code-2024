import unittest
from day04 import check_a, load, check_b

class Test1(unittest.TestCase):
    def test_check(self):
        d = load('test_input.txt')
        self.assertEqual(18, check_a(d))
    def test_check_b(self):
        d = load('test_input.txt')
        self.assertEqual(9, check_b(d))
    def test_one(self):
        d = ['M.M', '.A.', 'S.S']
        self.assertEqual(1, check_b(d))
    def test_one_flip(self):
        d = ['S.S', '.A.', 'M.M']
        self.assertEqual(1, check_b(d))
    def test_m(self):
        d = ['M.M', '.A.', 'M.M']
        self.assertEqual(0, check_b(d))
    def test_none(self):
        d = ['M.M', 'M.M', 'S.S']
        self.assertEqual(0, check_b(d))
    def test_missing_a(self):
        d = ['M.M', '...', 'S.S']
        self.assertEqual(0, check_b(d))
    def test_side_by_side(self):
        d = ['M.S.MA.', '.A.A.A.', 'M.S.MA.']
        self.assertEqual(2, check_b(d))

if __name__ == '__main__':
    unittest.main()