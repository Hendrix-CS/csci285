---
layout: work
type: Lab
num: 4
worktitle: Modeling Flight Delays
---

## Overview
The U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics tracks the on-time performance of domestic flights operated by large air carriers. Summary information on the number of on-time, delayed, canceled, and diverted flights is published in DOT's monthly Air Travel Consumer Report and in this dataset of 2015 flight delays and cancellations.

We discussed this dataset in class using [Flight Delays And Cancellations](https://nbviewer.org/github/Hendrix-CS/csci285/blob/master/assets/notebooks/Flight_Delays_And_Cancellations.ipynb?flush_cache=true). It may be a good idea to review this notebook as a starting point for this lab. In this notebook, we aggregated `arrival_delay` and `departure_delay` by airline, airport, and month. In this lab, you are going to take a closer look at delays and model them using regression.

<br />

### Transformed Data
Instead of working with the raw flights data, you will use a tranformed version made specifically for this lab. [Click here](https://www.kaggle.com/datasets/hendrixwilsonj/flights-transformed) to download. This data is quite large (727mb) so I zipped it to make it easier to download.

<br />

### References
* [https://www.kaggle.com/datasets/usdot/flight-delays](https://www.kaggle.com/datasets/usdot/flight-delays)


<br />

## Step 1: Loading `flights`
* Load the transformed data into a data frame called "flights" and familarize yourself with the size and quality of the dataset. 
* Convert `scheduled_departure` to a datetime (this column loads as a string)
* Write a data dictionary which explains each column's dtype and meaning.

<br />

## Step 2: Aggregating & Plotting Delay
Let's start by performing some general analysis about delays. From [Flight Delays And Cancellations](https://nbviewer.org/github/Hendrix-CS/csci285/blob/master/assets/notebooks/Flight_Delays_And_Cancellations.ipynb?flush_cache=true), we learned that most airlines report delays close to zero but all experience large outliers. 

Using two bar charts aggregated by `airline`, plot mean `departure_delay` and mean `arrival_delay`. Make sure to label your charts, size the figure correctly, and set a title. 

**Feature Selection**: Restrict columns to just the three mentioned above.

**Aggregation**:  You'll need to aggregate the data (i.e. mean delays) after feature selection. Once aggregation is done, its common to [reset the index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html) in order to make the data easier to plot. 

<br />

### Discussion
Examine the charts you just produced. Which airlines are outliers for `departure_delay`? Which airlines are outliers for `arrival_delay`? Find the mean `departure_delay` and `arrival_delay` across all airlines excluding any outliers.

<br />

## Step 3: Departure Delay
In Step 2, you showed that mean `departure_delay` is larger than mean `arrival_delay` (If that's not the conclusion you got in Step 2, you may want to revisit your answer!). This can be explained by flights increasing their flight speed (and thereby burning more fuel) in order to make up for lost time.

For the rest of this lab, we will continue to model `departure_delay`, but ignore `arrival_delay` since it may be impacted by variables outside the `flights` dataset (e.g. flight speed). 

<br />

### Origin Airport vs. Airline
Let's see if the `origin_airport` has an impact on `departure_delay` by plotting a heatmap of `airline` vs. `origin_airport`. The color should correspond to `delay_level`, which we will define in a bit. 

**Feature Selection**: Start by creating a dataframe that has the three columns mentioned above.

**Aggregation**: Group the dataframe by `origin_airport` and `airline` and calculate mean `departure_delay`. The resulting dataframe should have a shape of (1304, 1). `origin_airport` and `airline` should make up a [MultiIndex](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html).

**Augmentation**: Create a new feature called `delay_level`. Values in this column should be one of "on time" (if delay is less than 5 minutes), "small delay" (if delay is less than 45 minutes) or "long delay". 

**Reshaping**: Select just the `delay_level` series from the grouped dataframe and call [.unstack()](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-stacking) to shape the series back into a dataframe that has `origin_airport` as its index and all of the airlines as columns. The final shape should be (322, 14). The values of this heatmap should be the `delay_level` categories you just defined. 

**Plotting**: Finally, use the provided plot_heatmap_discrete_legend() function to visualize this dataset. This function's purpose is mostly to discretize the `delay_level` color pallete and legend. You should be able to pass the unstacked data frame that has a shape of (322, 14) to this function as a parameter.


Run in a cell by itself,
```
%%javascript
IPython.OutputArea.prototype._should_scroll = function(lines) {
    return false;
}
```

and then in a new cell define the following function, 
```
from matplotlib.colors import LinearSegmentedColormap


def plot_heatmap_discrete_legend(data):
    
    # Set the width and height of the figure
    plt.figure(figsize=(20,100))
    
    # Add title
    plt.title("Average Departure Delay (Airline vs. Origin Airport)")
    
    # calc discrete values
    value_to_int = {j:i for i,j in enumerate(pd.unique(data.values.ravel()))}
    n = len(value_to_int)   

    # discrete colormap (n samples from a given cmap)
    cmap = sns.color_palette("Paired", n) 
    ax = sns.heatmap(
        data=data.replace(value_to_int), 
        cmap=cmap,
        linewidths=0.5,
        linecolor='lightgray'
    ) 

    # modify colorbar
    colorbar = ax.collections[0].colorbar 
    r = colorbar.vmax - colorbar.vmin 
    colorbar.set_ticks([colorbar.vmin + r / n * (0.5 + i) for i in range(n)])
    colorbar.set_ticklabels(list(value_to_int.keys()))                                          
    
    # show plot
    plt.show()
```

<br />

### Discussion
Compare the output from using plot_heatmap_discrete_legend() vs. a vanilla call to `sns.heatmap`. What's the value of discretizing the color pallete and legend?

Discuss whether `origin_airport` has an impact on `departure_delay`. Are some airports more prone to delays than others? Or is `origin_airport` not an important feature when modeling flight delays?

<br />

## Step 4: Temporal Analysis (Bonus)
In Steps 2 & 3, you did an analysis of how `airline` and `origin_airport` affect `departure_delay`. We also narrowed our view to just modeling `departure_delay`. Let's start modeling delays now by looking at `scheduled_departure` more closely for a given `airline` and `origin_airport`. 

**Note**: There is so much data to parse that in order to visualize its temporal nature we need to restrict our view to a smaller time range.

<br />

### Transformation

**Feature Selection**: Start by restricting, re-naming, and re-ordering your dataset's features to the following columns: (airline, airport, time, delay). Here "airport" means `origin_airport`, "time" means `scheduled_departure` and "delay" means `departure_delay`. 

**Aggregation**: You'll need to aggregate the data (i.e. mean `delay`) after feature selection. It is possible for multiple rows to match (airline, airport, time) because destination airport has been dropped (i.e. multiple flights can leave at the same time going to different destinations). Check for duplicates before and after aggregating to ensure this was done correctly.

**Filter Data**: Set the following filters, 

```
# Check out https://chrisalbon.com/code/python/data_wrangling/pandas_selecting_rows_on_conditions/ for how to chain pandas conditionals together

delaythreshold = 60 * 12 # delayed less than a day. 

time_range = f['time'] < datetime.datetime(2015, 1, 15)
delay_cap = f['delay'] < delaythreshold
airline = f['airline'] == "American Airlines Inc."
airport = f['airport'] == "Dallas/Fort Worth International Airport"
```

I deliberately chose an airline and airport that I knew would have lots of data to work with - AA is headquartered in Dallas, so there are a large number of daily flights. Make sure to **drop any NaN values** from the final dataframe. 

<br />

### Plot `time` vs. `delay`
Create two line charts. The first line chart should show data ranging from 2015-01-01 to 2015-01-14. For the second, choose only two or three days of data to display. Make sure to label your axes and set a title. Size the figure appropriately. Set `aspect=3.0`.

<br />

### Model time of day
Now we want to zero in on `time` and `delay` across all airlines and for all of 2015. Reduce the dataset again to just two columns: `time` and `delay`. Make sure to to clear any filters, such as airline/airport, that were previously applied. This plot should cover the full 2015 dataset for all airlines. 

Convert the `time` column to just be "seconds since the start of the day". You can either make a new column, or replace the existing `time` column with this new series. Create a scatter plot and regression line using [lmplot](https://seaborn.pydata.org/generated/seaborn.lmplot.html). 

* Aggregate data and drop any NaN values.
* Label your axes and set a title. 
* Size the figure appropriately. Set `aspect=3.0`.
* Color the reg line by passing `line_kws={'color': 'red'}` as an argument to `.lmplot()`.
* Pass as an argument `order=3` to fit a polynomial of 3 terms intead of linear.

<br />


### Discussion
For each plot, what patterns in the data do you observe? What explains these patterns?

<br />


## Step 5: Choropleths (Bonus)
In [airports.csv](../assets/data/airports.csv) there are geographical features that can be used to make choropleths. Overlay airport location on top of any choropleth of your choosing. You may need to use [kaggle](https://www.kaggle.com/) to load the necessary geopandas libraries. Please turn in step 5 in a separate notebook from Steps 1-4.


## What To Turn In

**Note**: Please do not turn in the data you used for this lab. The file size is too large.

As you work on this lab, record all of your progress in a Jupyter notebook. Record your solutions and attempts in `Code` blocks, and annotate what you did with `MarkDown` blocks. Cite all the webpages you find and use in your search for your solution. A good solution should read like a self-contained report.

* Add your name and your lab partner at the top of the notebook. 
* [https://dillinger.io/](https://dillinger.io/) for good `MarkDown` styling.
* Go to the file menu and do "Kernel -> Restart and Run All" before submitting. This ensures there are no runtime errors and all figures are generated correctly.


## Grading

* Complete: Notebook can be read easily w/o needing to reference this page for additional detail. It should read like a self-contained report. It can be executed without producing runtime errors. All steps (1, 2, 3, and optionally 4, 5) are finished and all discussion questions are answered.

* Partially complete: Notebook can be executed without producing runtime errors. Steps (1, 2, 3) are attempted.

* Bonus #1: If you complete Step 4, then you can get 15 additional points added to your Exam #1 grade. This is enough to turn a "B" into an "A".

* Bonus #2: If you complete Step 5, then you are can receive one additional "late work day" to use anytime the rest of the semester.

