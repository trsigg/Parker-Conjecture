import matplotlib.pyplot as plt


class Language(object):
    """General base class for finding lengths of written forms of numbers in various languages"""
    base = 10  # numerical base used in language
    period_digits = 3  # number of digits in a numerical "period"
    digit_names = []
    suffixes = []  # period suffixes (thousand, million, billion, etc.)

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
    def num_period_letters(cls, number, period_index):
        """Returns the number of letters in the written form of a single period (without suffix)"""
        digits = cls.get_digits(number)
        num_letters = 0

        for digit in digits:
            if digit > 0:
                num_letters += len(cls.digit_names[digit])

        num_letters += len(cls.suffixes[period_index])

        return num_letters

    @classmethod
    def num_letters(cls, number):
        """Returns the number of letters in the written form of a number"""
        num_letters = 0
        period_index = 0

        while number > 0:
            period = number % cls.base ** cls.period_digits
            num_letters += cls.num_period_letters(period, period_index)
            number = (number - period) / (cls.base ** cls.period_digits)
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
    def find_cycle_lengths_in_range(cls, bound, upper=None):
        """Returns a list of all cycle lengths for numbers in specified range"""
        cycle_lengths = []

        if upper is None:
            to_check = xrange(bound)
        else:
            to_check = xrange(bound, upper)

        for number in to_check:
            cycle_lengths.append(len(cls.find_cycle(number)))

        return cycle_lengths

    @classmethod
    def find_max_cycles_in_range(cls, bound, upper=None):
        """Returns maximum length cycle length from numbers in specified range and list of numbers which yield it"""
        max_length = 0
        cycles = []

        if upper is None:
            to_check = xrange(bound)
        else:
            to_check = xrange(bound, upper)

        for number in to_check:
            length = len(cls.find_cycle(number))

            if length == max_length:
                cycles.append(number)
            elif length > max_length:
                max_length = length
                cycles = [number]

        return max_length, cycles

    @classmethod
    def plot_cycle_lengths_in_range(cls, bound, upper=None, histogram=False):
        cycle_lengths = cls.find_cycle_lengths_in_range(bound, upper)
        if histogram:
            plt.hist(cycle_lengths)
        else:
            if upper is None:
                x_vals = range(bound)
            else:
                x_vals = range(bound, upper)

            plt.plot(x_vals, cycle_lengths)

        plt.show()
