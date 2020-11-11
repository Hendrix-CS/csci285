---
layout: work
type: Lab
num: 8
worktitle: Optimization
---

## Overview

In this lab, you will create plots to better understand the local search
algorithms of gradient descent and simulated annealing, compare two implementations of evolutionary algorithm search, and extend the algorithm to solve a 3D problem.

### Step 1 - Local Search Plotting

#### Step 1.1 Plotting the internal details

* Create a Tour with 50 random points.
* Draw a plot of the cost of a tour over time using gradient descent, where each call to calculate the distance of a tour takes 1 unit of time.
* Draw a plot of the cost of a tour over time using simulated annealing, where each call to calculate the distance of a tour takes 1 unit of time.
* Draw a scatter plot of the probability of accepting a bad move over time using simulated annealing.

#### Step 1.2 Interchange neighborhood

* Extend the Tour object to include an "interchange" function. Similar to swap,
it will bring in an *i*th and *j*th city, and reverse the order of all cities
in between them, including the *i*th and *j*th city.
* Rerun the simulated annealing and gradient descent algorithms, using
the interchange neighborhood function. How do the results compare in terms of the quality of solutions found, and the time needed to find them? Be sure to show a plot of the tour, and the graphs create above.

### Step 2 - Evolutionary Algorithm Extensions

Implement one of the crossover techniques below and compare your results to the method presented in class.

* [Cycle Crossover](https://web.archive.org/web/20200216005128/http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/CycleCrossoverOperator.aspx)
* [Edge Recombination](https://web.archive.org/web/20200215110258/http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/EdgeRecombinationCrossoverOperator.aspx)
* [PMX Crossover](https://web.archive.org/web/20200216051820/http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/PMXCrossoverOperator.aspx)

### Step 3 - Interstellar Journey

You are planning a journey for a robotic probe to survey all of the
[closest stars](http://en.wikipedia.org/wiki/List_of_nearest_stars_and_brown_dwarfs).
Your probe will start at Earth, visit each star once, and return home.
Convert the distance, right ascension and declination for each
star to [cartesian coordinates](http://www.astronexus.com/node/37), then plan
out a close-to-optimal journey using one of the techniques we have learned in class.
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
* 10 points for Interstellar Journey code
