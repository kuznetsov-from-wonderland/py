"""
6. Реализовать два небольших скрипта:

а) итератор, генерирующий целые числа, начиная с указанного,

б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
"""

from itertools import count, cycle

start = int(input('Введите стартовое число '))

for n in count(start):
    print(n)
    if n >= 1000:
        break

names = ["Katya", 'Daria', 'Sveta', 'Sasha']
counter = 0
for name in cycle(names):
    print(name)
    counter += 1
    if counter >= 1000:
        break
