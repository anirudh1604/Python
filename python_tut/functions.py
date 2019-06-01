global_var="This is global variable"

def func(n) :
    if (n==1) :
        return 1
    return (n*func(n-1))

print(func(5))

def func2 (n) :
    if (n==1) :
        return 1
    return (n*func(n-1))


print(func2(6))

def func4():
    x=21
    print(x)


x=20

def func3 () :
    local_var = "This is local"
    print (local_var)
    print(global_var)
    x=21
    print(x)
    
print(x)
print(global_var)
func3()
print(global_var)
lst=[]
func4()
dir(lst)