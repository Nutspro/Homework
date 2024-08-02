first = int(input('введите целое число: '))
second = int(input('введите целое число: '))
third = int(input('введите целое число: '))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)