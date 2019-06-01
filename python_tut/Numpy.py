import numpy as np
a=np.arange(10)
print(a)
b=a[::2]
print(b)
print(np.shares_memory(a,b))
c=a[1::2]
print(np.shares_memory(a,c))
print(np.shares_memory(b,c))
a=np.arange(5)
print(np.sin(a))
#print(np.log(a))
d=np.array([[1,2,3],[0,1,5]])
print(d)
print(np.shape(d)) #Shape
print(np.ndim(d))#2D array
print(d.argmin())
e=np.zeros((50,50))
f=np.ones((30,35))
print(np.all(e!=0))
print(np.all(f!=0))
print(np.any(e!=0))
print(np.any(f!=0))
print(np.all(e==f))

y=np.array([1,3,5,7,9])
print(np.median(y))



l=np.tile(np.arange(0,40,10),(3,2))
print(l)


g=np.array([[[1,2,3],[3,4,5]],[[2,3,6],[3,7,8]]])
print(g)
print(g.ndim)
print("shape",g.shape)
print(g.ravel())
print("transposed",g.T)
print(g.T.ravel())






a=np.array([10,15,62,51])
print(a)
print(type(a))
#a=np.append(a,[5000])
b=np.append(a,np.array([500000000])) #saare element 500000000 itti space k bnenge
print(b)
print(type(b))
#b=np.arange(10)