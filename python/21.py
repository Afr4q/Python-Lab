class rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        area=self.l*self.b
        print("Area = ",area)
        return area
    def perimeter(self):
        peri=2*(self.l+self.b)
        print("Perimeter = ",peri)
        return peri
l,b=map(int,input("enter the length and breadth of first rectangle : ").split())
r1=rectangle(l,b)
l,b=map(int,input("enter the length and breadth of second rectangle : ").split())
r2=rectangle(l,b)
print(r1.area(),r2.area())
print(r1.perimeter(),r2.perimeter())
if r1.area()>r2.area():
    print("first rectangle is larger")
else:
    print("second rectangle is larger")