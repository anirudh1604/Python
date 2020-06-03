import itertools 
input1=int(input())
input2=int(input())
input3 = [int(i) for i in input().split()]

lst=list(itertools.combinations(input3,input2))

lst2=[]

for j in lst :
    lst2.append(sum(j))

a=max(lst2)


for j in lst :
    if (sum(j)==a):
        print(min(j))
        