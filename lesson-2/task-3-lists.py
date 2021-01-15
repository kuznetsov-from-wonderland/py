seasons_list = [
    'Зима',
    'Зима',
    'Весна',
    'Весна',
    'Весна',
    'Лето',
    'Лето',
    'Лето',
    'Осень',
    'Осень',
    'Осень',
    'Зима',
]

month_input = int(input("Введите месяц (1..12) "))

if len(seasons_list) >= month_input >= 1:
    month = seasons_list[month_input - 1]
    print(month)
else:
    print('Invalid input')
