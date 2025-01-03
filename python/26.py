size=int(input("enter the size of list : "))
color=[]
for i in range(size):
    clr=input(f"enter color {i+1} : ")
    color.append(clr)
print(color[0],color[-1])