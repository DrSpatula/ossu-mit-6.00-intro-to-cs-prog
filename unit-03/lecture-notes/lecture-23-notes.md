# Lecture 23: Dynamic Programming

## Optimal Substructure
* Global solutions can be found by combining local solutions of sub-problems
* Examples:
	* Merge sort (does NOT have overlapping sub-problems, though)
	* Shortest path
		* Any sub path of the shortest path between two nodes is the shortest path between those sub-nodes

## Overlapping Sub-Problems
* To find the global solution, the same sub-problem would need to be solved multiple times
* Allows memoization

## 0/1 Knapsack Problem Revisited
* Its recursive solution can be solved using dynamic programming
	* Uses a depth first search of a decision tree
* **Optimal Substructure:** solution is made up of solutions to subsets of items
* **Overlapping Sub-Problems:** sub-solutions are stored using a tuple of the remaining items and the remaining weight as the key
* This **only** works if different selections of items can add up to the same weight

## Complexity/Runtime
* The calculation of new keys is the prime factor of complexity
* How complex is the algorithm that calculates a new key?
* The more overlap between sub-processes, the more efficient the global algorithm
* Said to be of _pseudo-polynomial_ complexity
	* Will generally run in polynomial time unless conditions are unfavorable (low overlap)