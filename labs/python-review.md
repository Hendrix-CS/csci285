---
layout: work
type: Lab
num: 1
worktitle: Python Review
---

## Overview

In this lab you will refresh your Python skills and become familiar
with installing Anaconda and Jupyter on your own machine.

## Materials

* [Puzzle Files](../assets/data/puzzle.zip)

## Description

    Let the missing be your order,
    Leaving out the one I drop.
    Bright has won while dim is zilching,
    Go around until you stop.
    Split the journey into thirds as keys
    For what had come before.
    Tragic end on island clifftop
    And in forty-four no more.

## What To Turn In

Write a program in Python that solves the riddle above, using the puzzle files provided.
Solving the puzzle by hand without evidence of coding will only be awarded minimal points.

As you work on this lab, record all of your progress in a Jupyter notebook, both
successes and failures. Record your solutions and
attempts in `Code` blocks, and annotate what you did with `MarkDown` blocks.
Cite all the webpages you find and use in your search for your solution.

{% include warning.html content="For this lab, you can collaborate with your team, but each member must turn in a
notebook that they created on their own machine, to ensure they have
installed and can use the tools needed to be successful the rest of the semester." %}

## Installing Anaconda

To analyze our data this semester, we will be using Anaconda and
Jupyter Notebooks, and hosting these on our own computers. What we will be
doing is usually too large for the free cloud-based notebooks like
Azure.

The [Anaconda Installation](https://docs.anaconda.com/anaconda/install/)
page lists many instructions for multiple operating systems. Follow the
instructions that make sense to you, choosing the Python 3.8 version.

### Open a Jupyter Notebook

Now we can test to see that everything is working. Follow
[these instructions](https://docs.anaconda.com/anaconda/install/verify-install/)
or mine below to get the `root` environment ready.

Then, type `jupyter notebook` and a browser window should appear.
From here, you can make a notebook as I have demonstrated in class.

### On a Mac

Open up the terminal and type

    conda env list

Hopefully you only see the `base` environment. Then type

    source activate base

to get the mappings correct for your programs.

### On a Windows Machine

Open up the Anaconda Prompt and type

    conda env list

Hopefully you only see the `base` environment. Then type

    activate base

to get the mappings correct for your programs.

## Adding Modules Using pip

At the anaconda prompt with the `root` environment activated, type:

    pip install matplotlib
    pip install pandas
    pip install plotnine
    pip install scipy
    pip install numpy
    pip install scikit-learn

## Grading

* 20 points for code which leads to the correct answer.
* 10 points for proper citations of references.
* 10 points for written explanations of your attempts.
