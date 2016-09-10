class Language:
    """General base class for finding lengths of written forms of numbers in various languages"""
    base = 10  # numerical base used in language
    period_digits = 3  # number of digits in a numerical "period" (e.g. 3 in English)
    digit_names = []
    suffixes = []

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
    def num_period_letters(cls, number):
        """Returns the number of letters in the written form of a single period (without suffix)"""
        letters = 0
        digits = cls.get_digits(number)

        for digit in digits:
            if digit > 0:
                letters += len(cls.digit_names[digit]) + len(cls.suffixes[digit])

        return letters

    @classmethod
    def num_letters(cls, number):
        """Returns the number of letters in the written form of a number"""
        num_letters = 0
        period_index = cls.period_digits

        while number > 0:
            period = number % cls.base ** cls.period_digits
            num_letters += cls.num_period_letters(period) + len(cls.suffixes[period_index])
            number -= period
            period_index += 1

        return num_letters

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
