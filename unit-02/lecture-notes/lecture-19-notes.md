# Lecture 19: More Optimization and Clustering

## Machine Learning
* Code that learns to recognize complex patterns
* Uses _inductive inference_: making intelligent decisions based on available data
* Two approches: supervised and unsupervised learning

## Supervised Learning
* The training data has a label associated with each example
	* If the label is discrete, the program solves a classification problem
	* If the label is real-valued, the program solves a regression problem
* The trained program can then predict answers for other problems not observed
* The objective function should minimize training error, however _overfitting_ might not generalize well

### Questions:
* Are the labels accurate?
* Is past data representative of future data?
* Is enough data available to generalize?
* Feature extraction: which features label an example?
* How tight should the fit be?

## Unsupervised Learning
* Trainig data has no labels
* Used to learn about regularities of the data
* Clustering is the dominant form of unsupervised learning
	* Organizes data into groups with similar members (eg: groups of customers with similar purchases)
* Dissimilarity between data is modeled using variance
* Possible constraints:
	* Maximum number of clusters
	* Maximum distance between clusters

### Properties of Good Clustering
* Low _intra_-cluster dissimilarity
* High _inter_-cluser dissimilarity

### Two approaches:
1. **K-Means:** find the best _K_ number of clusters
2. **Hierarchial**

## Hierarchial Clustering

### Given:
* _N_ items
* _N_ x _N_ matrix of distances between items

### Agglomerative Clustering Algorithm
1. Assign each item to its own cluster
2. Find the most similar pairing and merge
3. Continue merging until there is only one cluster
4. Find the level of the hierarchy with the desired number of clusters

* Step two needs a metric of similarity, called _linkage criteria_
	* **Single Linkage:** the distance between two clusters is the shortest distance between any pair
	* **Complete Linkage:** the distance between two clusters is the furthest between any pair
	* **Average Linkage:** the average distance between all points

* Time consuming: at least O(_n_<sup>2</sup>) complexity
* Doesn't necessarily find the optimal solution
* Feature selection is **important**
* Define items in terms of a feature vector: `(feature1, feature2, feature3)` etc.