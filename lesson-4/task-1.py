"""
Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо
запускать скрипт с параметрами.
"""

from sys import argv

try:
    _, hours, rate, bonus = argv
    try:
        res = float(hours) * float(rate) + float(bonus)
        print(f"Employee's payroll equals {res}")
    except ValueError:
        print('Not a number')
except ValueError:
    print('Not enough values')

# python3 task-1.py 160 25 1
