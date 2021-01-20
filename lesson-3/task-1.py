"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print('Cannot divide by 0')
        return


x = int(input('Введите первое число (делимое): '))
y = int(input('Введите второе число (делитель): '))

res = divide(x, y)
if res:
    print(res)
