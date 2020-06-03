###custom map

import inspect

def my_map(func,lst) :
    for i in lst :
        yield(func(i))
def square(x):
    return (x*x)





res=my_map(square,[1,2,3,4,5])
for i in res:
    print(i)




####
lst=[1,3,5,7]
st="".join([str(i) for i in lst])
print(st)


print(inspect.getsource(my_map))

