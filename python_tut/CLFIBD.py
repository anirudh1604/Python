from sys import stdin,stdout
for _ in range(int(stdin.readline().strip())) :
    lst=list(stdin.readline().strip())
    s =set(lst)
    freq=[lst.count(i) for i in s]
    freq=sorted(freq)
    print ('Dynamic' if (len(freq)< 3 or freq[-1] == (freq[-2]+freq[-3])) 
    else 'Not')
   