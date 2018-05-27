import unittest
from python.algorithms import *


class TestAll(unittest.TestCase):

    def test_insertion_sort(self):
        elements = [2, 3, 1, 0, 5, 4]
        self.assertEqual([0, 1, 2, 3, 4, 5], insertion_sort(elements))
