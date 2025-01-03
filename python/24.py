dict1=dict()
size1=int(input("enter the size of dictionary 1 :"))
for i in range(size1):
    key=input(f"enter the key {i+1} : ")
    value=input("enter the value : ")
    dict1[key]=value
dict2=dict()
size2=int(input("enter the size of dictionary 2 :"))
for i in range(size2):
    key=input(f"enter the key {i+1} : ")
    value=input("enter the value : ")
    dict1[key]=value
merg_dict=dict1|dict2
print(merg_dict)