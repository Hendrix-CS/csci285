---
layout: work
type: Lab
num: 8
worktitle: Optimization
---

## Overview

## Description

### Step 1 - TSP Extensions

* Create a Tour with 80 random points.
* Draw a plot of the cost of a tour over time using gradient descent.
* Draw a plot of the cost of a tour over time using simulated annealing.
* Draw a scatter plot of the probability of accepting a bad move over time using simulated annealing.
* Extend the Tour object to include an "interchange" function. Similar to swap,
it will bring in an *i*th and *j*th city, and reverse the order of all cities
in between them, including the *i*th and *j*th city.
* Rerun your simulated annealing algorithm and gradient descent algorithm above, using
the interchange neighborhood function. How do the results compare?

### Step 2 - GA Extensions

Implement one of the crossover techniques below and compare your results to the
method presented in class.

* [Cycle Crossover](http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/CycleCrossoverOperator.aspx)
* [Edge Recombination](http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/EdgeRecombinationCrossoverOperator.aspx)
* [PMX Crossover](http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/PMXCrossoverOperator.aspx)

### Step 3 - Interstellar Journey

You are planning a journey for a robotic probe to survey all of the
[closest stars](http://en.wikipedia.org/wiki/List_of_nearest_stars_and_brown_dwarfs).
Your probe will start at Earth, visit each star once, and return home.
Convert the distance, right ascension and declination for each
star to [cartesian coordinates](http://www.astronexus.com/node/37), then plan
out a close-to-optimal journey using the techniques we have learned in class.
Assume the probe can travel at half the speed of light.

Write a detailed lab report describing how you scraped
and cleaned the data, and the strengths/weaknesses of your selected search technique.
Be sure to state any other assumptions you need to make to solve this problem.
In your report, you should draw a
[3D plot](https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html) of your
resulting journey, and show how long this journey will take.

## Grading

* 10 points for well-written explanation of data provenance, discussion of each graph, and summary.
* 10 points for TSP Extensions code
* 10 points for GA Extensions code
* 10 points for Intertellar Journey code
