# -------------
# User Instructions
#
# Write a function, solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the 
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#
# Note that you will not be able to run your code yet since the 
# program is incomplete. Please SUBMIT to see if you are correct.

import string, re, itertools, time

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    # Your code here
    for f in fill_in(formula):
        if valid(f):
            return f # only return the first value

# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????. 
#
# note: The maketrans() method returns a mapping table that maps each 
# character in the given string to the character in the second 
# string at the same position. This mapping table is used with 
# the translate() method, which will replace characters as per 
# the mapping table.
#
# yield is only legal inside of a function definition, and the 
# inclusion of yield in a function definition makes it return a generator.

def fill_in(formula):
    """Generate all possible fillings-in of letters in formula with digits.
    Example: 
    formula = "ODD + ODD = EVEN"
    letters = 'DOEVN'
    '[A-Z]': only upper case
    '[a-zA-z]': all the letters
    """
    letters = ''.join(set(re.findall(r'[A-Z]', formula))) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):# permutations: combination without same numbers
        table = str.maketrans(letters, ''.join(digits)) # return the mapping table
        yield formula.translate(table) # replace characters

# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    
def valid(f):
    "Formula f is valid if it has no numbers with leading zero and evals true."
    # The eval() function evaluates the specified expression, if the expression 
    # is a legal Python statement, it will be executed.
    # unwanted results: the number in f starts with "0"
    # \b is used to represent word boundaries
    try:
        ## your code here.
        return not re.search(r'\b0[0-9]', f) and eval(f) == True    
    except ArithmeticError:
        # ArithmeticError is the upper level of zeroDivisionError
        ## your code here
        return False



def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.perf_counter() # in the course, it uses time.clock()
    result = fn(*args)
    t1 = time.perf_counter()
    return t1-t0, result
    
examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
ODD + ODD == EVEN
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
RAMN == R**3 + RM**3 == N**3 + RX**3
A**N + B**N == C**N and N > 1
sum(range(AA)) == BB
sum(range(POP)) == BOBO
PLUTO not in set([PLANETS])""".splitlines() 


def test():
    t0 = time.perf_counter()
    for example in examples:
        print(); print(13*'', example)
        print ('%6.4f sec:  %s ' % timedcall(solve, example))
    print('%6.4f tot.' % (time.perf_counter()-t0)) # print the total running time

print(test())

# tracking the time
"""
in terminal: python -m cProfile crypt.py

in python:
import cProfile
cProfile.run('test()')
"""

