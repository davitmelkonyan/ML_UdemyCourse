s = 'Hello World'
s[0]
s[1]
s[2]

# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]

# Grab everything UP TO the 3rd index
s[:3]

#Everything
s[:]


# We can also use negative indexing to go backwards.
# Last letter (one index behind 0 so it loops back around)
s[-1]

# Grab everything but the last letter
s[:-1]


# We can also use index and slice notation to grab elements of a sequence by a
# specified step size (the default is 1). For instance we can use two colons in
# a row and then a number specifying the frequency to grab elements. For example:

# Grab everything, but go in steps size of 1
s[::1]

# Grab everything, but go in step sizes of 2
s[::2]

# We can use this to print a string backwards
s[::-1]


# ## String Properties
# Its important to note that strings have an important property known as
# immutability. This means that once a string is created, the elements within
# it can not be changed or replaced. For example:

s

# Let's try to change the first letter to 'x'
s[0] = 'x'


# Notice how the error tells us directly what we can't do,
# change the item assignment!
#
# Something we can do is concatenate strings!
s

# Concatenate strings!
s + ' concatenate me!'

# We can reassign s completely though!
s = s + ' concatenate me!'

print(s)

# We can use the multiplication symbol to create repetition!

letter = 'z'

letter*10


# ## Basic Built-in String methods
#
# Objects in Python usually have built-in methods. These methods are functions
# inside the object (we will learn about these in much more depth later) that
# can perform actions or commands on the object itself.
#
# We call methods with a period and then the method name. Methods are in the form:
#
# object.method(parameters)
#
# Where parameters are extra arguments we can pass into the method.
# Don't worry if the details don't make 100% sense right now. Later on we will
# be creating our own objects and functions!
#
# Here are some examples of built-in methods in strings:

# Upper Case a string
s.upper()

# Lower case
s.lower()

# Split a string by blank space (this is the default)
s.split()

# Split by a specific element (doesn't include the element that was split on)
s.split('W')

# There are many more methods than the ones covered here.

########################
### Print Formatting ###
########################

# We can use the .format() method to add formatted objects to printed string statements.
#
# The easiest way to show this is through an example:

'Insert another string with curly brackets: {}'.format('The inserted string')

# Using the string .format() method
# The best way to format objects into your strings for print statements is using
# the format method. The syntax is:
#
#  'String here {var1} then also {var2}'.format(var1='something1',var2='something2')
#
# Lets see some examples:


print('This is a string with an {p}'.format(p='insert'))

# Multiple times:
print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi!'))


# Several Objects:
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3))


# That is the basics of string formatting!
