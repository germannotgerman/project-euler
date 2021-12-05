class MultiplesOfThreeOrFive:

    def __init__(self):
        self.multiplier_three = 3
        self.multiplier_five = 5

    def get_sum_of_multiples(self, source_number):
        sum_of_multiples = 0
        candidate_numbers = self.get_candidate_numbers(source_number)
        multiples_of_three_and_five = self.get_multiples_of_three_and_five(candidate_numbers)
        return sum(multiples_of_three_and_five)

    def get_candidate_numbers(self, source_number):
        candidate_numbers = list(range(self.multiplier_three, source_number))
        return candidate_numbers

    def get_multiples_of_three_and_five(self, candidate_numbers):
        candidate_multiples = []
    
        for candidate_number in candidate_numbers:
            if (candidate_number % self.multiplier_three == 0 or candidate_number % self.multiplier_five == 0):
                candidate_multiples.append(candidate_number)
        return candidate_multiples
