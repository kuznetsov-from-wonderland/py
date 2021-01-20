"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
 """


def strange_sum():
    total = 0
    running = True
    while running:
        n = input('Input numbers or Q for quit - ').split()

        res = 0
        for num in n:
            if num.lower() == 'q':
                running = False
                break
            else:
                res += int(num)
        total += res
        if running:
            print(f'Current sum is {total}')
    print(f'Result sum is {total}')


strange_sum()