from math import *
class Circle:
    radius = None
    def __init__(self, radius):
        self.radius = radius
    
    def get1(self):
        return pi * (self.radius ** 2)
    
    def get2(self):
        return 2 * pi * self.radius