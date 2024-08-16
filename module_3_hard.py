def number_for_sum(n):
    if isinstance(n, str):
        a = len(n)
    elif isinstance(n, list) or isinstance(n, tuple):
        if len(n) > 1:
            a = number_for_sum(n[0]) + number_for_sum(n[1:])
        elif len(n) == 0:
            a = 0
        else:
            a = number_for_sum(n[0])
    elif isinstance(n, set):
        a = number_for_sum(list(n))
    elif isinstance(n, dict):
        a = number_for_sum(list(n.items()))
    else:
        a = n
    return a


def calculate_structure_sum(*args):
    b = number_for_sum(args[0])
    if len(args) > 1:
        b += calculate_structure_sum(*args[1:])
    else:
        pass
    return b


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
result2 = calculate_structure_sum(data_structure, (), 'fgg', {'df': 100}, (False, [{True}]))
print(result)
print(result2)
