a,b=map(int,input("enter two numbers : ").split())
for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break