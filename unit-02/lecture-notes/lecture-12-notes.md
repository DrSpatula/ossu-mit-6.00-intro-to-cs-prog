# Lecture 12: Introduction to Simulation and Random Walks

## Yield Statement
* Used in a similar place to a return statement
* Creates a _generator_
    * A function that remembers the state where it last returned a value, including local variables
* Can be an alternative to stepping through a list 
* Gives more control over outside access to members of a collection

## Analytic Methods
* Aim to _predict_ the exact behavior of a system given inital conditions and a set of parameters
* Not always useful- too hard to build exact model of a given system

## Simulation Methods
* Easier to view intermediate results
* Refining a series of simulations can give better results than analytics

## Simulation
* Build a model that:
	* Gives useful information about the behaviour of a system
	* Gives an _approximation_ of reality
	* Is _descriptive_ instead of _prescriptive_
		* A good guess versus a definitive answer
		* Could give a different result for the same input
* Test calculations should be done to see what results to expect
	* Use to evaluate the accuracy of the simulation

## Random Walk
* A useful method of simulation
* A system in which its members make a movement at each timestep