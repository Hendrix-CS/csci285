---
layout: work
type: Lab
num: 2
worktitle: Data Visualization
---

## Overview

In this lab, you will find a dataset and analyze it using the pandas and seaborn python libraries.

## Materials

* [FEV dataset](../assets/data/FEV.csv)
* [FEV notebook](https://nbviewer.jupyter.org/urls/hendrix-cs.github.io/csci285/assets/notebooks/FEV_Data_Analysis.ipynb)
* [Seaborn Regression Models](https://seaborn.pydata.org/tutorial/regression.html)


## Step 1: Data Gathering

Find a CSV-formatted scientific dataset with multiple columns and rows of experimental results. Your dataset must have more than one numerical feature and at least one categorical feature. Here are some resources for open data:

* [USGS Datasets](https://www.usgs.gov/products/data)
* [Little Rock Data Hub](https://data.littlerock.gov/)
* [NYC Open Data](https://opendata.cityofnewyork.us/)


Open a notebook and begin writing your data dictionary. 

* Record the provenance of the data.
* How it was collected and by whom.
* Describe the features (e.g. columns) of your data


## Step 2: Analysis

Load your csv file as a Pandas data frame. Begin exploring your data using the methods discussed in class and used in Lab #1. Perform any data transformations that you feel adds value to your analysis.

## Step 3: Visualization

Continue exploring your data using visualization techniques discussed in class. Specifically, 

* Draw histograms
* Draw scatter plots (with and without linear reg)
* Draw categorical plots (box, violin, swarm, etc.)
* Divide the data into subcategories for further plotting

Be sure to label your axes and title your figures. 

## Step 4: Conclusions

Throughout your notebook, write descriptions of your findings and graphs. Draw some conclusions. Include a summary section near the end about what you learned from exploring this data.

## What To Turn In

As you work on this lab, record all of your progress in a Jupyter notebook. Record your solutions and attempts in `Code` blocks, and annotate what you did with `MarkDown` blocks. Cite all the webpages you find and use in your search for your solution. You should turn in this notebook, all of the data you used, and anything else produced during your investigation. A good solution should read like a self-contained report.

## Grading

The FEV notebook linked above is a good example of my expectations for this lab, in terms of the computational analysis and the written descriptions and reflections.

* Complete: Notebook can be read easily w/o needing to reference this page for additional detail. It should read like a self-contained report. It can be executed without producing runtime errors. All steps (1, 2, 3, and 4) are finished. All data loaded into the notebook should be provided.

* Partially Complete: Notebook can be executed without producing runtime errors. All steps (1, 2, 3, and 4) are attempted.
