class EvenFibonaccyNumbers:

    def __init__(self):
        """
        F1 = F2 = 1
        """
        self.fibonacci_terms = [1, 2]
        self.even_fibonacci_terms = [2]
        
    def get_terms_below(self, limit):
        length_of_fibonacci_numbers = len(self.fibonacci_terms)
        f_n_minus_one = self.fibonacci_terms[length_of_fibonacci_numbers-1]
        f_n_minus_two = self.fibonacci_terms[length_of_fibonacci_numbers-2]
        next_fibonacci_number = f_n_minus_one + f_n_minus_two
        if(next_fibonacci_number < limit):
            self.fibonacci_terms.append(next_fibonacci_number)
            self.get_terms_below(limit)
        return self.fibonacci_terms
    
    def get_even_terms_below(self, limit):
        length_of_fibonacci_numbers = len(self.fibonacci_terms)
        f_n_minus_one = self.fibonacci_terms[length_of_fibonacci_numbers-1]
        f_n_minus_two = self.fibonacci_terms[length_of_fibonacci_numbers-2]
        next_fibonacci_number = f_n_minus_one + f_n_minus_two
        if(next_fibonacci_number < limit):
            if(self.is_even_number(next_fibonacci_number)):
                self.even_fibonacci_terms.append(next_fibonacci_number)

            self.fibonacci_terms.append(next_fibonacci_number)
            self.get_even_terms_below(limit)
        return self.even_fibonacci_terms

    def get_sum_of_even_fibonacci_terms_below(self, limit):
        even_terms = self.get_even_terms_below(limit)
        return sum(even_terms)

    def is_even_number(self, number):
        return number % 2 == 0
