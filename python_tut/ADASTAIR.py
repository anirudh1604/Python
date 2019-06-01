from sys import stdin,stdout
from functools import reduce
count =0
def count_Steps(x,y) :
    x=int (x)
    y=int (b)
    if (x+b<y) :
        count=count+1
        return count
    else :
        return y
b=0
for _ in range (int(input())) :
    a,b=stdin.readline().split()
    a=int (a)
    b=int (b)
    lst=[]
    count=0
    lst.extend(stdin.readline().split())
    count =reduce(count_Steps,lst)
    print(count)


