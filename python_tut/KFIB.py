n,k=map(int,input().split())
if (n<=k) :
    print (1)
else :
    L=[1]*k

    sum=k
    for i in range(n-k) :
        L.append(sum%1000000007)
        print(L)
        sum=sum-L.pop(0)
        print(sum)
        sum=(sum+L[-1])%1000000007
    ans=L[-1]%1000000007
print(ans)
