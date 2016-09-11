from language import Language
from english import English


class crh23_Binary(Language):
    base = 2
    period_digits = 1

    @classmethod
    def num_period_letters(cls, number, period_index):
        if number == 1:
            return English.num_letters(cls.base ** period_index)
        else:
            return 0