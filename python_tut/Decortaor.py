def ecorator_function(original_function)  :
    def wrapup_function():
        print('wrapper function executed before display')
        return original_function()
    return wrapup_function

@ecorator_function
def display() :
    print("Display")

display()