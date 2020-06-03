lst1=[{'a':0,'b':5},{'a':-1,'b':4},{'a':3,'b':1},{'a':0,'b':7}]

lst2=[]
for index,i in enumerate(lst1) :
    lst2.append((index,lst1[index].get('a')))


print("lst2={}".format(lst2))

lst2=sorted(lst2,key=lambda x : x[1])

print(lst2)

lst3=[]

for i in lst2 :
    lst3.append(lst1[i[0]])

print(lst3)