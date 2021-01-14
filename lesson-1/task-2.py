# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк

time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)

formatted_hours = f"0{hours}" if hours < 10 else f"{hours}"
formatted_minutes = f"0{minutes}" if minutes < 10 else f"{minutes}"
formatted_seconds = f"0{seconds}" if seconds < 10 else f"{seconds}"

print(f"Время в формате чч:мм:сс   {formatted_hours}:{formatted_minutes}:{formatted_seconds}")
