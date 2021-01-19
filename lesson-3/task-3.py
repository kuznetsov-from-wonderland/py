"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def fn(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    max_1, max_2 = numbers[1:]
    return max_1 + max_2


print(fn(1, 2, 3))
print(fn(111, 222, -3))
print(fn(14, -20, 0))
