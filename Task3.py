# Создайте функцию генератор чисел Фибоначчи

n = int(input('Введите число: '))


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(*fibonacci(n))