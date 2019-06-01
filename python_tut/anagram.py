#Write your code here

from sys import stdin,stdout

str1=[]
for _ in range(0,2) :
    str1.append(input().split())
print(str1[0],str1[1])
if (len(str1[0])== len(str1[1])) :
    if (str1[0]==str1[1]) :
        print ('True')
    else :
        if sorted(str1[0])==sorted(str1[1]) :
            print('True')
        else :
            print ('False')

else :
        print ('False')        