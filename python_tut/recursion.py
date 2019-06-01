import sys
a=1
def factorial (n) :
    global a
    if (n==1) :
        return  a 
    a =n*factorial(n-1)
    return a
   
#old=sys.getrecursionlimit()
#print(old)
#sys.setrecursionlimit(1000000) 
print(factorial (22750))
#sys.setrecursionlimit(old) 
