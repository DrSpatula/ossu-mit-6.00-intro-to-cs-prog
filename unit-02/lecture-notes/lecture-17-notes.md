# Lecture 17: Curve Fitting

## A statistically sound conclusion _is not_ truth
* Assumes the simulation was modeled correctly
* Assumes the simulation was constructed without errors
* Results need to be tested against reality
* Sanity checks are necessary
* Are results plausible

## Experimentation generally moves through the following:
1. Observation of physical reality
2. Theoretical modeling 
3. Computational modeling

## Experimental Error
* Occurs in all experiments
* Data will be randomly perturbed by errors
* Errors tend to be normally distributed
* Fitting a line or curve to a set of datapoints is a way to "correct" for error

## Best Fit
* Line or curve drawn closest to all datapoints on a plot
* Accuracy of the fit determined using an _objective function_
    * A function that returns a judgement of the fit
    * _Least squares fit_ is usually used
    * Found using the _mean square error_
    	* sum of the squares of the difference between each observed datapoint and its corresponding predicted datapoint
    	* squaring the difference removes whether the point is above or below the fit line
* The fit line gives predicted values
* Minimizing the mean square error gives best fit

## `polyfit` Function in PyLab
* Calculates least squares fit in python
* Takes observed _x_ and _y_ values and the degree of the polynomial describing the fit line
* Returns a tuple of the polynomial's coefficients

## Linear Regression
* Method PyLab uses to fit lines
* Can be used to find polynomials other than just lines

## How is the accuracy of a fit measured?
* There is no upper bound on the mean square error value
* Uses the _coefficient of determination_, R<sup>2</sup>
	* Value is always between 0 and 1
	* Calculated as 1 - (Estimated Error / Measured Variance)
    * Estimated error is the sum of the squares of the difference between the estimated datapoints and the corresponding measured datapoint
    * Measured variance is the sum of the squares of the differences between the measured mean and each measured datapoint