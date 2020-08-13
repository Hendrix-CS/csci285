---
layout: work
type: Lab
num: 4
worktitle: K-means and PCA
---

## Overview

https://www.researchgate.net/publication/43080482_A_global_map_of_human_gene_expression

https://www.ebi.ac.uk/arrayexpress/files/E-MTAB-62/E-MTAB-62.sdrf.txt

https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-62/

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

-   [Ovarian and Breast Cancer Data](http://mark.goadrich.com/courses/csci385f16/data/cancergenes.txt)

Create a Jupyter notebook, and read this file into a Pandas DataFrame.
The gene expression data is separated by tabs, so you will need the
`sep="\t"` argument for `read_csv`. The first row specifies the labels of
each column. In this file, each row shows the expression levels for one
of 978 different genes. The first column lists the name of the gene, and
the remaining columns show results for 16 samples, one from each patient
with cancer. An individual value in this dataset is a number representing
the normalized logarithm of how a particular gene was expressed in a
particular sample in comparison to a normal sample.

### Step 2

To visually see and compare trends across the whole microarray
experiment, a heatmap plot is commonly used. You will find
code that brings in a dataset and maps it to the red-green color
spectrum on a heat map. Red indicates that this gene is expressed
much less than expected in control conditions, and green
indicates that this gene is expressed much more than expected.

    theme_set(theme_void())
    ggplot(df_rows, aes('variable', 'NAME')) + geom_tile(aes(fill='value'))\
        + scale_fill_gradientn(colors=['#FF0000','#000000','#00FF00']) \
        + theme(
        figure_size=(3, 10), # inches
        aspect_ratio=5    # height:width
    )

Plot your data using this function and discuss any patterns you notice
in the figure.

### Step 3

We will need to cluster the genes in this data.
Use K-means clustering to separate the genes into 2 clusters
Reorganize your data based on these clusters, such that the genes in one
cluster are placed above the genes in the other cluster.

Draw a plot with this new data, and report on any patterns you
notice in the figure.

### Step 4

## Evaluation

## Grading

* To earn a 5, demonstrate
* To earn a 10, do the above and
* To earn a 14, do the above and
* To earn a 17, do the above and
* To earn a 20, do the above and
