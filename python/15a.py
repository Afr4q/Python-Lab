sentence=input("enter the string : ")
ch=input("enter the letter : ")
dicto=dict()
for i in range(0,len(sentence)):
    if sentence[i] not in dicto:
        dicto[sentence[i]]=1
    else:
        dicto[sentence[i]]+=1
print(dicto[ch])