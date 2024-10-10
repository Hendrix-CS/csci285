---
layout: work
type: Lab
num: 5
worktitle: Predicting the mid-term elections
---

## Description

The 2024 elections are upon us. These elections are taking place now and will culminate on election day, which is November 5th. To get a sense of the will of the electorate, and predict what news we might wake up to on November 5th, organizations (such as [Hendrix](https://www.hendrix.edu/news/news.aspx?id=86521)) conduct polls where they ask randomly selected likely voters for their choice in the upcoming election. These organizations then use statistics to show how their sample of the population is representative of the whole state. Others, such as [FiveThirtyEight](https://fivethirtyeight.com/), can then attempt to determine the winner of the election using these polls and performing Monte Carlo simulations.


## Step 1: Download polling data

Download the zip file of the [polling data](https://projects.fivethirtyeight.com/polls/senate/2024/) collected by FiveThirtyEight, located at the bottom of this page, with the relevant polls recorded in `senate_polls.csv`. This file holds all the senate polls for each state from the last two years. Load this file up in a Kaggle notebook as a Pandas DataFrame. Examine its shape and features and produce a data dictionary explaining the most important columns and what a row of data represents. 


## Step 2: Preparing the polling data for analysis

Our goal is to predict the probability that Democrats will win or lose [key swing states](https://www.cookpolitical.com/ratings/senate-race-ratings) and retain (or lose) control of the Senate after the November 5th mid-term elections. We will look at the following races which are LEAN D, TOSS UP, or LEAN R (incumbent Senators are in all caps):

* Arizona (Ruben Gallego (D) vs. Kari Lake (R))
* Nevada (JACKY ROSEN (D) vs. Sam Brown (R))
* Pennsylvania (BOB CASEY JR. (D) vs. Dave McCormick (R))
* Michigan (Elissa Slotkin (D) vs. Mike Rogers (R))
* Ohio (SHERROD BROWN (D) vs. Bernie Moreno (R))
* Wisconsin (TAMMY BALDWIN (D) vs. Eric Hovde (R))
* Montana (JOHN TESTER (D) vs. Tim Sheehy (R))
* Texas (Colin Allred (D) vs. TED CRUZ (R))

 _For our first assumption_, we will only use the most recent poll for each state. Format the `created_at` column of the polling DataFrame as a **datetime** and then select only the poll with the latest value for each `state`. If there are multiple polls entered on the same date, select the one with the larger `sample_size`.

In these polls, we will need the data in the `sample_size`, `party`, and `pct` columns. The `sample_size` is how many people were surveyed in this poll, the `party` lists the choice offered (Note: `answer` is actually the choice offered, but since we are rolling this up to political parties it makes sense to work with the `party` column), and the `pct` is the percent of people who selected this choice. Divide the value in `pct` by 100, so it is a number between 0 and 1.

These choices don’t always add up to 100%, some small percentage of voters remain undecided or unwilling to offer their choice, and there are small margins for Libertarian, Green, and other party candidates. _For our second assumption_, to help determine the plurality winner for each state, we will say that people are either voting DEM, or voting against DEM. Therefore, we can select only those rows with the `party` equal to DEM.

_For our third assumption_, we will say that all other Senate races besides the 8 listed above, in the SOLID or LIKELY categories, will be won as predicted by the Cook Report. 

## Step 3: Generating probability distributions

Polls based on a sample of the whole population include a _margin of error_. To determine if DEMs will win a particular state, we will generate a random number using a normal distribution, with a mean of `pct` for that state’s poll. To account for the margin of error, we will use the following formula to calculate the standard deviation for the poll, which is based on the `sample_size` for that state.


```
stdv = 1 / (2 * math.sqrt(sample_size))
```


## Step 4: Simulation

We now have enough data to simulate the elections. For each seat, generate a percentage of voters choosing DEM. If this generated value is greater than 0.5, then award the seat to the Democrats. Run the election simulation 40,000 times and collect the results of each simulation. 

Plot the (binary) outcomes (e.g. "won" or "lost") for each state using a bar chart.


## Step 5: Conclusion

Using the results of your Monte Carlo simulations, clearly state your predicted 2024 mid-term election outcomes for each state, and for the Senate as a whole. Will the Democrats maintain control of the U.S. Senate? How closely do your results match the [Consensus Forecast](https://www.270towin.com/2024-senate-election/consensus-2024-senate-forecast) at 270toWIN? What could explain any differences you see? What other assumptions did we implicitly make in our simulation?


## What To Turn In

As you work on this lab, record all of your progress in a Jupyter notebook. Record your solutions and attempts in `Code` blocks, and annotate what you did with `MarkDown` blocks. Cite all the webpages you find and use in your search for your solution. A good solution should read like a self-contained report.

* Add your name and your lab partner at the top of the notebook. 
* [https://dillinger.io/](https://dillinger.io/) for good `MarkDown` styling.
* [Overleaf](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) for good `LaTeX` styling.
* Go to the file menu and do "Kernel -> Restart and Run All" before submitting. This ensures there are no runtime errors and all figures are generated correctly.


## Grading

* Complete: Notebook can be read easily w/o needing to reference this page for additional detail. It should read like a self-contained report. It can be executed without producing runtime errors. All steps (1-5) are finished and all discussion questions are answered.

* Partially complete: Notebook can be executed without producing runtime errors. Steps (1-5) are attempted.

* Bonus: If you complete the lab before the mid-terms on November 8th, then you can get 15 additional points added to your Exam #2 grade. this is enough to turn a "B" into an "A".
