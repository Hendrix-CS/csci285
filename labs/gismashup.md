---
layout: work
type: Lab
num: 3
worktitle: Choropleths
---

## Overview

For this lab, you will be creating a Choropleth, incorporating the tools we learned in class about data analysis and GeoPandas.

## Possible Datasets

* [Our World in Data](https://ourworldindata.org/)
* [Southern Poverty Law Center Hate Crimes Index](http://www.splcenter.org/get-informed/hate-incidents)
* [Medical Expenditure Panel Survey](http://meps.ahrq.gov/mepsweb/)
* [Centers for Disease Control and Prevention](https://data.cdc.gov/)
* [Pew Research](http://www.pewresearch.org/data/download-datasets/)
* [Pew Internet Research](http://www.pewinternet.org/datasets/)
* [Data.gov](https://catalog.data.gov/dataset)
* [Census Data](https://data.census.gov/cedsci/)

## Examples

* [Most Common Job in Every State](http://www.npr.org/sections/money/2015/02/05/382664837/map-the-most-common-job-in-every-state)
* [La Quinta and Denny's coincidence](http://njgeo.org/2014/01/30/mitch-hedberg-and-gis/)
* [Which is closer, beer or whisky?](http://blog.wolfram.com/2014/08/19/which-is-closer-local-beer-or-local-whiskey/)
* [Geology and Voting](http://www.npr.org/blogs/krulwich/2012/10/02/162163801/obama-s-secret-weapon-in-the-south-small-dead-but-still-kickin)
* [Data Visualization at census.gov](http://www.census.gov/dataviz/)
* [Church or Beer on Twitter](http://www.floatingsheep.org/2012/07/church-or-beer-americans-on-twitter.html)
* [Football Allegiance as declared on Facebook](http://www.theatlantic.com/technology/archive/2014/09/the-geography-of-nfl-fandom/379729/)
* [COVID-19 Maps](https://blog.mapbox.com/notable-maps-visualizing-covid-19-and-surrounding-impacts-951724cc4bd8)

## Making a Choropleth

I have linked in a number of possible sources for datasets above, but this is by no means exhaustive, please feel free to use data from a topic you find relevant and interesting.

There are many examples of Choropleths in the news, also linked above. You should similarly strive to a visualization not seen before and that helps explain a hypothesis and visualizes the supporting evidence. Make something awesome that you are proud of and is [reddit](https://www.reddit.com/r/dataisbeautiful/)/[hackernews](https://news.ycombinator.com/) worthy.

### Requirements

Specifically, you should

* Find a geospatial dataset and note its provenance (collection time, accuracy, method, etc).
* Draw a map using this data to shade the regions with colors. This can be on a world, state, national, or county level.
* Use an appropriate projection to minimize distortion in your map.
* Denote the steps you used so that your analysis is repeatable by others.
* Write descriptions in your notebook of your project for a general audience. This should be in the style of a blog post, intermixed with the relevant python code and map figures.
* Give a 3 minute presentation to the class about your findings.

### Something More

For full credit, you must include something more. For example, add in specific points as symbols on the map with Circles or Text, draw a path across the map connecting major important pieces, or animate the map over time by assembling an animated gif. Be creative! Specify in your writeup what takes your lab beyond the required elements above.

## Grading

This assignment is due at 6:00 pm on Thursday, September 8th in Moodle. This is to give me time to assemble your documents for easy presentation in class on Friday, and to allow you to practice your presentation.

* 20 points for drawing a map based on a geospatial dataset using GeoPandas with appropriate projection
* 10 points for well-written explanation of data provenance, discussion of each graph, and summary.
* 5 points for class presentation of analysis.
* 5 points for something more.
