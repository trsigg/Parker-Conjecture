from language import Language


class English(Language):
    digit_names = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    suffixes = ['', 'thousand', 'million', 'billion', 'trillion']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    @classmethod
    def num_period_letters(cls, number):
        num_letters = 0
        digits = cls.get_digits(number)

        if len(digits) > 0:
            if len(digits) > 1:
                if len(digits) == 3:
                    num_letters += len(cls.digit_names[digits[2]] + 'hundred')

                if digits[1] == 1:
                    num_letters += len(cls.teens[digits[0]])
                else:
                    num_letters += len(cls.tens[digits[1] - 2] + cls.digit_names[digits[0]])
            else:
                num_letters = len(cls.digit_names[digits[0]])

        return num_letters
