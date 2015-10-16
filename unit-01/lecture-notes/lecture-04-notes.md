# Lecture 4: Machine Interpretation of a Program

## Mechanisms provided by functions
### Decomposition
* Provides structure
* Creates modules of code
	* Self-contained
	* Reusable

### Abstraction
* Supresses detail
* Allows use of code as black boxes
	* Don't need to know _how_ the code in the function works
	* Facilitates easy re-use of code

## Functions
* Break code into coherent, reusable pieces
* Extend the language by adding new primitives
* Have three parts: name, parameters, body
* If named well, make code easier to read

### Scope
* A self contained set of mappings of names to objects.
* Each scope occupies a frame on the stack.

### Parameters
**Formal Parameter: ** A parameter that is part of a function definition
**Actual Parameter: ** The actual object passed to a function

**_The names of formal parameters are bound to the values of the actual parameters by the function call._**