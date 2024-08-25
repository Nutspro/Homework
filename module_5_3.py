class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'Объект класса House сравнивать можно только с объектами класса House'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Объект класса House сравнивать можно только с объектами класса House'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'Объект класса House сравнивать можно только с объектами класса House'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Объект класса House сравнивать можно только с объектами класса House'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'Объект класса House сравнивать можно только с объектами класса House'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'Объект класса House сравнивать можно только с объектами класса House'

    def __add__(self, value: int):
        if isinstance(value, int):
            self.number_of_floors += value
        else:
            print('Количество этажей должно быть целым числом (только тип int)')
        return self

    def __radd__(self, value: int):
        self.__add__(value)
        return self

    def __iadd__(self, value: int):
        self.__add__(value)
        return self

    def __sub__(self, value: int):
        if isinstance(value, int):
            self.number_of_floors -= value
        else:
            print('Количество этажей должно быть целым числом (только тип int)')
        return self

    def __isub__(self, value: int):
        self.__sub__(value)
        return self

    def __mul__(self, value: int):
        if isinstance(value, int):
            self.number_of_floors *= value
        else:
            print('Множитель должен быть целым числом (только тип int)')
        return self

    def __rmul__(self, value: int):
        self.__mul__(value)
        return self

    def __imul__(self, value: int):
        self.__mul__(value)
        return self

    def __truediv__(self, value: int):
        if isinstance(value, int):
            self.number_of_floors //= value
        else:
            print('Делитель должен быть целым числом (только тип int)')
        return self

    def __itruediv__(self, value: int):
        self.__truediv__(value)
        return self

    def __floordiv__(self, value: int):
        self.__truediv__(value)
        return self

    def __ifloordiv__(self, value: int):
        self.__truediv__(value)
        return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__