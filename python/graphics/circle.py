import math
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        area=math.pi*self.r*self.r
        return area
    def perimeter(self):
        peri=2*math.pi*self.r
        return peri