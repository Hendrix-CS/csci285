---
layout: work
type: Lab
num: 2
worktitle: Data Visualization
---

## Overview

In this lab, you will find a dataset and analyze it using the python libraries
Pandas and Plotnine.

## Materials

* [FEV dataset](../assets/data/FEV.csv)
* [FEV notebook](https://nbviewer.jupyter.org/urls/hendrix-cs.github.io/csci285/assets/code/FEV_Data_Analysis.ipynb)

### Step 1 - Data Gathering

Find a CSV-formatted scientific dataset with multiple columns and rows of experimental results.
I strongly recommend you get your dataset from the United States Geological Survey data repository
linked below, please talk to me if there is another dataset you wish to examine.

* [USGS Science Datasets](https://www.usgs.gov/products/data-and-tools/science-datasets)

Open a notebook and record the provenance of the data, how it was collected, and by whom.
Discuss the meaning of the columns and rows in your dataset.

### Step 2 - Analysis

Load your csv file as a Pandas data frame.

Analyze your file, attempting to discover if there are any relationships
between the data fields. Specifically, you should find a dataset where you can

* Draw histograms
* Draw scatter plots
* Draw line plots
* Divide the data into subcategories for further plotting
* Use Linear Regression to look for patterns with high correlation

Be sure to label your axes and title your figures.

### Step 3 - Descriptions

Throughout your notebook, write descriptions of your findings and each graph
in `MarkDown` blocks. Include a summary section about what you learned from exploring this data.

## Grading

The FEV notebook linked above is a good example of my expectations for this lab, in terms
of the computational analysis and the written descriptions and reflections.

* 15 points for good use of Pandas functions for summarization, selection, and data cleaning
* 15 points for including each of the requested plot types using plotnine
* 10 points for well-written explanation of data provenance, discussion of each graph, and summary.
