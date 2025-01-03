sentence=input("enter the string : ")
ch=input("enter the letter : ")
num=0
for i in range(0,len(sentence)):
    if sentence[i]==ch:
        num=num+1
print(num)
