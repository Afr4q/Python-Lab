import math
class Sphere:
    def __init__(self,r):
        self.r=r
    def area(self):
        area=4*math.py*self.r*self.r
        return area
    def perimeter(self):
        peri=2*math.pi*self.r
        return peri