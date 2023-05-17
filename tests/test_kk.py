import unittest
from common import PartitionTestCase
import partitionpy

class TestKK(PartitionTestCase):
    def test_too_few_numbers(self):
        with self.assertRaises(ValueError):
            partitionpy.karmarkar_karp([])
        with self.assertRaises(ValueError):
            partitionpy.karmarkar_karp([0])

    def test_numbers(self):
        expected = ([8, 6], [7, 5, 4])
        actual = partitionpy.karmarkar_karp([4,5,6,7,8])
        self.cmp_partition(expected, actual)

    def test_indices_sorted(self):
        # kk does not sort internally, still check that the indices are still correct
        expected =([1, 3, 4], [0, 2])
        actual = partitionpy.karmarkar_karp([8,7,6,5,4], return_indices=True)
        self.cmp_partition(expected, actual)

    def test_indices_unsorted(self):
        # kk does not sort internally, still check that the indices are still correct
        expected =([0, 1, 3], [2, 4])
        actual = partitionpy.karmarkar_karp([4,5,6,7,8], return_indices=True)
        self.cmp_partition(expected, actual)

if __name__ == "__main__":
    unittest.main()