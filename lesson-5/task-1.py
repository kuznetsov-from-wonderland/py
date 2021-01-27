"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

data = []

while True:
    result = input("Enter anything: ")
    if result == '':
        print(data)
        break
    else:
        data.append(f"{result}\n")

with open("test_1.txt", "w") as file:
    file.writelines(data)
