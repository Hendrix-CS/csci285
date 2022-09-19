---
layout: work
type: Exam
num: 1
worktitle: Visualizing Data from the Duke Lemur Center
---

## Description

![Leaping Sifaka from DLC](../assets/images/leaping.jpg){: .pull-right .w-50 .img-fluid}

The [Duke Lemur Center](https://lemur.duke.edu/) (DLC)
is an 85 acre research facility in Durham, North Carolina
that currently houses over 200 lemurs from many different
species of lemurs. Researchers at the DLC care for
lemurs and record data on their growth, diet, and
social interactions, to learn more about these amazing
animals on the edge of extinction in their native Madagascar.

In this exam, you will be analyzing
[two datasets](https://lemur.duke.edu/duke-lemur-center-database/)
about lemurs in residence at the DLC, which can be cited as
*Zehr, SM, Roach RG, Haring D, Taylor J, Cameron FH, Yoder AD. Life history profiles for 27 strepsirrhine primate taxa generated using captive data from the Duke Lemur Center. Sci. Data 1:140019 doi: 10.1038/sdata.2014.19 (2014).*

Specifically, you
will identify an extreme outlier in one dataset, and cluster
different species across multiple statistics in another dataset.

{% include important.html content="Be sure to add readable labels to your axes and a title for
each graph you generate." %}

[Register for free](https://duke.qualtrics.com/jfe/form/SV_cZMTHoHiAljNGXX?Q_JFE=qdg)
at the DLC Database website and download
the following files.
* DLC-data
  * Updated_Data_Release_2019
    * 2_DLC_Life_History_Table_Folder
      * DataRecord_1b_DLC_LH_Table_Analysis_05Feb2019.csv
      * DLC_LH_Table_VariableDescriptions_and_UsageNotes_08Feb2019.pdf
    * 4_DLC_Weight_File_Folder
      * DataRecord_3_DLC_Weight_File_05Feb2019.csv
      * DLC_WeightFile_VariableDescriptions_and_UsageNotes_08Feb2019.pdf

{% include important.html content="If you are having trouble opening the files because of a UTF-8 error, please try my local copies of the  files linked below." %}

* [Weight]({{site.baseurl}}/assets/data/DataRecord_3_DLC_Weight_File_05Feb2019.csv)
* [Life History]({{site.baseurl}}/assets/data/DataRecord_1b_DLC_LH_Table_Analysis_05Feb2019.csv)

## Lemurs of Unusual Size

### Step 1

The lemurs are regularly weighed as part of their medical
checkups throughout the year. The **Weight_File** table
holds the information recorded during
each lemur's weighing. Each row is a different
weighing instance. The columns are described in the
**Descriptions and Usage Notes** file.

Load the **Weight File** into a Pandas DataFrame. Record how many
rows and columns are in the DataFrame.

What is the name and species of the earliest lemur recorded to be pregnant at the DLC, and what was the date of birth of the infant lemur?

### Step 2

Draw a boxplot of adult lemur's weight in grams versus sex.

What
differences do you notice in this plot?

### Step 3

Draw a boxplot of adult lemur's weight in grams versus the species
(taxon), rotating the labels on the x axis by 90 degrees.

What
differences do you notice in this plot?

Discuss what you notice in
the data for the sifaka species.

### Step 4

Draw a scatterplot of adult
[sifaka](https://en.wikipedia.org/wiki/Sifaka) lemur's weight in
grams **on the y axis** versus their age in years at the time of weighing **on the x axis**, using an alpha
transparency of 0.1.

Add in a linear regression line to this graph.

Discuss any trends you notice in the data and any outliers.

### Step 5

Draw a line graph of **all** (infant/juvenile,
young adult, and adult) sifaka lemur's weight in
grams **on the y axis** versus their age in years at the time of
weighing **on the x axis**, and color the lines based on the name of the lemur.

Identify the name of the outlier lemur we have been
noticing all along.

Search Google for this name in quotes
plus "duke lemur center" and summarize your findings.

## A Conspiracy of Lemurs

![Sifaka Selfie from DLC](../assets/images/sifakas.jpg){: .pull-right .w-50 .img-fluid}

### Step 6

The **Life History** table holds aggregate information about the
species of lemurs in residence at the DLC. Each row is a different
species. The columns are described in the
**Descriptions and Usage Notes** file.

Load the **Life History** file into a Pandas DataFrame. Record how many
rows and columns are in the DataFrame.

### Step 7

Create a reduced DataFrame with only the following columns:

* Latin_Abbreviation
* R_Ratio_MtoF_DLCBirths
* R_Mean_LitterSize
* R_Expected_Gestation_d
* R_Peak_Birth_Month
* M_Mean_All_AdultWeight_g
* M_Mean_All_NeonateWeight_g
* M_Mean_All_YngAdultWeight_g
* L_Median_All_Longevity_gt30d_y
* L_Pct_All_InfMort_lt30d

In this reduced DataFrame, keep only the rows that do
not have any *NaN* values.

### Step 8

Extract the values of the numerical columns in the reduced DataFrame
and standardize the data.

Use KMeans to cluster this data into two clusters.

### Step 9

Find the first two principal components of the data you
standardized in Step 8 using PCA.

Create a new DataFrame using your results with `PCA 1` and `PCA 2` columns.

Add the cluster labels from Step 8 to the
PCA DataFrame in a new `cluster` column and
force the datatype to be a string.

Also add a new column called `Latin_Abbreviation` using
the values from the reduced DataFrame. (If you just copy the
column, the data will be misaligned because of the dropped row
from Step 7).

### Step 10

Draw a scatterplot of the PCA DataFrame using `PCA 1`
as the x-axis and `PCA 2` as the y-axis. Color the plot
based on the `cluster` column.

Add in the species as labels to the points using the following code

    + geom_text(aes(label="Latin_Abbreviation"))

Discuss the results from this chart.

Compare this plot to the chart you created in Step 3. Does this
clustering make sense in light of your earlier chart?

What species was found to be the closest to the sifaka lemurs
in your clustering? Why do you think they were
clustered together? How are they alike? How are they different?

## Handin and Grading

Turn in your Jupyter Notebook on Moodle in the Exam 1 folder.

Each step will be worth 12 points.

{% include important.html content="Add readable labels to your axes,
include a title for each graph you generate, discuss your results,
and cite all of your references and resources used to complete
this exam." %}
