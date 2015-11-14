# Lecture 21: Using Graphs to Model Problems, Part 1

## K-Means Clustering
* Usually run several times an the "best" result is used
	* Because the initial centroids are chosen at random, the results vary for each trial
	* "Best" is usually selected using a min/max metric
		* The smallest value of the largest distance between clusters


## Machine Learning Wrap-Up
* **Supervised Learning:** Infers the relationship between features and labels
* **Unsupervised Learning:** Inferst the relationshib between features themselves
* Be weary of overfitting, the training dataset may be too small or not representative of the population as a whole
	* M.L. resluts on sample won't relate/generalize to population
* _**FEATURES MATTER**_
	* _THE_ most important decision that will influence M.L. results

## Graph Theoretical Models
* **Graph:** A set of nodes (verticies) connected by a set of edges (arcs)
* If edges are one-way, the graph is called a _digraph_ (directed graph)
* Typically used where interesting relationships exist between parts of a system
* First use was Euler's solution to the Koningsburg bridges problem
* Edges can have an associated weight
	* Graph becomes a _weighted graph_
	* Weights can represent distance, cost, etc
* The WWW can be represented as a weighted digraph
* A graph is a specialization of a digraph

### Data Structures for Representing Graphs

#### Adjacency Matrix
* an _N x N_ matrix of nodes
	* for a weighted digraph, matrix entries are the edge weights
	* for a graph, entries are typically true or false values reperesenting whether or not those nodes are connected
* Multiple edges connecting nodes can make this representation complicated
	* Matrix entries would have to contain multiple values

#### Adjacency List
* Each list entry represents a node, with the sub-list entries represent edges eminating from that node