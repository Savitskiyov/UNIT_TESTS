from abc import ABC, abstractmethod


class Vehicle(ABC):
    company = ''
    model = ''
    year_release = 0
    num_wheels = 0
    speed = 0

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass


class Car(Vehicle):
    def __init__(self, company: str, model: str, year_release: int):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = 4
        self.speed = 0

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

    def __str__(self):
        return f'{self.company}, {self.model}, {self.year_release}, {self.num_wheels}, {self.speed}'


class Motorcycle(Vehicle):
    def __init__(self, company: str, model: str, year_release: int):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = 2
        self.speed = 0

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def __str__(self):
        return f'{self.company}, {self.model}, {self.year_release}, {self.num_wheels}, {self.speed}'


if __name__ == '__main__':
    car = Car('Lexus', 'RX300', 2002)
    print(car)
    car.test_drive()
    print(car)
    car.park()
    print(car)

    motorcycle = Motorcycle('Harley-Davidson', 'Breakout', 2023)
    print(motorcycle)
    motorcycle.test_drive()
    print(motorcycle)
    motorcycle.park()
    print(motorcycle)