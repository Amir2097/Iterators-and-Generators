def flat_generator(list_of_lists):
    '''Генератор обрабатывает список списков'''
    for main_list in list_of_lists:
        for nested_list in main_list:
            yield nested_list


def flat_generators(list_of_list):
    '''Генератор обрабатывает любой уровень вложенности списков в плоское представление'''
    nested = True
    while nested:
        new_list = []
        nested = False
        for nested_list in list_of_list:
            if isinstance(nested_list, list):
                new_list.extend(nested_list)
                nested = True
            else:
                new_list.append(nested_list)
        list_of_list = new_list
    for item in list_of_list:
        yield item