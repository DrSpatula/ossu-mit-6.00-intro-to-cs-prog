# Lecture 25: Queuing Network Models

## Queuing Simulations
* Systems where waiting plays a central role
* Queuing makes sense economically when resources are limited
	* Having "enough" servers to eliminate waits would often leave resources idle for an unacceptable amount of time
* Aim for an optimal balance between customer service and resource utilization
	* Excess resources capacity needed to handle occasional bursts of jobs

## Queue Model
1. Jobs enter the system
2. Jobs wait in the queue
3. Jobs leave the queue and enter a server for processing
4. Once processed, jobs leave the system

## Arrival Process
* How do jobs arrive? Singly or in batches?
* What is their time distribution?
	* Is it uniform or random?
	* Typically modeled using the inter-arrival time distance
	* Typically a Poisson Process distribution
		* Random but exponential
		* More towards the beginning

## Service Mechanism
* How long does service take?
	* Service time distribution depends on:
        * Amount of time to process a job
        * The speed of the server
* How many servers?
* How many queues? One for all servers, or one per server?
	* Single queue for all servers is the better solution, but there is not always enough space (memory) to implement
* Is preemption allowed?  Can a higher priority job interrupt one of lower priority?

## Queue Characteristics
* Policy: How is the next customer chosen?
	* **FIFO:** first in, first out
	* **LIFO:** last in, first out
	* **SRPT:** shortest remaining processing time
* Policy choice has **BIG** effect on performance and the correct choice can reduce queue congestion
* Also referred to as a "queue discipline"

## Questions/Metrics to Use When Evaluating
1. Average wait time
2. Is the wait time bounded? Is there a maximum wait?
3. Average queue length
4. Is the queue length bounded?
5. Server utilization: What is the amount of time a server is fully occupied?

## SRPT Discipline
* Typically gives the shortest average wait time
* Typically gives the shortest queue length
* **NOT A _FAIR_ DISCIPLINE**
* Allows starvation-- jobs with long processing time can wait forever