"""
This module contains pylint samples.
"""


class SamplePylint:  # pylint: disable=too-few-public-methods
    """This class represents pylint sample."""
    def __init__(self, number):
        self._number = number

    @staticmethod
    def divide(number):
        """

        :param number:
        :return:
        """
        if number == 0:
            raise ZeroDivisionError()


class Children(SamplePylint):
    """This class represents pylint sample."""
    def __init__(self, name, number):
        super().__init__(number)
        self._name = name

    @staticmethod
    def some_method(param):
        """

        :param param:
        :return:
        """
        return param in (1, 2, 3)

    @staticmethod
    def some_method2():
        """

        :return:
        """
        print('bad implementation')


if __name__ == '__main__':
    sample = SamplePylint(10)
    try:
        sample.divide(0)
    except ZeroDivisionError:
        pass
    sample.divide(0)

    Children.some_method(4)
