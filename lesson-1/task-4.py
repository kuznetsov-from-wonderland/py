n = int(input("Введите целое положительное число "))
max = 1

while True:
    last_char = n % 10
    if last_char > max:
        max = last_char
    n = n // 10
    if n > 9:
        continue
    else:
        print(f"Максимальное цифра в числе {max}")
        break
