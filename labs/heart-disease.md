---
layout: work
type: Lab
num: 3
worktitle: K-means and PCA
---

## Overview

Imagine you are tasked by the [Cleveland Clinic](http://my.clevelandclinic.org/) to help them train new doctors to diagnose patients with [heart disease](https://en.wikipedia.org/wiki/Cardiovascular_disease). They have been reviewing their past patient histories and started to notice some patterns after narrowing their focus to a few key features of each patient. They also give you some more detailed information about these features in the form of a data dictionary,

| Feature | Data Type | Description |
|:----|:------|:-----|
| age                       | int       | age in years |
| female                    | boolean   | true if female patient |
| chest_pain                | string    | type of chest pain |
| rest_bps                  | int       | resting systolic blood pressure in mm Hg on admission to the hospital |
| cholesterol               | int       | serum cholesterol in mg/dl |
| high_fasting_blood_sugar  | bool      | true if > 120 mg/dl |
| rest_ecg                  | string    | resting electrocardiographic results |
| maximum_heart_rate        | int       | maximum heart rate achieved |
| exercise_angina           | bool      | exercise induced angina |
| vessels                   | int       | number of major vessels (0-3) colored by flourosopy, showing they are clogged |
| heart_disease             | bool      | doctor's diagnosis of heart disease |

<br />

## Step 1: Understanding the data

You will be analyzing past patient history in order to understand patterns of heart disease. Create a Jupyter notebook and read the cleveland-testing.csv into a pandas data frame.

* Here is the dataset for the lab: [cleveland-testing.csv](../data/cleveland-testing.csv)
* Display the shape (i.e. rows & columns) and a subset of the data using pandas. 
* Display `.dtypes` and confirm these match with the provided data dictionary.
* `.describe()` the dataset to understand the quality of numerical columns


### Step 1.1: Categorical analysis

* Display `.value_counts()` for `chest_pain`, `rest_ecg`, and `heart_disease`. 
* Construct three pairwise plots that color these three categorical features against the five numerical features.


Discuss any patterns or other interesting traits you notice from your numerical and categorical analysis.


## Step 2: K-Means

Run K-Means using the five numerical features as input. Make sure to drop any NaN values in these features (garbage in, garbage out) and also remember to scale your features in order to avoid overfitting. Store two new columns to your original data frame, 

* `cluster` - this should be 0 or 1 and is the resulting labels from running K-Means.
* `prediction` - transformed 0s and 1s into True/False values that align with the ground truth `heart_disease` column.


## Step 3: Confusion matrix

Produce a confusion matrix (2x2) and associated heatmap that compares ground truth values (i.e. `heart_disease`) against predicted values. Discuss the outcome of running K-Means on this dataset and explain this in terms of four categories: 

* True Positives - These patients have heart disease and were predicted correctly
* False Positives - These patients do **not** have heart disease and were predicted **incorrectly**
* True Negatives - These patients do **not** have heart disease and were predicted correctly
* False Negatives - These patients have heart disease and were predicted **incorrectly**


## Step 4: Principal component analysis

Use PCA to find the first two principal components. The variance of each component explains its "importance" in the decomposition. By running `pca = PCA(n_components=2).fit(x)`, you can get back the variance of each component from `pca.explained_variance_`. You can then run `pca.transform(x)` to rotate your input features into PCA-1/PCA-2 space. 

* Produce a bar chart that plots the components (PCA-1, PCA-2) against their explained variance. 
* Produce a scatter plot of the PCA rotated heart disease data colored by cluster (i.e. K-Means resulting labels). 

Describe how much variance is explained through using these components. 


## Step 5: Discussion

How would you decribe the results of this experiment? What would you recommend to the doctors that tasked you with this problem? What could be done to improve the outcome of your model? Assuming you cannot build a perfect model, how should you optimize your model with respect to the confusion matrix analysis?


## What To Turn In

As you work on this lab, record all of your progress in a Jupyter notebook. Record your solutions and attempts in `Code` blocks, and annotate what you did with `MarkDown` blocks. Cite all the webpages you find and use in your search for your solution. You should turn in this notebook and all of the data you used. A good solution should read like a self-contained report.

* Add your name and your lab partner at the top of the notebook. 
* Turn in a zip file that contains your notebook and any data needed to run the notebook.


## Grading

* Complete: Notebook can be read easily w/o needing to reference this page for additional detail. It should read like a self-contained report. It can be executed without producing runtime errors. All steps (1, 2, 3, 4, and 5) are finished and all discussion questions are answered. All data loaded into the notebook should be provided.

* Partially complete: Notebook can be executed without producing runtime errors. All steps (1, 2, 3, 4, and 5) are attempted.
