# Modify the timedcalls(n, fn, *args) function so that it calls 
# fn(*args) repeatedly. It should call fn n times if n is an integer
# and up to n seconds if n is a floating point number.

import time

def test():
    return "pass"

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.perf_counter() # in the course, it uses time.clock()
    result = fn(*args)
    t1 = time.perf_counter()
    return t1-t0, result

print(timedcall(test))

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

"""
version 1: typr error
def timedcalls(n, fn, *args):
    "Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"
    # Your code here.
    times = []
    for i in range(n):
        t0 = time.perf_counter()
        fn(*args)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return times, min(times), average(times), max(times)
"""

'''
#version 2: pass the test

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # !!range() input has to be integer
    # if n is a float --> will run the function continously until 
    # the total running time reaches n seconds
    # Your code here.
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)
'''

# version 3: pass the test
def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # !!range() input has to be integer
    # if n is a float --> will run the function continuously until 
    # the total running time reaches n seconds
    # Your code here.
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        time_now = time.perf_counter()
        while time.perf_counter() < time_now + n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)

# example: run the function repeatedly in 1 second
def print_1s():
    time_now = time.perf_counter()
    while time.perf_counter() < time_now + 1:
        pass
    print("Delay took", time.perf_counter() - time_now, "s")