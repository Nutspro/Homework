immutable_var = ('apple', 1, True)
print(immutable_var)
# immutable_var[1] = 2
# ~~~~~~~~~~~~~^^^
# Ошибка: тип данных "кортеж" (tuple) не позволяет заменять свои элементы
mutable_list = [False, 3, 'banana']
mutable_list[0] = 5
mutable_list[1] = True
mutable_list[-1] = 'sun'
mutable_list = mutable_list + ['monkey']
print(mutable_list)