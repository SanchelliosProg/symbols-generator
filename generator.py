import string
import random


class StringGenerator:
    ALL_MODE = 0
    ALL_LETTERS_MODE = 1
    JUST_DIGITS_MODE = 2
    JUST_PUNCTUATION_MODE = 3
    chars = ''
    size = 0

    def __init__(self, mode, size):
        self.size = int(size)
        if mode == self.ALL_MODE:
            self.chars += string.ascii_lowercase
            self.chars += string.ascii_uppercase
            self.chars += string.digits
            self.chars += string.punctuation
            self.chars += ' '
        elif mode == self.ALL_LETTERS_MODE:
            self.chars += string.ascii_lowercase
            self.chars += string.ascii_uppercase
        elif mode == self.JUST_DIGITS_MODE:
            self.chars += string.digits
        else:
            print 'No such mode'

    def string_generator(self):
        return ''.join(random.choice(self.chars) for _ in range(self.size))

    def string_generator(self, new_size):
        return ''.join(random.choice(self.chars) for _ in range(new_size))
