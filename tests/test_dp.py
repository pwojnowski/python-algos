from unittest import TestCase

from algos.dp import number_factor_dp

class DynamicProgrammingTest(TestCase):

    def test_number_factor(self):
        factors = [1, 3, 4]
        self.assertEqual(0, number_factor_dp(0, factors))

        self.assertEqual(1, number_factor_dp(1, factors))
        self.assertEqual(1, number_factor_dp(2, factors))

        self.assertEqual(2, number_factor_dp(3, factors))
        self.assertEqual(3, number_factor_dp(4, [1, 3, 5]))
        self.assertEqual(4, number_factor_dp(4, factors))
        self.assertEqual(6, number_factor_dp(5, factors))
        self.assertEqual(9, number_factor_dp(6, factors))
        self.assertEqual(15, number_factor_dp(7, factors))
