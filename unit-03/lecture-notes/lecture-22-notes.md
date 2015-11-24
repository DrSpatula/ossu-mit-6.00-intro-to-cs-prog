#Lecture 22: Using Graphs to Model Problems, Part 2

## Graph Problems
* **Shortest Path:** Find the shortest sequence of edges that connect two nodes
* **Shortest Weighted Path:** Find the lowest weighted path between two nodes
* **Cliques:** Find a set of nodes with a path connecting all its members
* **Minimum Cut:** Given two sets of nodes, find the minimum number of edges such that, if removed, the sets will be separated

## Recursive Depth First Search (DFS)
* Recursion ends when the starting node of a particular call is the destination node: `start == end`
* The recursion:
	* Choose one child of the current node and recur with the child node as the `start` of the new call
	* Repeat this until:
		* A node without children is reached
		* The destination node is reached
		* The child node has already been visited (this prevents infinite cycling)
	* If a "dead end" is reached, the recursion will "backtrack" and take the next child of the previous node
* This method will "solve" the same sub-paths multiple times, which is bad for performance
	* Can be mitigated with _dynamic programming_, aka _memoization_
		* Best solutions for sub-paths are stored in a lookup table
		* Table is checked for saved data before initiating a new recursive calculation
		* If found, saved answer is returned saving the time of re-processing the answer and significantly improving performance


## Dynamic Programming
* One of the most important algorithms in use today
* Can be used to find solutions to problems that would otherwise take too long to return a solution
* _**Memoization**_ is the key technique

### When to use Dynamic Programming
* The problem must have **optimal substructure**
	* A globally optimal solution can be found by combining locally optimal solutions
	* `A -> B + B -> C = A -> C`
* The problem must have **overlapping sub-problems**
	* Finding a solution involves solving the same sub-problem multiple times