seasons_dict = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима',
}

month_input = int(input("Введите месяц (1..12) "))

month = seasons_dict.get(month_input)

if month is None:
    print('Invalid input')
else:
    print(month)
