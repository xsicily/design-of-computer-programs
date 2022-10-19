# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!
#
# palindrome: The characters read the same backward as forward. 
# e.g. racecar

# slow version: pass the test but not efficient
"""
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    orig_string = text.lower()
    # Find all the substrings
    result = []
    for i in range(len(orig_string)+1):
        for j in range(i+1, len(orig_string)+1):
            result.append(orig_string[i:j]) 
    # Find all the palidrome 
    palidrome = []
    for item in result:
        if item == item[::-1]:
            palidrome.append(item) 
    # Find the longest palidrome
    if len(palidrome) > 0:
        max_length = 0
        longest_pali = ''
        for pali in palidrome:
            if len(pali) > max_length:
                longest_pali = pali
                max_length = len(pali)
        # Find the index of the longest palidrome
        for i in range(len(text)):
            if orig_string[i:].startswith(longest_pali):
                return (i, i + len(longest_pali))
    else:
        return (0,0)
"""


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())