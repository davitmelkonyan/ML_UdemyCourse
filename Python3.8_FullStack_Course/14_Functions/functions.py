

def my_function():
    test = 1 # this is defined in the local scope of the function
    print('my_function:', test)
test = 0 # this is defined in the global scope
my_function()
print('global:', test)


#Argument passing
x = 3
def func(y):
    print(y)
func(x) # prints: 3

#Assignment to argument names do not affect the caller
x = 3
def func(x):
    x = 7 # defining a local x, not changing the global one
    print(x)
func(x)
print(x) # prints: 3

#However Changing a mutable affects the caller!
x = [1, 2, 3]
def func(x):
    x[1] = 42 # this affects the caller!
func(x)
print(x) # prints: [1, 42, 3]


#######################################   5. Ways to input parameters##############################

#Positional arguments

def func(a, b, c):
    print(a, b, c)
func(1, 2, 3) # prints: 1 2 3

#Keyword arguments are assigned by keyword using the name=value syntax.

def func(a, b, c):
    print(a, b, c)
func(a=1, c=2, b=3) # prints: 1 3 2

#Default values
def func(a, b=4, c=88):
    print(a, b, c)
func(1) # prints: 1 4 88
func(b=5, a=7, c=9) # prints: 7 5 9
func(42, c=9) # prints: 42 4 9


#Variable positional arguments numeric
def minimum(*n):
    # print(n) # n is a tuple
    if n: # explained after the code
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)
minimum(1, 3, -7, 9) # n = (1, 3, -7, 9) - prints: -7
minimum() # n = () - prints: nothing


#Variable keyword arguments
def func(**kwargs):
    print(kwargs)
# All calls equivalent. They print: {'a': 1, 'b': 42}
func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))

#Keyword-only arguments
def kwo(*a, c):
    print(a, c)

kwo(1, 2, 3, c=7) # prints: (1, 2, 3) 7
kwo(c=4) # prints: () 4
# kwo(1, 2) # breaks, invalid syntax, with the following error
# TypeError: kwo() missing 1 required keyword-only argument: 'c'
def kwo2(a, b=42, *, c):
    print(a, b, c)
kwo2(3, b=7, c=99) # prints: 3 7 99
kwo2(3, c=13) # prints: 3 42 13
# kwo2(3, 23) # breaks, invalid syntax, with the following error
# TypeError: kwo2() missing 1 required keyword-only argument: 'c'


#REMEMBER
#Functions should do one thing
#Functions should be small
#The fewer input parameters, the better
#Functions should be consistent in their return values
#Functions shouldn't have side effects:























def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

print("first", "second", 3, 4, "spam")
