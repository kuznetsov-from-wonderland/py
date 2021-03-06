"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

mass = 25  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
height = 5  # число см толщины полотна


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return self._width * self._length * mass * height


road = Road(length=5000, width=20)
required_kr = (road.calc() / 1000)
print("{0:.0f} т".format(required_kr))
