from language import Language


class French(Language):
    digit_names = ['', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf']
    suffixes = ['', 'mille', 'millions', 'millard', 'billions']
    tens = ['vingt', 'trente', 'quarante', 'cinquante', 'soixante', 'soixante-dix', 'quatre-vingts']
    teens = ['dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf']

    @classmethod
    def num_period_letters(cls, number, period_index):
        num_letters = 0
        digits = cls.get_digits(number)

        if len(digits) > 0:
            if len(digits) > 1:
                if len(digits) == 3:
                    if digits[2] != 1:
                        num_letters += len(cls.digit_names[digits[2]])
                    num_letters += len('cent')

                if digits[1] in (1, 7, 9):
                    if digits[1] != 1:
                        num_letters += len(cls.tens[digits[1] - 3])
                        if digits[0] == 1:
                            num_letters += len('et')
                        else:
                            num_letters += len('-')
                    num_letters += len(cls.teens[digits[0]])
                else:
                    num_letters += len(cls.tens[digits[1] - 2])
                    if digits[0] != 0:
                        if digits[0] == 1:
                            num_letters += len('et')
                        else:
                            num_letters += len('-')
                        num_letters += len(cls.digit_names[digits[0]])
            else:
                if digits[0] != 1 or period_index == 0:
                    num_letters = len(cls.digit_names[digits[0]])

            num_letters += len(cls.suffixes[period_index])

        return num_letters
