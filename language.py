class Language:
    """General base class for finding lengths of """
    base = 10
    period_digits = 3  # number of digits in a numerical "period" (3 in English)
    digit_lengths = []  # length of digit names in language
    period_lengths = []  # length of period names (hundred, million, billion, etc.)

    @classmethod
    def get_digits(cls, number):
        """Returns a list of digits in the number written in the language's base, from least to most significant"""
        digits = []

        while number > 0:
            digit = number % cls.base
            digits.append(digit)
            number = (number - digit) / cls.base

        return digits

    @classmethod
    def num_letters(cls, number):
        letters = 0
        digits = cls.get_digits(number)

        for digit in digits:
            if digit > 0:
                letters += cls.digit_lengths[digit] + cls.power_lengths[digit]

        return letters

    @classmethod
    def find_cycle(cls, number):
        """Returns results of iterating num_letters until a cycle is reached"""
        cycle = []

        while number > 0 and number not in cycle:
            cycle.append(number)
            number = cls.num_letters(number)

        return cycle

    @classmethod
    def find_lengths_of_cycles_up_to(cls, bound):
        cycle_lengths = []

        for i in xrange(bound):
            cycle_lengths.append(len(cls.find_cycle(i)))
