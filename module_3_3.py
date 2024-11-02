def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [23, 'Kasha', True]
values_dict = {'a': 325, 'b': 'Vodka', 'c': False}
values_list_2 = [54.32, 'Строка']
print_params()
print_params(10, 27, 23523)
print_params(21, 'Domashka', False)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)