dicto=dict()
size=int(input("enter the size of dictionary :"))
for i in range(size):
    key=input(f"enter the key {i+1} : ")
    value=input("enter the value : ")
    dicto[key]=value
keys=list(dicto.keys())
print("----Before sorting----")
print(dicto)
print("----After sorting----")
keys.sort()
asc_dicto={key:dicto[key] for key in keys}
keys.sort(reverse=1)
dsc_dicto={key:dicto[key] for key in keys}
print(asc_dicto)
print(dsc_dicto)