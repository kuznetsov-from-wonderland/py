"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста
"""

import json
from functools import reduce


def sum_fn(a, b):
    return a + b


# return value
def rv(x):
    return list(x.values())[0]


profit = {}
result = []

with open('file_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, company_type, revenue, costs = line.split()
        profit[name] = int(revenue) - int(costs)

successful_companies = [{c: profit[c]} for c in profit if profit[c] > 0]

companies_dict = {}

for c in successful_companies:
    key = list(c.keys())[0]
    companies_dict[key] = c[key]

result.append(companies_dict)

average = reduce(sum_fn, list(map(rv, successful_companies)))
result.append({"average_profit": average})

with open('file_7.json', 'w', encoding='utf-8') as output:
    json.dump(result, output, ensure_ascii=False, indent=2)

    pretty_json = json.dumps(result, ensure_ascii=False, indent=2)
    print(pretty_json)
