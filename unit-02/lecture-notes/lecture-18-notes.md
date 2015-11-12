# Lecture 18: Optimization Problems and Algorithms

## More on Curve Fitting
* If R<sup>2</sup> is 1, all data is explained perfectly by the model
* If R<sup>2</sup> is 0, there is no relationship between the model and data
* `polyfit` creates an analytical model of the data
	* Allows questions about the data to be answered

## Pattern of Computational Analysis
1. Start with an experiment
2. Use computation to find and evaluate the model
3. Use theory, analysis, and computation to derive the consequence of the model

## Optimization Problems
* Programs to find optimal solutions to problems
* Have two parts:
	1. An objective function to be minimized or maximized
	2. A set of constraints to be satisfied
* Often solved by means of _problem reduction_
	* Mapping the new problem onto a classic problem that has a solution
* Optimization programs are typically complex
	* Usually no efficient way to be solved
	* Often use approximate or "best effort" solutions

## Knapsack Problem
* Maximize the value of a set of items, constrained by a maximum carry weight
* Two variations:
	* 0/1 Knapsack: Items can either be taken or not taken
	* Continuous Knapsack: Some subquantity of an item can be taken (eg: rice, sand, etc)

## Greedy Algorithms
* Iterative
* The _locally_ optimal choice is made at each step
* What defines "locally optimal" must be determined
	* Most value vs. least weight
* Guaranteed to give an optimal solution for the continuous knapsack
* Will not necessarily give an optimal solution for 0/1
* Are typically efficient
	* O(_n_ log _n_), the complexity of sorting the items

## Straightforward (Brute Force) Algorithm
1. Enumerate all possible combinations of items
2. Choose the combination that best satisfies the constraints

* 2<sup>n</sup> possible combinations of items
* For 50 items, assuming 1 micorsecond of processing time per combination, it would take 36 years to find the optimal combination
* The knapsack problem is inherently of exponential complexity