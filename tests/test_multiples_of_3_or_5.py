from assertpy import assert_that

from solutions.multiples_of_3_or_5 import MultiplesOfThreeOrFive

"""
If we list all the natural numbers below 10 that 
are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

class TestMultiplesOfThreeOrFive:

    def test_natural_numbers_below_ten(self):
        multiples_of_three_and_five = MultiplesOfThreeOrFive()
        source_number = 10
        expected_sum = 23
        actual_sum = multiples_of_three_and_five.get_sum_of_multiples(source_number)
        assert_that(actual_sum).is_equal_to(expected_sum)

    def test_natural_numbers_below_thousand(self):
        multiples_of_three_and_five = MultiplesOfThreeOrFive()
        source_number = 1000
        expected_sum = 233168
        actual_sum = multiples_of_three_and_five.get_sum_of_multiples(source_number)
        assert_that(actual_sum).is_equal_to(expected_sum)