n=int(input("enter the number : "))
for i in range(0,n):
    for j in range(0,i+1):
        print('*',end=" ")
    print("\n")
for i in range(n-1,0,-1):
    for j in range(0,i):
        print('*',end=" ")
    print("\n")
