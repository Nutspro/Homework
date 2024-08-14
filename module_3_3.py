def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(5)
print_params(7, 8)
print_params(b=25)
print_params(6, b=25)
print_params(c=[1, 2, 3])

values_list = ['x', 25, True]
values_dict = {'a': True, 'b': 88, 'c': 'y'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['sun', False]
print_params(*values_list_2, 42) # значение 42 встает на место параметра 'c'