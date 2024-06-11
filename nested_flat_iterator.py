class FlatIterator:
    def __init__(self, list_of_list):
        """
        Инициализация итератора для списков с любым уровнем вложенности.

        :param list_of_list: список списков для итерации.
        """
        self.stack = [(list_of_list, 0)]

    def __iter__(self):
        """
        Метод, который делает объект итератором.

        :return: сам объект итератора.
        """
        return self

    def __next__(self):
        """
        Метод для получения следующего элемента в последовательности.

        :return: следующий элемент в последовательности.
        :raises StopIteration: если все элементы уже пройдены.
        """
        while self.stack:
            current_list, current_index = self.stack[-1]
            if current_index == len(current_list):
                self.stack.pop()
                continue
            self.stack[-1] = (current_list, current_index + 1)
            item = current_list[current_index]
            if isinstance(item, list):
                self.stack.append((item, 0))
            else:
                return item
        raise StopIteration


def test_3():
    """
    Тест для FlatIterator с любым уровнем вложенности.
    """
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
