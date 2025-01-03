class rectangle:
    def __init__(self,length,breadth):
        self.__l=length
        self.__b=breadth
    def area(self):
        area=self.__l*self.__b
        print("Area = ",area)
        return area
    def perimeter(self):
        peri=2*(self.__l+self.__b)
        print("Perimeter = ",peri)
        return peri
    def __lt__(self,other):
        if self.area()<other.area():
            return True
        else:
            return False
l,b=map(int,input("enter the length and breadth of first rectangle : ").split())
r1=rectangle(l,b)
l,b=map(int,input("enter the length and breadth of second rectangle : ").split())
r2=rectangle(l,b)
print(r1.area(),r2.area())
print(r1.perimeter(),r2.perimeter())
if r1<r2:
    print("r2 is larger")
else:
    print("r1 is larger")