"""
Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

src = open("file_4.1.txt", "r")
res = open("file_4.2.txt", "w")

mapping = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

result = []

for line in src:
    name, value = line.split('—')
    result.append(f"{mapping[name.strip()]} - {value}")

res.writelines(result)
res.close()
src.close()
