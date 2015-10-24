# Lecure 9: Memory and Search Methods

##Linked Lists
* Each item in the list is an object containing a value and a pointer to the next item
* Finding the *i*th item is O(*i*)
    * Each item between L[0] and L[*i*] needs to be traversed

##Indirection
* Lists in Python contain pointers to each item instead of the items themselves
	* _Indirect_ access to list members
* Allows array-like access of heterogeneous data in constant time (O(1))

###Indirection is a _powerful_ technique

##Sorting
* A list cannot be sorted in sub-linear time as each element in the list must be examined
* The expense of sorting can be justified by the number of times the sorted data will be accessed/searched
	* **Amortized Complexity:** cost of sort divided amongst number of searches

##Selection Sort
* O(_n_<sup>2</sup>) complexity
* Depends on establishing and maintaining an _invariant_
	* **Invariant:** a condition that stays true throughout the algorithm

1. Divide the list into a prefix and suffix (prefix is initially empty)
2. The prefix will always be sorted (invariant)
3. Find the smallest element in the suffix
4. Swap that element into the prefix
5. Move the division between prefix and suffix to be after the new element
6. Repeat from step 3

##Elements of a Divide and Conquer Algorithm
1. Find the threshold input size (_n_<sub>0</sub>): the smallest possible sub-problem that can be directly solved without further division
2. Find the number of sub-problems in which to divide the input
3. Devise an algorithm to combine the sub-solutions

##Merge
* Two sorted lists can be merged quickly in O(_n_) (linear) time

1. Compare first items in each list
2. Append the smaller to the sorted list
3. Repeat with the remaining item and the next item from the other list

##Merge Sort Algorithm
1. Divide list into lists of length 1
2. Merge those into sorted lists of length 2
3. Continue merging until only one list remains

* Implementation is best done recursively
* Number of merges equal to log<sub>2</sub>(len(list))
* Order of merge sort is O(_n_ log _n_), where:
	* _n_ is the number of elements in the list
	* log _n_ is the number of merges