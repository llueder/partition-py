import unittest

class PartitionTestCase(unittest.TestCase):
    def cmp_partition(self, expected, actual):
        exp_a, exp_b = expected
        act_a, act_b = actual

        # the order of the numbers in the output is undefined, therefore sort
        exp_a.sort()
        exp_b.sort()
        act_a.sort()
        act_b.sort()

        # which list is a anb b is undefined
        if exp_a == act_a:
            self.assertEqual(exp_b, act_b)
        else:
            self.assertEqual(exp_a, act_b)
            self.assertEqual(exp_b, act_a)
