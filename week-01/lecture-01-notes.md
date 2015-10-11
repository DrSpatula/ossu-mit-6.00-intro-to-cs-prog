# Lecture 1: Introduction to 6.0

## What is computation?
### Two types of knowledge:
* Declarative
* Imperative

### Declarative Knowledge
* Statements of fact
* _What_ something is
* Definition or axiom
* Can be used as testing criteria

### Imperative Knowledge
* _How_ to deduce something
* A recipe
* Description of a set of steps
	* Sequence of specific instructions done in order
	* Includes tests that can change order
	* End test that determines the end and answer

**_Computation is about capturing imparative processes_**


## How to mechanically capture an imperative process?

### Fixed program computers
* Piece of circuitry designed to do a specific computation
	* Calculator
	* Turing's Bombe (Enigma codebreaker)

### Stored program computer
* Machine that can take a series of steps and "reconfigure" itself to execute those steps
* An interpreter

**_A program is a recipe for a stored program computer_**

## Programs
* Built from a straightforward set of _primitives_
* Given a fixed set of the right primitives, anything can be programmed
	* Turing showed only 6 were needed
	* Anything done in one language can be done in another (Turing compatibilty)


## Dimensions of a Language
### High Level vs. Low Level
* **Low Level:** deals more directly with the underlying machine, smaller set of primitives, less "built-into" the language
* **High Level:** much richer set of primitives, more built-ins

### General vs. Targeted
How wide a variety of applications does the language support the creation of

### Interpreted vs. Compiled
* **Interpreted:** Interpreter is operating directly on the source code at runtime
	* Easier to debug
* **Compiled:** Source code is transformed into object code.  The process checks for errors and creates more efficient code to run.
	* Often runs faster

**_Python is a high-level, general, interpreted language_**


## Syntax vs. Semantics
### Syntax
* What are the legal expressions in a particular language?
* "cat dog boy"
	* Just a set of words, not a sentance
	* Wrong syntax
* Python will check syntax

### Static Semantics
* Which expressions are meaningful
* "My desk is Susan"
	* Syntactically correct
	* No semantic meaning
* Errors show primarily at runtime

### Full Semantics
* What happens when the program is run
* What is the meaning of the expression
* Most difficult to debug