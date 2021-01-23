"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
"""

from functools import reduce


def multiply(a, b):
    return a * b


my_list = range(100, 1000 + 1)
evens = [n for n in my_list if n % 2 == 0]
print(reduce(multiply, evens))

# my_list = range(1, 10 + 1)
# evens = [n for n in my_list if n % 2 == 0]
# print(reduce(multiply, evens))
# print(2*4*6*8*10)
