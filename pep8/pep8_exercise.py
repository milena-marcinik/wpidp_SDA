"""
This module contains pep8 samples.
"""


def count_message_letters(message):
    """
    Counts letters in the given string.

    :param message: string containing message to count
    :return: number of letters
    """
    counter = 0
    for _ in message:
        counter += 1
    return counter


STRING_CONSTANT = 'Ala ma kota'


def modify_message_to_list(message):
    """

    :param message:
    :return:
    """
    return [letter + '-' + message for letter in message]


class SampleClass:  # pylint: disable=too-few-public-methods
    """This class represents pep8 sample."""
    SOME_CONST = 0

    def __init__(self):
        self.list_of_items = []

    def sample_method(self, item):
        """

        :param item:
        :return:
        """
        return self.list_of_items.append(item)


if __name__ == '__main__':
    pass
