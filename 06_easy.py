# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала!'.format(self.name))

    def stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class SportCar(TownCar):
    # можно использовать pass
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)



class WorkCar(TownCar):
    # можно использовать pass
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)


class PoliceCar(TownCar):
    # можно использовать pass
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=True)


car1 = TownCar(100, 'red', 'Honda')


car2 = SportCar(100, 'red', 'Honda')
car2.turn('назад')



