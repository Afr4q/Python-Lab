n=int(input('enter the number of terms : '))
a,b=0,1
print("Fibonacci series : ")
for i in range(0,n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
