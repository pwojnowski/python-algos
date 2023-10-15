from unittest import TestCase

from algos.dp import number_factor_dp

class DynamicProgrammingTest(TestCase):

    def test_number_factor(self):
        self.assertEqual(1, number_factor_dp(1, [1, 3, 4]))
        self.assertEqual(1, number_factor_dp(2, [1, 3, 4]))
        self.assertEqual(1, number_factor_dp(3, [1, 3, 4]))
