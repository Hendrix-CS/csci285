---
layout: work
type: Lab
num: 6
worktitle: Agent-Based Modeling
---

## Overview

In this lab, you will use [Mesa](https://github.com/projectmesa/mesa) to update and implement Agent-Based Models related to forest fires, chemical diffusion, ant pheromone communication, and termite construction.


## Step 1 - Forest Regrowth

Start by making a copy of the [Forest Fire Notebook](https://www.kaggle.com/code/markgoadrich/forest-fires-mesa-abm-2-4) in a new Kaggle Notebook. 


### Add Complexity

Add a new state to the tree called `Empty`, and make it the default condition for new Trees. 

Add a new parameter to the model called `lifetime` which denotes how long a tree will live in the model. Each tree when initialized to `Fine` should be given an age between 0 and `lifetime`.

Revise the model setup so that an `Empty` Tree is added to every space. Use the `density` parameter to initialize some Trees to `Fine`.

Continue the current assumption that all Trees with `x == 0` should start `On Fire` but change the ending condition of the model step method to be based on if `self.schedule.time` is greater than 200.


### Change Tree Lifecycle

Now, revise the Tree lifecycle in the step method to incorporate the following:

* `Burned Out` trees decay over time. Add a `decay_time` integer parameter to the model. Each tree that is burned should keep track of the time since it was burned. After the `decay_time` has passed, the tree decays, and its condition should be `Empty`.

* `Fine` trees can grow new `Fine` trees in adjacent `Empty` neighbors. When a tree reaches the age of the `lifetime` parameter, the tree will try to change up to two adjacent `Empty` spaces into `Fine` trees, and set their age to 0. Then, the tree will change its own condition to `Empty`.


### Analysis

Using [Forest Fire Notebook](https://nbviewer.org/github/Hendrix-CS/csci285/blob/master/assets/notebooks/Forest%20Fire%20Model.ipynb) for reference, create a notebook to re-run model simulations and perform a parameter sweep over `decay_time` from 0 to 60 with a step size of 2. Run each parameter choice 4 times. Set the other parameters, such as density and lifetime, to the interesting values you determined through visualizing your model.

 Determine the effect of changing this parameter on the number of `Fine` trees after 200 time steps.

