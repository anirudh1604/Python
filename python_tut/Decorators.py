def display():

    print("Hello Orginal Master")

def decorator_function(original_function):
    def wrapper_function () :
        print("Before Original Function")
        original_function()
        print("After Original Function")
    return wrapper_function

my_func=decorator_function(display)

my_func()