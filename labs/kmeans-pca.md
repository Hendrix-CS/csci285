---
layout: work
type: Lab
num: 4
worktitle: K-means and PCA
---

## Description

A common way to gain insight into the underlying genetic components of a
disease is through running an experiment with a [DNA
Microarray](http://en.wikipedia.org/wiki/DNA_microarray). A microarray
can detect the levels of thousands of genes simultaneously. More details
on the way these datasets are created from biological experiments can be
found
[here](http://www.mrc-lmb.cam.ac.uk/genomes/madanm/microarray/chapter-final.pdf).

### Step 1

First, you will be analyzing the results of a microarray experiment related to
breast and ovarian cancer, found in the publication
[Gene Expression Patterns in Ovarian Carcinomas](http://www.molbiolcell.org/content/14/11/4376.full), by
Schaener et al. Mol. Biol. Cell, Nov 1 2003, vol 14, no 11. The
following file contains a subset of their experimental data.

-   [Ovarian and Breast Cancer Data]({{site.baseurl}}/assets/data/cancergenes.csv)

Create a Jupyter notebook, and read this file into a Pandas DataFrame.
The gene expression data is separated by tabs. The first row specifies the labels of
each column. In this file, each row shows the expression levels for one
of 978 different genes. The first column lists the name of the gene, and
the remaining columns show results for 16 samples, one from each patient
with cancer. An individual value in this dataset is a number representing
the normalized logarithm of how a particular gene was expressed in a
particular sample in comparison to a normal sample.

### Step 2

To visually see and compare trends across the whole microarray
experiment, a heatmap plot is commonly used.

First, melt the data so
that you have three columns, one for the NAME, one for the Sample,
and one for the value.

Reset the Sample column to be Categorical based on the order in the
original data frame, since this is different than alphabetical.

Construct a heatmap where red indicates that this gene is expressed
much less than expected in control conditions (negative numbers), and green
indicates that this gene is expressed much more than expected (positive numbers).

Plot your data discuss any patterns you notice in the figure.

### Step 3

Now we will need to cluster the genes in this data.

Use K-means clustering to separate the genes into 2 clusters.

Reorganize your data by making the NAME column Categorical
based on these clusters, such that the genes in one
cluster are placed above the genes in the other cluster.

Draw a plot with this new data, and report on any patterns you
notice in the figure.

Compare the figure you created with those
found in the original scientific paper.

### Step 4

Next, we look at a different dataset, from
[A Global Map of Human Gene Expression](https://www.researchgate.net/publication/43080482_A_global_map_of_human_gene_expression) by Lukk et al.
Nature Biotechnology April 2010. This comprehensive survey
tried to understand the structure of genetic expression through examining
5,372 human samples representing 369 different cell and tissue types,
disease states and cell lines. Each cell is associated with 22,283
microarray experiments. We will use their
[data](https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-62/) and
replicate their study to visualize
the cell types using PCA.

The original data is transposed from how we need it to use our sklearn PCA
library, so use the following lines of code to write a new reformated file.

    df = pd.read_csv("data/hgu133a_rma_okFiles_080619_MAGETAB.csv", sep='\t', header=None).T
    df.columns = df.iloc[0]
    df.drop(0,inplace=True)
    df.to_csv("data/hgu133a_rma_okFiles_080619_MAGETAB_fixed.csv", index=False)

Open a new notebook, and load the fixed data as a Pandas DataFrame.
The first two columns are information about
the sample, and the remaining columns are the microarray experiments.

Use PCA to find two principal components.

Draw a plot of the data on these two components.

Describe how much variance is explained through using these components.

### Step 5

Finally, load up the data file `E-MTAB-62.sdrf.txt` that includes the cell types for each of the
samples used in the study.

Color your plot above using the
`Characteristics[Blood/NonBlood meta-groups]` column.

Then make another plot using the
`Factor Value[4 meta-groups]` column for the color.

Report on any patterns you notice in the figure.

Compare the figure you created with those
found in the original scientific paper.

## Grading

* To earn a 5, demonstrate
* To earn a 10, do the above and
* To earn a 14, do the above and
* To earn a 17, do the above and
* To earn a 20, do the above and
