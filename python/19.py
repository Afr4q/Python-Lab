str1=input("enter string 1 : ")
str2=input("enter string 2 : ")
str1,str2=list(str1),list(str2)
str1[0],str2[0]=str2[0],str1[0]
str1,str2=''.join(str1),''.join(str2)
print(str1+str2)

