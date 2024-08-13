def my_parol(n=int(input('Введите число от 3 до 20: '))):
    parol = []
    t = 1
    while t < n and n >= 3 and n <= 20:
        k = t + 1
        while k < n:
            if n % (t + k) == 0:
                parol.append(str(t))
                parol.append(str(k))
            k = k + 1
        t = t + 1
    return parol
result = ''.join(my_parol())
print(result)