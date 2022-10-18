# Design-of-computer-programs

This repository keeps study records of Udacity CS212 course "Design of computer programs" (https://www.udacity.com/course/design-of-computer-programs--cs212) to move along the path towards becoming an expert programmer! 

## Course content
### Lesson 1: Winning poker hand
- Write a poker problem: define the problem, write the specs and design the code
    - Shuffle
    - List comprehensions
- Problem sets: 7-card study and wild card
- Code design principle: correctness, efficiency, elegance
    
### Lesson 2: Back of the envelop
- [Zebra puzzle](https://en.wikipedia.org/wiki/Zebra_Puzzle)
    - Summary: conceptualize the inventory, refine the idea, simple implementation, back envelop (simple calculation), refine the code
    - Python: List comprehensions, generator, time measurement, star args, aspects (correct, efficient, debugging)
    - Goal: clean code
- Cryptarithmetic problem
    - Problem example: ODD + ODD = EVEN. The alphabets can be replaced by any possible digits (0-9) to get the result arithmetically correct.
        - Design: all the rules of arithmetic. Complexity-->short design.
        - Concepts to representations
        - Handling special case: the numbers starting with 0
        - Tracking the running time to find the possible way to speed up
        - Refactoring the code
    - Python: 
        - List comprehensions
        - generator
        - time measurement
        - eval()
        - Lambda function
        - itertools.permutation()
        - str.maketrans(), translate
        - string format
- Problem sets: 
    - no zero leading
    - floor puzzle
    - subpalindrome_slice
