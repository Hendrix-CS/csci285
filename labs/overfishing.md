---
layout: work
type: Lab
num: 6
worktitle: Overfishing
---

## Overview

The reproduction rate of fish populations is being outpaced by our appetites and [fishing abilities](https://en.wikipedia.org/wiki/World_fisheries_production). Without moderation and
[attention to the aquatic ecosystem](https://en.wikipedia.org/wiki/Population_dynamics_of_fisheries), through
[overfishing](https://www.worldwildlife.org/threats/overfishing)
we could easy end up in a world without fish.
To make our models feasible, we will be simplifying the situation a bit.

### Step 1

Create a Monte Carlo simulation of two large and two small fishing companies competing for [whitefish](https://en.wikipedia.org/wiki/Coregonus) in the
[Great Lakes](https://en.wikipedia.org/wiki/Great_Lakes). Every year, each large company catches on average 150,000 fish, with a standard deviation of 50,000. Each small company catches on average 60,000 fish, with a standard deviation of 20,000.

The lakes in which the companies are fishing can only support two million fish. Every year, the fish that remain after fishing will reproduce at an average rate of 25% with a standard deviation of 5%, rounded to the nearest whole number without going over two million. For instance, if there are 1.2 million fish, they are expected to grow to 1.5 million for the next year. If there are 1.9 million, they will grow to two million.

Run 100 trials of this simulation, and create a cumulative graph of all experiments showing the total population of the fish in the lake over time for the next 50 years.

What is the average length of time before the fish population in the lake reaches zero?

### Step 2

The local Fish and Wildlife Department wants to regulate the number of fish a company can catch each year, creating an upper bound somewhere between 100,000 and 200,000. Revise your model above to explore the impact of such a regulation.

What would you recommend as a good number for this regulation that will balance a sustainable ecosystem with the interests of the fishing companies?

Back up your decision with graphs and analysis.

### Step 3

The values above for the number of fish in the Great Lakes, the average number of fishing caught, the number of fishing companies, etc, are all very, very rough and incorrect estimates.

Research the actual fishing situation in Michigan by reading about the [current commercial fishing industry](https://www.bridgemi.com/michigan-environment-watch/commercial-fishing-sinking-fast-michigan-time-more-regulations), the [state commercial fishing regulations](https://www.michigan.gov/dnr/0,4570,7-350-79136_79236_80538_80541---,00.html), and a [history of commercial fishing in Michigan](https://www.michigan.gov/dnr/0,4570,7-350-79136_79236_80538_80541-424724--,00.html).

What are some of the largest errors in the numerical estimates used above? Decide on your own estimates and rerun the simulation above to provide a more accurate picture.

### Step 4

Discuss one structural simplification we made in our simulation above, such as ignoring tribal fishing allowances, or the zebra muscle invasion.

Develop a way to align your model more closely with the actual situation of fish population dynamics. Run your new simulation and report on your results.

## Grading

* 10 points for creating the initial model described in step 1.
* 5 points for determining an appropriate threshold in step 2.
* 5 points for revising the numerical estimates through step 3.
* 10 points for augmenting your model in step 4 with your own extension.
* 10 points for well-written explanations of your models and research,
and discussion of each graph throughout.
