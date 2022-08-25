---
layout: work
type: Lab
num: 1
worktitle: Lake Trout
---

## Overview

In this lab, you will refresh your knowledge of Python, install conda, and get some practice using pandas. You will also learn a great deal about how to determine the age of lake trout in Alaska using [otolith growth measurements](https://en.wikipedia.org/wiki/Age_determination_in_fish).

The data you'll need can be downloaded as a zip file here: https://alaska.usgs.gov/products/data.php?dataid=306. An abstract of a paper published using this data can be found here: https://onlinelibrary.wiley.com/doi/epdf/10.1111/eff.12566 (not important to the lab, but you may be curious to learn more about trout!)

## Installing Anaconda

To analyze our data this semester, we will be using Anaconda and Jupyter Notebooks, and hosting these on our own computers. The [Anaconda Installation](https://docs.anaconda.com/anaconda/install/) page lists many instructions for multiple operating systems. Follow the instructions that make sense to you. Or, if you prefer a more light-weight approach, you can start with [miniconda](https://docs.conda.io/en/latest/miniconda.html). If you go with miniconda, then you may require more setup than others. Reach out to your instructor if this interests you.

In order to test that your installation was successful, follow [these instructions](https://docs.anaconda.com/anaconda/install/verify-install/).

### Open a Jupyter Notebook

There are multiple ways to use Anaconda. You can use the `conda` command line tool to manage your python environments, fire up an instance of [Pycharm](https://www.jetbrains.com/pycharm/), or start a `jupyter notbook` or `jupyter lab` right from your terminal. For starters, the simpliest way may be to use Anaconda Navigator to launch either a jupyter notebook or jupyter lab.

Note: Your instructor prefers `jupyter lab`.

## Step 1: Understanding the data
Download the archive and unzip it to find the following three files: 
* lakeTrout_otolithGrowth_LakeClarkNP_vonBiela_1979_2012.csv
* lakeTrout_otolithGrowth_LakeClarkNP_vonBiela_1979_2012_metadata.html
* lakeTrout_otolithGrowth_LakeClarkNP_vonBiela_1979_2012_metadata.xml

### 1.1: Create a data dictionary
The included metadata files (.html or .xml) can be thought of as a [data dictionary](https://en.wikipedia.org/wiki/Data_dictionary), which typically provide critical context for the data you are looking to analyze. Every time you begin working with a new, unfamiliar dataset, your first question should always be: Where is the data dictionary?

1. In your notebook, using `MarkDown`, write a simplified form of the data dictionary that will help readers answer the following questions: 
* What does each column of data represent? 
* What is each column's data type? (hint: `df.dtypes`)
* If a column is numeric, what are its units? 
* Anything special mentioned / caveats / other pitfalls the reader should be aware of? 

2. There is a section in the metadata called "Data Quality". Is there anything in that section that the user of this data may want to be aware of? Add that to your data dictionary section.

### 1.2: Grokking & (lightly) transforming the data
Load the data into a `pandas.DataFrame` and begin exploring its contents. 

1. What is the shape of the data (how many rows, how many columns)? 
2. Use `.head()` or `.tail()` to view a section of the dataset. 
3. Convert all of the column names to lower case. 
4. Are there any [duplicate](https://chrisalbon.com/code/python/data_wrangling/pandas_delete_duplicates/) rows in this dataset? If so, drop them. What explains duplicate rows?
5. How many distinct fish are being studied in this dataset?

### 1.3: Descriptive Statistics
Perform some common [descriptive statistics](https://chrisalbon.com/code/python/data_wrangling/pandas_dataframe_descriptive_stats/) on the data. What conclusions can you draw from steps 1-5 about the data?

1. Run `.describe()`. Does this output align with what the data dictionary says about max/min values for `year` and `age`?
2. Find the max and min values of the `age` column using at least one other method besides `.describe()`. 
3. For the `year` column, run `.value_counts()` and `.hist()`. Compare and constrast both techniques.
4. Produce histograms for the `age` and `width` columns in addition to `year`.
5. For the `lake` column, run `.value_counts()`. 


## Step 2: Aggregating the data
For this section of the lab, I want you to write out a CSV file that has two columns: `lake` and `fish_count`. This CSV file should be turned in with your notebook and raw data.

1. Create a dataframe that only has the two columns of interest.
2. Drop duplicates (there are multiple measurements per fish, but we only care about number of fish in the study per lake).
3. Use `.groupby('lake').count()` on your dataframe aggregate the data. Learn more about `groupby` [here](https://chrisalbon.com/code/python/data_wrangling/pandas_apply_operations_to_groups/).
4. Rename the aggregated column name to `fish_count`. 
5. Save the resulting dataframe to a [CSV file](https://chrisalbon.com/code/python/data_wrangling/pandas_saving_dataframe_as_csv/). 


## Step 3: Python Only
As you can (hopefully) appreciate by now, doing all of this analysis with pure python (sans pandas) would be a daunting task even for the most savvy pythonistas. In order to drive this point home, please re-do 1.3.5 using only python libraries. 

> For the `lake` column, run `.value_counts()`.

In other words, compute how many times each lake appears in the CSV file. You'll need to load the CSV file using https://docs.python.org/3/library/csv.html. A dictionary is a good data structure to use for this.


## What To Turn In

As you work on this lab, record all of your progress in a Jupyter notebook. Record your solutions and attempts in `Code` blocks, and annotate what you did with `MarkDown` blocks. Cite all the webpages you find and use in your search for your solution. You should turn in this notebook, all of the data you used, and the CSV file produced in Step 2. A good solution should read like a self-contained report.

{% include warning.html content="For this lab, you can collaborate with your team, but each team member must install the necesssary tooling we will use for the rest of the semester." %}

## Grading

* Complete: Notebook can be read easily w/o needing to reference this page for additional detail. It can be executed without producing runtime errors. All steps (1, 2, and 3) are finished and all discussion questions are answered. All data loaded into the notebook and the CSV file produced in step 3 should be provided.

* Partially complete: Notebook can be executed without producing runtime errors. All steps (1, 2, and 3) are attempted. All data loaded into the notebook and the CSV file produced in step 3 should be provided.

