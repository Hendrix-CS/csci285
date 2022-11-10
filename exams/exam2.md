---
layout: work
type: Exam
num: 2
worktitle: System Dynamics & Monte Carlo Simulations
---

In this exam, you will demonstrate your mastery of CSCI 285 Module #2 concepts in two parts. Part #1 focuses on solving a system dynamics problem. Part #2 involves a Monte Carlo simulation.

<br />

# Part 1 - 75 points

The [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system) is a set of ordinary differential equations that, while deterministic in its representation, exhibits chaotic solutions under certain conditions. Applications of the Lorenz system has led to the popularization of the term "butterfly effect" (i.e. even the minor disturbance of butterfly wings could cause hurricanes to form on the other side of the world). 

Using Euler's method, solve and visualize the Lorenz system for x(t), y(t), and z(t) using line graphs, and produce "butterfly" phase portrait(s) by scatter plotting y(x), y(z), and x(z). For initial conditions, use σ = 10, β = 8/3, ρ = 28, x_0 = 2.0, y_0 = 5.0, and z_0 = 3.0. For the time range, you should choose n=30 (30 steps) to start. dt ~ 0.001. 

### Visualizations
Make sure that your axes are labeled and that you set a title for each chart. Increase the size and aspect ratio to improve visibility. 

### Variable Step Size
Vary the step size (n=1, n=5, n=10, n=50, etc.) and interpret the results. What do you observe in the phase portraits? What do you observe in the time series plots? What happens as n increases?

### Write-Up
While writing up your solution, use appropriate markdown stying and include the Lorenz system (and all of its initial conditions) written in LaTeX. Your solution should read like a report about the Lorenz system and points will be awarded for readibility and attention to detail. Cite your sources.

<br />

{% include warning.html content="If you cannot complete the simulation and want to forfeit the points, you can still get partial credit by producing some of the visualizations. Come see me for more detail." %}

<br />


# Part 2 - 75 points

The reproduction rate of fish populations is being outpaced by our appetites and [fishing abilities](https://en.wikipedia.org/wiki/World_fisheries_production). Without moderation and [attention to the aquatic ecosystem](https://en.wikipedia.org/wiki/Population_dynamics_of_fisheries), through [overfishing](https://www.worldwildlife.org/threats/overfishing) we could easy end up in a world without fish. To make our models feasible, we will be simplifying the situation a bit.

### Step 1

Create a Monte Carlo simulation of two large and two small fishing companies competing for [whitefish](https://en.wikipedia.org/wiki/Coregonus) in the [Great Lakes](https://en.wikipedia.org/wiki/Great_Lakes). Every year, each large company catches on average 150,000 fish, with a standard deviation of 50,000. Each small company catches on average 60,000 fish, with a standard deviation of 20,000.

The lakes in which the companies are fishing can only support two million fish. Every year, the fish that remain after fishing will reproduce at an average rate of 25% with a standard deviation of 5%, rounded to the nearest whole number without going over two million. For instance, if there are 1.2 million fish, they are expected to grow to 1.5 million for the next year. If there are 1.9 million, they will grow to two million.

Run 100 trials of this simulation, and create a cumulative graph of all experiments showing the total population of the fish in the lake over time for the next 50 years. You can assume that the starting population of fish is two million.

What is the average length of time before the fish population in the lake reaches zero?

### Step 2

The local Fish and Wildlife Department wants to regulate the number of fish a company can catch each year, creating an upper bound somewhere between 80,000 and 150,000. Revise your model above to explore the impact of such a regulation.

What would you recommend as a good number for this regulation that will balance a sustainable ecosystem with the interests of the fishing companies?

Back up your decision with graphs and analysis.

### Step 3

The values above for the number of fish in the Great Lakes, the average number of fishing caught, the number of fishing companies, etc, are all very, very rough and incorrect estimates.

Research the actual fishing situation in Michigan by reading about the [current commercial fishing industry](https://www.bridgemi.com/michigan-environment-watch/commercial-fishing-sinking-fast-michigan-time-more-regulations), the [state commercial fishing regulations](https://www.michigan.gov/dnr/0,4570,7-350-79136_79236_80538_80541---,00.html), and a [history of commercial fishing in Michigan](https://www.michigan.gov/dnr/0,4570,7-350-79136_79236_80538_80541-424724--,00.html).

What are some of the largest errors in the numerical estimates used above? Decide on your own estimates and rerun the simulation above to provide a more accurate picture.


### Visualizations
Make sure that your axes are labeled and that you set a title for each chart. Increase the size and aspect ratio to improve visibility. Produce visualizations that convince yourself (and me) that you have the correct solution to the above problem. 

### Write-Up
While writing up your solution, use appropriate markdown styling and any LaTeX you think is needed. Your solution should read like a report about overfishing on the Great Lakes and points will be awared for readibility and attention to detail. Cite your sources.


<br />

# What To Turn In

A Jupyter notebook that begins with the following statement, 

> All of the below work is my own. I adhered to the test-taking procedure by not receiving any help from my peers. I have cited all resources I found online or from notebooks shared from class that helped me complete this exam.

* Please print (sign) your name and date. 

* Please label each **Part** of the exam using markdown headers. 

* Turn in a zip file that contains your notebook and any data needed to run the notebook.

<br />

# Grading

* **Complete** - Earn (at least) 90% of the points.

* **Partially Complete** - Earn (at least) 70% of the points. 
