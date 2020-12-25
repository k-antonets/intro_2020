from abc import ABC


class Vehicle(ABC):
    _wheels = 4

    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        self.started = False

    @property
    def wheels(self):
        return self.__class__._wheels

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        if color != '' and color.startswith('#') and len(color) == 7:
            self._color = color

    def start_engine(self):
        print(self.model + ': Engine started')
        self.started = True

    @classmethod
    def get_wheels(cls):
        return cls._wheels

    @staticmethod
    def get_wheels():
        return Vehicle._wheels


class Car(Vehicle):

    def __init__(self, model: str, color: str, price: int):
        super().__init__(model, color)
        self.price = price

    def empty_func(self):
        pass


class Truck(Vehicle):
    _wheels = 6


