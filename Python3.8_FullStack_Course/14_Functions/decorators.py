# Decorator - software design patterns that dynamically alter the functionality of a function, method, or
#             class without  directly using subclasses or changing the source code of the decorated function. 


# does nothing (can be used as a kind of code marker)
#decorator function takes a function as an argument, returns another function
def super_secret_function(f):
    return f
@super_secret_function    #same as -->  my_function = super_secret_function(my_function)
def my_function():
    print("This is my secret function.")

#############################################################

def print_args(func):#This is the decorator
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs) #Call the original function with its arguments
    return inner_func

@print_args #same as -->  multiply = print_args(multiply)
def multiply(num_a, num_b):
    return num_a * num_b
print(multiply(3, 5))
#Output:
# (3,5) - is  the 'args'  the function receives.
# {} -  is the 'kwargs'
# 15 - The result of the function.

#############################################################


#Decorator class          
class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Before the function call.')  
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res

@Decorator
def testfunc():
    print('Inside the function.')

testfunc()
# prints - Before the function call.
#          Inside the function.
#          After the function call.

