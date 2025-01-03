class Cuboid:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def area(self):
        area=2*(self.l*self.b+self.b*self.h+self.h*self.l)
        return area
    def perimeter(self):
        peri=4*(self.l+self.b+self.h)
        return peri