sentence=input("enter the sentence : ")
sentence=list(sentence)
sentence[0],sentence[-1]=sentence[-1],sentence[0]
sentence=''.join(sentence)
print(sentence)
