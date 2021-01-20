"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

first_name_input = input('enter firstname: ')
last_name_input = input('enter lastname: ')
year_input = input('enter year: ')
city_input = input('enter city: ')
email_input = input('enter email: ')
phone_input = input('input phone: ')


def log_person(first_name, last_name, year, city, email, phone):
    return ' '.join([first_name, last_name, year, city, email, phone])


print(log_person(first_name=first_name_input, year=year_input, city=city_input, email=email_input,
                 last_name=last_name_input,
                 phone=phone_input))
