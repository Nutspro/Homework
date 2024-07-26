my_dict = {'Marina':1980,'Natasha':1989, 'Petr':1992}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Natasha'))
print('Not existing value:', my_dict.get('Egor'))
my_dict['Egor'] = 2001
my_dict['Veniamin'] = 1999
ex = my_dict.pop('Petr')
print('Deleted value:', ex)
print('Modified dictionary:', my_dict)

my_set = {2,6,0,False,'cat',2.0}
print('Set:', my_set)
my_set.add((1,6,0))
my_set.add('dog')
my_set.discard('cat')
print('Modified set:', my_set)