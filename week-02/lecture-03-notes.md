# Lecture 3: Problem Solving

## Decrementing Function
Code that determines when an iteration will finish.

**Has all of the following properties:**
* Maps a set of variables to an integer
* Starts with that integer non-negative
* When integer is <= 0, loop terminates
* It's value decreases every iteration of the loop

## Exhaustive Enumeration
* A type of "guess and check" algorithm
* Tests each possible value in the answer space
* Considered a "brute force" technique
	* Not ideal, but often good enough because computers are FAST

## Approximation
* Used to find an answer that's good enough
* The definition of "good enough" is the specification of the problem to be solved

## Bisection Search
An approximation algorithm where search space is halved upon each iteration

Works as follows:
* Determine a good upper and lower bound for the search space
* Make an initial guess that is halfway between the bounds
* Test if the guess is higher or lower than the needed result
* Discard the irrelevant half of the answer space by redefining the upper or lower bound
