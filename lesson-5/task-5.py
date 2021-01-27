"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint
from functools import reduce

file = open("file_5.txt", "w+")

nums = [str(randint(-10, 10)) for _ in range(0, 10)]

file.write(" ".join(nums))
file.seek(0)
nums_from_file = file.read()


def sum_fn(a, b):
    return a + b


print(f"\nSum is {reduce(sum_fn, list(map(int, nums_from_file.split())))}")

file.close()
