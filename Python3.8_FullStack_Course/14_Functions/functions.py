######  Input parameters (6 ways)

#1. Positional arguments
def func(a, b, c):
    print(a, b, c)
func(1, 2, 3) # prints: 1 2 3

#2. Keyword arguments are assigned by keyword using the name=value syntax.
def func(a, b, c):
    print(a, b, c)
func(a=1, c=2, b=3) # prints: 1 3 2 (i.e. doesn't matter where c is)

#3. Default vals
def func(a, b=4, c=88):
    print(a, b, c)
func(1) # 1 4 88
func(b=5, a=7, c=9) # 7 5 9
func(42, c=9) # 42 4 9

#4. Variable positional arguments numeric
def minimum(*n): #n is a tuple
    if n: 
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)
minimum(1, 3, -7, 9) # prints: -7
minimum() # prints: nothing

#5. Variable keyword arguments
def func(**kwargs):
    print(kwargs)

func(a=1, b=42)# All print: {'a': 1, 'b': 42}
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))

#6. Keyword-only arguments (new for py 3)
def kwo(*a, c):
    print(a, c)

kwo(1, 2, 3, c=7) # prints: (1, 2, 3) 7
kwo(c=4) # prints: () 4
# kwo(1, 2) # invalid syntax-> error: missing 1 required keyword-only argument: 'c'

def kwo2(a, b=42, *, c):
    print(a, b, c)
kwo2(3, b=7, c=99) # prints: 3 7 99
kwo2(3, c=13) # prints: 3 42 13
# kwo2(3, 23) # invalid syntax-> error: kwo2() missing 1 required keyword-only argument: 'c'

