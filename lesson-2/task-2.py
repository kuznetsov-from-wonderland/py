count = int(input("Введите количество элементов списка "))
data = []
# [1, 2, 3, 4, 5, 11, 13]

i = 0

while i < count:
    result = input(f"Введите {i + 1}-й айтем списка ")
    data.append(result)
    i += 1

print(data)

chunked_data = []

j = 0
is_even = len(data) % 2 == 0

limit = len(data) - 1

while j < limit:
    chunked_data.append([data[j + 1], data[j]])
    j += 2

chunked_data = sum(chunked_data, [])

if not is_even:
    chunked_data.append(data[-1])

print(chunked_data)
