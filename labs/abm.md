---
layout: work
type: Lab
num: 7
worktitle: Agent-Based Modeling
---

## Overview

In this lab, you will use [Mesa](https://github.com/projectmesa/mesa) to update and implement Agent-Based Models related to forest fires, chemical diffusion, ant pheromone communication, and termite construction.


## Step 1 - Forest Regrowth

Start by opening [https://github.com/projectmesa/mesa/tree/main/examples/forest_fire](https://github.com/projectmesa/mesa/tree/main/examples/forest_fire) in a new PyCharm Project. Confirm that you can run `python run.py` or `mesa runserver` and see the forest fire visualization. 


### Add Complexity

Add a new state to the tree called `Empty`, and make it the default condition for new Trees. Revise the model setup so that an empty Tree is added to every space. Use the `density` parameter to initialize some Trees to `Fine`.

Add a new parameter to the model called `lifetime` which denotes how long a tree will live in the model. Each tree when initialized to `Fine` should be given an age between 0 and `lifetime`.

Continue the current assumption that all Trees with x == 0 should start `On Fire` but change the ending condition of the model step method to be based on if `self.schedule.time` is greater than 200.


### Change Tree Lifecycle

Now, revise the Tree lifecycle in the step method to incorporate the following:

* `Burned Out` trees decay over time. Add a `decay_time` integer parameter to the model. Each tree that is burned should keep track of the time since it was burned. After the `decay_time` has passed, the tree decays, and its condition should be `Empty`.

* `Fine` trees can grow new `Fine` trees in adjacent `Empty` neighbors. When a tree reaches the age of the `lifetime` parameter, the tree will try to change up to two adjacent `Empty` spaces into `Fine` trees, and set their age to 0. Then, the tree will change its own condition to `Empty`.


### Visualization

Visualize your results using `mesa runserver` or `python run.py`. Add sliders for `decay_time` and `lifetime`. Identify a set of parameters and/or initial conditions that create an interesting visualization that highlights all of the model's behavior. Take some screen shots of your visualization to turn in with your report. 


### Analysis

Using [Forest Fire Notebook](https://nbviewer.org/github/Hendrix-CS/csci285/blob/master/assets/notebooks/Forest%20Fire%20Model.ipynb) for reference, create a notebook to re-run model simulations and perform a parameter sweep over `decay_time` from 0 to 60 with a step size of 2. Run each parameter choice 4 times. Set the other parameters, such as density and lifetime, to the interesting values you determined through visualizing your model.

 Determine the effect of changing this parameter on the number of `Fine` trees after 200 time steps.


## Step 2 - Diffusion and Wind

[Diffusion Mesa Model](https://github.com/wilsojb/diffusion-mesa/archive/refs/heads/master.zip) demonstrates diffusion and evaporation of a pollutant (from factories) in an environment. Download this model and visualize it using `mesa runserver` or `python run.py`. Read through the README to understand the model parameters and agent rules.

Alter the code such that the pollutant from the factory can be affected by a breeze from West to East. This breeze should be controlled by a parameter between 0 and 1 called `wind_strength`. 

Visualize your model using `mesa runserver` or `python run.py`. Add a slider for `wind_strength`. Take some screen shots of your visualization to turn in with your report.

Justify your choice of implementation and changes to the base model code.

### `mesa.time.SimultaneousActivation`

Notice that this simulation makes use of a different scheduler than forest fire (i.e. `mesa.time.RandomActivation`). Research these two schedulers on [https://mesa.readthedocs.io/en/latest/apis/time.html](https://mesa.readthedocs.io/en/latest/apis/time.html) and compare how each works by reviewing the differences between forest fire and the diffusion simulation.


## Step 3 - Ant Parameter Tweaking

[Ant Phereomone Model](https://github.com/wilsojb/ants-mesa/archive/refs/heads/master.zip) demonstrates ants communicating about food stores using pheromone diffusion. Download this model and visualize it using `mesa runserver` or `python run.py`. Read through the README to understand the model parameters and agent rules.

You should notice that the parameters for this model are very inadequate for effective communication. Find a reasonable set of parameters that allow the ants to quickly find the food and gather it all to their home. 

Use the Notebook included in the model to visualize a graph of the food collection using your optimized parameters.


## Step 4 - Termite Modeling

Create a new agent-based model to study the collective behavior of [termites](http://en.wikipedia.org/wiki/Termite). In particular, you will be modeling how termites organize to build large structures without a leader. There will be two types of agents in the world, `Termite` and `Environment`.

{% include tip.html content="Look to the Forest Fire
model for how to get started." %}

### Environment

The `Environment` of the world will have two states, `DIRT` and `EMPTY`. Make the `DIRT` tate appear yellow, and the `EMPTY` state be black. In this model, the `Environment` will not need to update its state, only hold information for the `Termite` class to manipulate.


### Termite

We will use three states to model our `Termite` behavior, `FORAGE`, `LOOK`, and `DROP`.

* When a `Termite` is in the `FORAGE` state, they wander randomly around the world. If they step on top of an `Environment` cell that contains `DIRT`, they pick it up by making their current cell `EMTPY`, and change their own state to `LOOK`.

* In the `LOOK` state, the `Termite` is looking for another piece of `DIRT`. They will again wander around the world randomly until they are standing on a cell with `DIRT`. When this happens, they change their state to `DROP`.

* Finally, a `Termite` in the `DROP` state is now looking for an `EMPTY` `Environment` cell in the world. They wander randomly until they find this `EMPTY` cell, then put their `DIRT` into the cell. They then take 5 random steps, and finally change to the `FORAGE` state. This last piece helps them not to immediately pick up the piece of `DIRT` they just dropped.


### Model

Initialize your model with the following parameters

* `height` = 40
* `width` = 40
* `num_dirt` = 200
* `num_termites` = 50

This will make a 40x40 world, with 200 random pieces of the environment selected to be `DIRT`, and with 50 `Termite` agents, placed them randomly in the world to start.

Call the step method of the scheduler, and make sure to stop the model from running if the scheduler time is greater than 200.

Following the Forest Fire and Ant models above, write a `server.py` that will allow you to visualize your termites. Use the `ant.png` file to display a termite on the screen. You do not need to create sliders, but are welcome to do so if you want.

Visualize your model using the `mesa runserver` method to display the grid.

### BONUS - Counting Piles

We would like to know how the number of piles changes over time. We can define a pile as a connected group of pieces of `DIRT`. To count the piles, we can implement the following algorithm as a static method in the model:

* initialize a boolean array the same size as the grid called `marking`.
* set everywhere in `marking` to `False`.
* examine each space in the grid systematically, row by column.
* if a grid space with a piece of `DIRT` is found, and the corresponding spot in `marking` is `False`
    * increment the number of piles
    * starting here, perform a recursive search to find the extent of the pile.
        * for each orthogonal neighbor (N, E, S, W) that is a piece of `DIRT` and is marked `False`
            * mark it to be `True`.
            * recursively search its neighbors.

### BONUS - Evaluation

Perform a parameter sweep on `num_termites`, from 20 to 80, incrementing by 5, running each parameter choice 4 times, and record the number of piles at the end of the simulation.

Include in your writeup screen shots from the start and end of your model. Describe what you see in terms of the formation of piles of dirt.


## What To Turn In

As you work on this lab, record all of your progress in a Jupyter notebook. Record your solutions and attempts in `Code` blocks, and annotate what you did with `MarkDown` blocks. Cite all the webpages you find and use in your search for your solution. A good solution should read like a self-contained report.

* Add your name and your lab partner at the top of the notebook. 

* [https://dillinger.io/](https://dillinger.io/) for good `MarkDown` styling.

* [Overleaf](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) for good `LaTeX` styling.

* Go to the file menu and do "Kernel -> Restart and Run All" before submitting. This ensures there are no runtime errors and all figures are generated correctly.


## Grading

* Complete: Notebook can be read easily w/o needing to reference this page for additional detail. It should read like a self-contained report. It can be executed without producing runtime errors. All steps (1-4) are finished and all discussion questions are answered.

* Partially complete: Notebook can be executed without producing runtime errors. Steps (1-4) are attempted.

* Bonus: If you complete (correctness counts!) the two bonus sections of termite modeling, then you can get 15 additional points added to your Exam #2 grade. this is enough to turn a "B" into an "A".
