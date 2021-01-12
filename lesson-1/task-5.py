revenue = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))

if revenue > costs:
    profit = revenue - costs
    print(f"Фирма работает с прибылью. Выручка составила {profit}")
    print(f"Рентабельность выручки составила {profit / revenue}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника сотавила {profit / workers}")

elif revenue == costs:
    print("Фирма работает впустую, доходы равны расходам")

else:
    print("Фирма работает в убыток")
