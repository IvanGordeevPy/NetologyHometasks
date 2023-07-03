import types

# Создание итератора
class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.lst_counter = -1
        self.counter = 0
        self.list_len = len(self.list_of_list)

    def __iter__(self):
        self.lst_counter += 1
        self.counter = 0
        return self

    def __next__(self):
        while self.lst_counter - self.list_len and self.counter == len(self.list_of_list[self.lst_counter]):
          iter(self)
        if self.lst_counter == self.list_len:
          raise StopIteration
        self.counter += 1     
        return self.list_of_list[self.lst_counter][self.counter - 1]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

# Создание генератора
def flat_generator(list_of_lists):
    for list in list_of_lists:
        for element in list:
            yield element

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_1()
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    ob = [ob for ob in FlatIterator(list_of_lists_1)]
    print(ob)

    test_2()
