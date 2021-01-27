"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
from functools import reduce

threshold = 20000
salaries = []


def sum_fn(a, b):
    return a + b


def parse_person(value):
    last_name, salary = value.split()
    salaries.append(float(salary))

    if float(salary) < threshold:
        print(f"{last_name}'s salary is below {threshold}")


src = open("file_3.txt", "r")

for line in src:
    parse_person(line)

src.close()

print(f"\nAverage salary is {reduce(sum_fn, salaries)}")
