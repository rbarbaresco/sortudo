import unittest
from python.algorithms import *
import random


RANGE_OF_ELEMENTS = 100
SHUFFLE_TIMES = 100

SORTED_LIST = [i for i in range(0, RANGE_OF_ELEMENTS)]


class TestAll(unittest.TestCase):

    def test_insertion_sort(self):
        self.assertSorted(insertion_sort)

    def test_selection_sort(self):
        self.assertSorted(selection_sort)

    def assertSorted(self, method):
        self.assertEqual([], method([]))

        for i in range(0, SHUFFLE_TIMES):
            shuffled = list(SORTED_LIST)
            random.shuffle(shuffled)
            self.assertEqual(SORTED_LIST, method(shuffled))
