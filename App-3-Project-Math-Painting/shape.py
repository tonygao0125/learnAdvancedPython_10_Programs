import numpy as np


class Rectangle:
    def __init__(self, x, y, height, width, color):
        self.color = color
        self.width = width
        self.height = height
        self.y = y
        self.x = x

        self.rectangle = np.zeros((height, width, 3), dtype= np.uint8)

    def draw(self, background):
        background.data[self.x: (self.x + self.height), self.y: (self.y + self.width)] = self.color


class Square:
    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, background):
        background.data[self.x: (self.x + self.side), self.y: (self.y + self.side)] = self.color