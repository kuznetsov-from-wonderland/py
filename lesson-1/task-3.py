n = input('Введите число n: ')
result = int(n) + int(f'{n}{n}') + int(f'{n}{n}{n}')
print(f'{n} + {n}{n} + {n}{n}{n} = {result}')
