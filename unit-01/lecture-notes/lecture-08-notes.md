# Lecture 8: Efficiency and Order of Growth

## Efficiency
* Getting programs to run fast enough to be useful
* Rarely about clever coding
* Usually about determining the correct alogrithm
* Reduce the problem to a version of a previously solved problem
* Measured in two dimensions:
	* Space (memory)
	* Time

## Time
* Not measured as execution time on a specific computer
	* Would depend on:
		* Speed of that particular machine
		* The efficiency of the languate implementation
		* The type and size of input
* Measured as a count of the number of basic steps 
	* Time is the size of the input mapped to the number of steps to process that input
	* A step takes a constant unit of time

## Random Access Machine (RAM) Model
* Conceptual computer model used in complexity analysis
* Executes steps of a program sequentially
* Memory access happens in constant time

## Which use case to analyze?
* **Best Case Complexity:** minimum time for all inputs
* **Worst Case Completxity:** maximum time for all inputs
* **Expected Case Complexity:** average time

#### Complexity analysis usually uses worst case
* Best case is too optimistic
* Expected case is too hard to define

#### Worst Case
* Provides upper bound on execution time, can't get longer
* Happens often

## Determining Complexity
* How does running time grow compared to growth in input?
* Refers to *asymptotic* growth
	* How is complexity affected as the limit of input size is approached

## Big "O" Notation
* O(*n*), pronnounced "order *n*", complexity grows linearly with growth of input *n*
* Always determine what *n* refers to

#### Common Complexity Types
* O(1) - Constant, algorithm takes the same time to complete regardless of input size
* O(*n*) - Linear
* O(log *n*) - Logarithmic
* O(*n* log *n*) - Log Linear
* O(*n*<sup>c</sup>) - Polynomial
* O(c<sup>*n*</sup>) - Exponential

### When analyzing:
* Determine what the algorithm is doing
* Start at the innermost loop and work outward
* Always define growth in term of the *inputs* of the algorithm