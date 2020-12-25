from abc import ABC, abstractmethod


class Shape(ABC):
    edges = 0

    @abstractmethod
    def square(self):
        pass


class Rectangle(Shape):
    edges = 4

    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def square(self):
        return self.height * self.width


class Square(Rectangle):
    def __init__(self, color, width):
        super().__init__(color, width, width)


