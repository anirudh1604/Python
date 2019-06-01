def factors (n):
    for k in range (1,n+1) :
        if (n%k==0) :
            yield k


for factor in factors(100) :
    print(factor)
a,b,c,d=range(7,11)