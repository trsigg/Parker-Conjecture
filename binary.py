from language import Language


class Binary(Language):
    base = 2
    period_digits = 1

    @classmethod
    def num_period_letters(cls, number, period_index):
        return len('zero') if number == 0 else len('one')
