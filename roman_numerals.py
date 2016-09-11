from language import Language


class RomanNumerals(Language):
    period_digits = 1

    @classmethod
    def num_period_letters(cls, number, period_index):
        if period_index < 6:
            if number in (2, 4, 6, 9):
                return 2
            elif number in (1, 5):
                return 1
            elif number in (3, 7):
                return 3
            else:  # Number is 8, assuming 1-digit input
                return 4
        else:
            return cls.base * digit * (period_index - 6)  # Repeated M-bars
