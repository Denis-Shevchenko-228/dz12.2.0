import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(arrs.get([1, 2, 3], 3, "test"), "test")
        self.assertEqual(arrs.get([], 1), None)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, 0), [])
