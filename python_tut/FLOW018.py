'''import math
for _ in range(int(input())) :
    f=int(input())
    print(math.factorial(f))
'''

def factorial (n) :
    if (n==1) :
        return 1 
    return (n*factorial(n-1))

for _ in range(int(input())) :
    print(factorial(int(input())))


'''for _ in range(int(input())) :
    f=int(input())
    a=1
    while f!= 0 :
        a=a*f
        f=f-1
    print(a)
'''    

