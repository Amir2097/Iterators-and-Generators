class FlatIterator:
    '''Итератор обрабатывает список списков в плоское представление'''
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1

        if self.nested_list_cursor >= len(self.list_of_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor = 0

        if self.main_list_cursor >= len(self.list_of_list):
            raise StopIteration

        return self.list_of_list[self.main_list_cursor][self.nested_list_cursor]


class FlatIterators:
    '''Итератор обрабатывает любой уровень вложенности списков в плоское представление'''
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = -1
        return self

    def __next__(self):
        self.main_list_cursor += 1
        nested = True
        while nested:
            self.new_list = []
            nested = False
            for nested_list in self.list_of_list:
                if isinstance(nested_list, list):
                    self.new_list.extend(nested_list)
                    nested = True
                else:
                    self.new_list.append(nested_list)
            self.list_of_list = self.new_list
        if self.main_list_cursor >= len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.main_list_cursor]
