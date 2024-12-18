import unittest
from algorithms import find_min_positive, sum_negative, fibonacci, electric_current

class TestAlgorithms(unittest.TestCase):

    def test_find_min_positive(self):
        self.assertEqual(find_min_positive([5, 3, 9, 1]), 1)
        self.assertEqual(find_min_positive([1, 2, 3]), 1)
        self.assertRaises(ValueError, find_min_positive, [])

    def test_sum_negative(self):
        self.assertEqual(sum_negative([-1, -2, -3]), -6)
        self.assertEqual(sum_negative([0, -1, -2]), -3)
        self.assertEqual(sum_negative([5, -5, 0]), 0)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_electric_current(self):
        self.assertEqual(electric_current(10, 2), 5)
        self.assertEqual(electric_current(20, 4), 5)
        self.assertRaises(ZeroDivisionError, electric_current, 10, 0)

if __name__ == '__main__':
    unittest.main()
