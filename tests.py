import random
from unittest import TestCase

from merge_sort import MergeSort


class MergeSortTest(TestCase):

    def test_when_list_is_empty(self):
        test_case = []
        expected = []
        algo_result = MergeSort().divide(test_case)
        self.assertEqual(expected, algo_result)

    def test_with_two_elements(self):
        test_case = [20, 2]
        expected = [2, 20]
        algo_result = MergeSort().divide(test_case)
        self.assertEqual(expected, algo_result)

    def test_with_five_elements(self):
        test_case = [10, 2, 1, 9, 20]
        expected = [1, 2, 9, 10, 20]
        algo_result = MergeSort().divide(test_case)
        self.assertEqual(expected, algo_result)

    def test_negative_elements(self):
        test_case = [-20, -2, -40, 0, -1, -50]
        expected = [-50, -40, -20, -2, -1, 0]
        algo_result = MergeSort().divide(test_case)
        self.assertEqual(expected, algo_result)

    def test_many_elements(self):
        test_case = range(1, 1000)
        random.shuffle(test_case)
        expected = sorted(test_case)
        algo_result = MergeSort().divide(test_case)
        self.assertEqual(expected, algo_result)
