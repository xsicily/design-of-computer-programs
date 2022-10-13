# Modify the timedcalls(n, fn, *args) function so that it calls 
# fn(*args) repeatedly. It should call fn n times if n is an integer
# and up to n seconds if n is a floating point number.

import time

def test():
    return "pass"

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.perf_counter()
    result = fn(*args)
    t1 = time.perf_counter()
    return t1-t0, result

print(timedcall(test))

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

"""
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

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # !!range() input has to be integer
    # Your code here.
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        
    return min(times), average(times), max(times)