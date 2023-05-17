import unittest
from common import PartitionTestCase
import partitionpy

class TestGreedy(PartitionTestCase):
    def test_too_few_numbers(self):
        with self.assertRaises(ValueError):
            partitionpy.naive_greedy([])
        with self.assertRaises(ValueError):
            partitionpy.naive_greedy([0])

    def test_numbers(self):
        expected = ([8, 5, 4], [7, 6])
        actual = partitionpy.naive_greedy([4,5,6,7,8])
        self.cmp_partition(expected, actual)

    def test_indices_sorted(self):
        # greedy will sort internally, check that the indices are still correct
        expected =([4, 3, 0], [1, 2])
        actual = partitionpy.naive_greedy([8,7,6,5,4], return_indices=True)
        self.cmp_partition(expected, actual)

    def test_indices_unsorted(self):
        # greedy will sort internally, check that the indices are still correct
        expected =([0, 1, 4], [2, 3])
        actual = partitionpy.naive_greedy([4,5,6,7,8], return_indices=True)
        self.cmp_partition(expected, actual)

if __name__ == "__main__":
    unittest.main()