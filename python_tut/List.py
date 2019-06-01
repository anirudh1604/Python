list1 =[[1,2],3,4,[5,6]]
print (len(list1))
print (list1[1])
print (list1[0])
print (len(list1[0]))
list1.remove([1,2])
#print(list1)
try :
    list1.remove([1,2])
    print(list1)
except Exception  :
    print(list1)



lst2=['one','three','four','two','zero','thre1','Three','threa']
lst2=sorted(lst2)
print (lst2)

lst3=['one','three','four','two','zero','thre1','Three','threa']
lst3=sorted(lst3,reverse=True)
print (lst3)

abc=lst3
lst3.append('4')
print(abc)
abc.append('5')
print(lst3)

print("\n")

print(lst3[-1])

if lst3[-1] == lst3[9]:
    if lst3==abc :
        print ("hii")

lst_1=[1,2,3,4]
lst_2=['varma','brahma']

new_lst=lst_1+lst_2
print(new_lst)

x=4
n=x**3
print(n)


str="one,two,three"
lst_9=str.split(',')
print(lst_9)

str1=','.join(lst_9)
print(str1)



matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
transpose=[]
for i in range(4) :
    lst=[]
    for k in matrix :
        lst.append(k[i])
    transpose.append(lst)

print(transpose)


t=(1,2,3,6,5)
print(sorted(t))


s={1,2,3}
print(s)


lst_7=[1,2,3,1,3]
print(lst_7)
s1=set(lst_7)
print(s1)
s1.update({1,4,2,3})
print(s1)



my_dict={1:'satish','1':'anirudh'}
print(my_dict)
print(my_dict['1'])

#print(my_dict[2])


my_dict1=dict([(1,'abc'),('1','xyz')])

print(my_dict1)

print(my_dict1.get(2))
print(type(my_dict1.get(2)))

if (my_dict1.get(2)==None ):
    print ("Hii")
else :
    print("Hello")

my_dict1=my_dict1.fromkeys(['2',2,'3',3],'xxx') 
print(my_dict1) 

my_dict1[1]='abc'
print(my_dict1)

print(my_dict1.items())

print(dir(my_dict1))