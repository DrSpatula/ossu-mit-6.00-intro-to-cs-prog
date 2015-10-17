# Lecture 5: Objects in Python
## Structures for collecting data
* Tuples, lists, and dictionaries
* Tuples and lists are _ordered sequences_
	* can be indexed (from zero) or sliced
	* elements can be of different types (non-homogeneous)

### Tuples
* **Immutable** sequences
* Tuple of length one is written `(elem, )`

### Lists
* **Mutable** sequences
* Calling a list method (append, etc.) changes the list **in place**
* Concatenating two lists produces a new list containing elements of both operands (flattened)

### Definitions
* **++Assignment++: ** binds a name to an object
* **++Mutation++: ** changes the value of an object
* **++Alias++: ** multiple names bound to the same object

### Dictionaries
* Not ordered
* Not sequences
* Set of key/value pairs
* Keys can be any _immutable_ type