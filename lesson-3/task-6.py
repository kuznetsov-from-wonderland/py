"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def capitalizer(s):
    return s.lower().capitalize()


print(capitalizer('text'))
print(capitalizer('python'))
print(capitalizer('ilya'))


def sentence_capitalizer(s):
    words = s.split()
    res = []
    for word in words:
        res.append(capitalizer(word))
    return " ".join(res)


sentence = input('Введите предложение из слов: (например "Hello, my name is Elias")')
print(sentence_capitalizer(sentence))
