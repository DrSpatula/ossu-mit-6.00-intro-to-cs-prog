# Lecture 7: Debugging

## Floating Point Numbers

### Binary Numbers
* Use only two digits, zero and one
* "Places" in a binary number represent increasing powers of two
* *n* binary digits can represent 2*^n^* numbers
* Whole numbers are trivial to represent in binary, fractions not so much

### Fractional Numbers in Binary
**In decimal form:** 0.125 = 1 \* 10<sup>-1</sup> + 2 \* 10<sup>-2</sup> + 5 \* 10<sup>-3</sup>

Because **0.125 = 1/8** and **1/8 = 2<sup>-3</sup>**, 0.125 in binary is 0.001
* "lucky" case, most fractional numbers have no exact binary representation
* there is no binary definition of the decimal number 0.1
	* infinite sequence
* Python uses approximations for binary fractions
	* Inaccurate, but it usually doesn matter

**Don't ever test the _equality_ of two floating point numbers.
Use a function that tests if they are _close enough_.**


## Debugging
### The aim of debugging is not to eliminate _one particular_ bug, but to _move towards_ a bug free program

**Debugging is a _search_ for the place where things went wrong**
* Be systematic when searching
* Use a technique equivalent to a binary search

**Ask: _How could the program have produced the incorrect output?_**

1. Study the available data
	* Text of the program
	* Results of tests
2. Form a hypothesis consistent with the data
3. Design and run a _repeatable_ experiment
	* Experiment should have the potential to disprove the hypothesis

**Testing tips:**
* Test with the smallest piece of input that produces the same bug
* Use a test harness: a piece of code that automates the test

### You never find _the_ bug, only _a_ bug.
