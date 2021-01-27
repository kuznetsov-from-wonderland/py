"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open('file_2.txt', 'r', encoding='utf-8')

total_lines = 0
line_lengths = []

for line in file:
    total_lines += 1
    line_lengths.append(len(line))


print(f"Количество строк {total_lines}\n")
for idx, l in enumerate(line_lengths):
    print(f"Строка {idx+1} => длина {l-1}")

file.close()
