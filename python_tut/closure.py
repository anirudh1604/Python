def outer_func(msg) :
    message=msg
    def inner_func():

        print(msg,message)
    return inner_func

my_func = outer_func("hii")

print(my_func)
print(my_func.__name__)
my_func()
my_func()
my_func()