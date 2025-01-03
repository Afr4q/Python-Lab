class Time:
    def __init__(self,hour,min,sec):
        self.h=hour
        self.m=min
        self.s=sec
    def __add__(self,other):
        