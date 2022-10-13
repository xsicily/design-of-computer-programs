# ------------
# User Instructions
#
# The iterables are handy because you can read them as much as you wish, 
# but you store all the values in memory and this is not always what 
# you want when you have a lot of values.
#
# Generators are iterators, a kind of iterable you can only iterate over once. 
# Generators do not store all the values in memory, they generate the values on the fly.
# Generators only can be used once.
#
# yield will return a generator.
# When you call the function, the code you have written in the function body does not run.  
# The function only returns the generator object.

# Generator expression: g = (term for-clause option(for-if...))
# Output results: next(g)

# Example:

def sq(x):
    print ('sq called', x)
    return x * x
# generator:
g = (sq(x) for x in range(10) if x%2 == 0)
next(g)

for x2 in (sq(x) for x in range(10) if x%2 == 0): pass
list((sq(x) for x in range(10) if x%2 == 0))

# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

# generator function
def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1

"""
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
"""
# Test
L1 = ints(0, 10)
for i in L1:
    print(i) # output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

L1 = ints(1, 10)
for i in L1:
    print(-i)  # output: -1, -2, -3, -4, -5, -6, -7. -8, -9, -10


def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    i = 0
    while True:
        yield i
        i = i - 1
        yield -i