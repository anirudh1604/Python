def square(x) :
    return x*x


def  my_map(func,arg_list) :

    for i in arg_list:
        yield(func(i))
    
squares=my_map(square,[1,2,3,4,5])

for i in squares :
    print(i)