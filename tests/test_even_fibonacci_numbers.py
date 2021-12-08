from solutions.even_fibonacci_numbers import EvenFibonaccyNumbers
from assertpy import assert_that

class TestEvenFibonacciNumbers:

    def test_fist_ten_fibonacci_terms(self):
        expected_terms = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        even_fibonacci_numbers = EvenFibonaccyNumbers()
        actual_terms = even_fibonacci_numbers.get_terms_below(100)
        assert_that(actual_terms).is_equal_to(expected_terms)

        
    def test_even_fibonacci_terms_below_10(self):
        expected_terms = [2, 8, 34]
        even_fibonacci_numbers = EvenFibonaccyNumbers()
        actual_terms = even_fibonacci_numbers.get_even_terms_below(100)
        assert_that(actual_terms).is_equal_to(expected_terms)

    def test_sum_of_even_fibonacci_terms_below_8(self):
        limit = 10
        expected_sum = 10
        even_fibonacci_numbers = EvenFibonaccyNumbers()
        actual_sum = even_fibonacci_numbers.get_sum_of_even_fibonacci_terms_below(limit)
        assert_that(actual_sum).is_equal_to(expected_sum)
    
    def test_sum_of_even_fibonacci_terms_below_400(self):
        limit = 400
        expected_sum = 188
        even_fibonacci_numbers = EvenFibonaccyNumbers()
        actual_sum = even_fibonacci_numbers.get_sum_of_even_fibonacci_terms_below(limit)
        assert_that(actual_sum).is_equal_to(expected_sum)
    
    def test_sum_of_even_fibonacci_terms_below_4_million(self):
        limit = 4000000
        expected_sum = 4613732
        even_fibonacci_numbers = EvenFibonaccyNumbers()
        actual_sum = even_fibonacci_numbers.get_sum_of_even_fibonacci_terms_below(limit)
        assert_that(actual_sum).is_equal_to(expected_sum)
