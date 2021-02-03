"""
 Реализовать класс Matrix (матрица). Обеспечить перегрузку
 конструктора класса (метод __init__()), который должен принимать
 данные (список списков) для формирования матрицы.
 Подсказка: матрица — система некоторых математических величин,
 расположенных в виде прямоугольной схемы.
 Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
 Следующий шаг — реализовать перегрузку метода __str__() для
 вывода матрицы в привычном виде.
 Далее реализовать перегрузку метода __add__() для реализации
 операции сложения двух объектов класса Matrix (двух матриц).
 Результатом сложения должна быть новая матрица.
 Подсказка: сложение элементов матриц выполнять
 поэлементно — первый элемент первой строки первой
 матрицы складываем с первым элементом первой строки
 второй матрицы и т.д.
 """


class Matrix:
    def __init__(self, values):
        self.values = values
        self.dimentions = (len(values), len(values[0]))

    def __str__(self):
        return str('\n'.join(['\t'.join(list(map(str, i))) for i in self.values]))

    def __add__(self, other):
        result = self.values
        for i in range(self.dimentions[0]):
            for j in range(other.dimentions[1]):
                result[i][j] = self.values[i][j] + other.values[i][j]
        return Matrix(result)


mtrx = Matrix([[1, 1, 0], [2, 17, 113], [50, 14, -8]])
print(mtrx)
print()
m1 = Matrix([[1, 1, 0]])
m2 = Matrix([[2, 17, 113]])
print(m1 + m2)
print()

m3 = Matrix([[1, 1, 0], [2, 17, 113], [50, 14, -8]])
m4 = Matrix([[-1, -1, 0], [2, 17, 113], [-50, -14, 8]])
print(m3 + m4)
