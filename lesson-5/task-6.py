"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from functools import reduce
import re

src = open("file_6.txt", "r")


def sum_fn(a, b):
    return a + b


def parse_values(val):
    # nums = []
    # for i in val.split():
    #     n = re.sub("\D", '', i)
    #     if n != '':
    #         nums.append(int(n))
    nums = map(int, [re.sub("\D", '', n) for n in val.split() if re.sub("\D", '', n) != ''])
    return reduce(sum_fn, nums)


result = {}

for line in src:
    subject, values = line.split(':')
    value = parse_values(values)
    result[subject] = value

src.close()

print(result)
