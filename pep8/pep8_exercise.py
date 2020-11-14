def count_message_letters(message):
    counter = 0
    for _ in message:
        counter += 1
    return counter


STRING_CONSTANT = 'Ala ma kota'


def modify_message_to_list(message):
    return [letter + '-' + message for letter in message]


class SampleClass:
    SOME_CONST = 0

    def __init__(self):
        self.list_of_items = []

    def sample_method(self, item):
        return self.list_of_items.append(item)


if __name__ == '__main__':
    pass
