
#####babbcd=====> a1b3c1d1

s1=list(input())
set1=set(s1)
dictionary={i:s1.count(i) for i in set1}
lst1=sorted(dictionary.keys())
lst2=[]
for i in lst1 :
    for j in dictionary :
        if j==i:
            lst2.append(i)
            lst2.append(str(dictionary.get(j)))

s1="".join(lst2)
print(s1)
