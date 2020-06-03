s="abc"
print(id(s))
s=s[::-1]
print(s)
print(id(s))


def add(x,y) :
    return x+y


def outer_func(f,x,y):
    if x>0 and y>0 :
         return f(x,y)


f=add
ou=outer_func(f,1,2)

print(ou)