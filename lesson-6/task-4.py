"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)\
должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go!')
        if self.is_police:
            print(f"Is police 🚨: {self.is_police}")

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Turning {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f"{self.speed} ⚠️")
        else:
            print(self.speed)


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f"{self.speed} ⚠️")
        else:
            print(self.speed)


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(color=color, speed=speed, is_police=True, name=name)


car_1 = TownCar(name='Audi', speed=90, color='black', is_police=False)
car_1.go()
car_1.show_speed()
car_1.turn('left')
car_1.stop()

print()

car_2 = SportCar(name='Porsche', speed=200, color='red', is_police=False)
car_2.go()
car_2.show_speed()
car_2.turn('right')
car_2.stop()

print()

car_3 = WorkCar(name='Gazel', speed=50, color='gray', is_police=False)
car_3.go()
car_3.show_speed()
car_3.turn('around')
car_3.stop()

print()

police_car = PoliceCar(name='VW', speed=100, color='blue')

police_car.go()
police_car.show_speed()
police_car.turn('around')
police_car.stop()
