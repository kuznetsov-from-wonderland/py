"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep

initial_color = 'r'
colors = {'r': '🔴 Red', 'g': '🟢 Green', 'y': '🟡 Yellow'}
seq = {'r': 'y', 'g': 'r', 'y': 'g'}
time_outs = {'r': 7, 'g': 9, 'y': 2}


class TrafficLight:
    color = initial_color

    def log(self):
        print(colors[self.color])

    def step(self):
        sleep(time_outs[self.color])
        next_color = seq[self.color]
        self.color = next_color

    def running(self):
        while True:
            self.log()
            self.step()


s = TrafficLight()
s.running()
