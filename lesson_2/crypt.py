# -------------
# User Instructions
#
# Write a function, solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the 
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#


import string, re, itertools, time

# version 1
"""
def solve(formula):
    # Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    # Input formula is a string; output is a digit-filled-in string or None.
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
    # Generate all possible fillings-in of letters in formula with digits.
    # Example: 
    # formula = "ODD + ODD = EVEN"
    # letters = 'DOEVN'
    # '[A-Z]': only upper case
    # '[a-zA-z]': all the letters

    letters = ''.join(set(re.findall(r'[A-Z]', formula))) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):# permutations: combination without same numbers
        table = str.maketrans(letters, ''.join(digits)) # return the mapping table
        yield formula.translate(table) # replace characters

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
"""

#version 2 - faster solution
def solve(formula):
    """Input formula is a string;output is a digit-filled-in string or None.
    this version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula) #should be a string
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):# permutations: combination without same numbers
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str,digits))) 
                return formula.translate(table)
        except ArithmeticError:
            pass


# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.
#
# You can create strings and use %s inside that string which acts like a placeholder. 
# Then you can write % followed be the actual string value you want to use.
# E.g. print("Hi, my name is %s." % "Jessica")-->Hi, my name is Jessica.
#
# Python 3 introduced str.format() along with formatted string literals. 
# basic syntax: "template string {}".format(arguments)
# Inside the template string, we can use {} which act as placeholders for the arguments. 
# The arguments are values that will be displayed in the string. 
# E.g. print("Hi, my name is {}.".format("Jessica"))
#
# enumerate() method adds counter to an iterable and returns it. The returned object is an enumerate object.
# You can convert enumerate objects to list and tuple using list() and tuple() method respectively.
# E.g. grocery = ['bread', 'milk', 'butter']-->print(list(enumerateGrocery))-->
# [(0, 'bread'), (1, 'milk'), (2, 'butter')]
#
# reverse the string: word[::-1]. The slice statement [::-1] means start at the end of the string and 
# end at position 0, move with the step -1, negative one, which means one step backwards.
#
# another option: The reversed() function allows us to process the items in a sequence in reverse order. 
# It accepts a sequence and returns an iterator. A sequence list string, list, tuple etc.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    if word.isupper():
        # generate list of strings. e.g. ['1*U', '10*o', '100*Y']
        word_formed = ['{}*{}'.format(10**i, letter) for (i, letter) in enumerate(reversed(word))]
        return '(' + "+".join(word_formed) + ')' # output: '(1*U+10*O+100*Y)'
    else:
        return word

def compile_formula(formula, verbose=False):
    """
    Compile formula into a function. Also return letters found,
    as a str, in same order as parameters of function. For example,
    'YOU == ME**2' returns 
    (Lambda Y, M, E, U, O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO'
    lambda syntax-->lambda arguments : expression

    """
    letters = ''.join(set(re.findall(r'[A-Z]', formula))) # find all the letters with uppercase as one string
    letters_parse = ', '.join(letters) # separate one string (word) to separate letters
    tokens = map(compile_word, re.split('([A-Z]+)', formula)) # re.split('([A-Z]+)', formula))-->['YOU','==','ME','**2']
    body = ''.join(tokens) # body: '(1*U+10*O+100*Y) == (1*E+10*M)**2'
    f = 'lambda %s: %s' % (letters_parse, body) # f='lambda M, U, O, E, Y: (1*U+10*O+100*Y) == (1*E+10*M)**2'
    if verbose: print(f)
    # eval() input is expression: the string parsed and evaluated as a Python expression
    return eval(f), letters



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

