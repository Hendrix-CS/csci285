---
layout: work
type: Lab
num: 7
worktitle: Agent-Based Modeling
---

## Overview

In this lab, you will use [Mesa](https://github.com/projectmesa/mesa) to
update and implement a Agent-Based Models related to forest fires,
chemical diffusion, ant pheromone communication, and termite construction.

### Step 1 - Forest Regrowth

* [Forest Fire Notebook](https://nbviewer.jupyter.org/urls/hendrix-cs.github.io/csci285/assets/code/Forest%20Fire%20Model.ipynb)

Add a new state to the tree called `Empty`, and make it the default condition for
new Trees.

Revise the model setup so that an empty Tree is added to every space. Use
the `density` parameter to initialize some Trees to `Fine`.

Add a new parameter to the model called `lifetime` which denotes how long a tree
will live in the model. Each tree when initialized to `Fine` should be given an
age between 0 and `lifetime`.

Continue the
current assumption that all Trees with x == 0 should start `On Fire`.

Change the ending condition of the model step method to be based on if `self.schedule.time` is greater than 200.

Now, revise the Tree lifecycle in the step method to incorporate the following:

* `Burned Out` trees decay over time. Add a `decay_time` integer parameter to the model. Each tree that is burned should keep track of the time since it was burned. After the `decay_time` has passed, the tree decays, and its condition should be `Empty`.
* `Fine` trees can grow new `Fine` trees in adjacent `Empty` neighbors. When
a tree reaches the age of the `lifetime` parameter, the tree will try to change up
to two adjacent `Empty` spaces into `Fine` trees, and set their age to 0.
Then, the tree will change its own condition to `Empty`.

Rerun the model simulations in the Jupyter notebook, and perform a parameter sweep on the `decay_time` parameter from 0 to 60 with a step size of 2, running each parameter choice 4 times. Determine the effect of changing this parameter on the number of `Fine` trees after 200 time steps.

### Step 2 - Diffusion and Wind

* [Diffusion Mesa Model](https://github.com/mgoadric/diffusion-mesa/archive/master.zip)

Alter the Diffusion model above, such that the pollutant from the factory can be affected by a breeze from West to East. This breeze should be controlled by a parameter between 0 and 1 called `wind_strength`.

Visualize your model using the `mesa runserver` method to display the grid.
Justify your choice of implementation and changes to the base model code.

### Step 3 - Ant Parameter Tweaking

* [Ant Phereomone Model](https://github.com/mgoadric/ants-mesa/archive/master.zip)

The above model demonstrates ants communicating about food stores using pheromone diffusion. Download this model and visualize your model using the `mesa runserver` method. You should notice that the parameters for this model are very inadequate for effective communication.

Find a reasonable set of parameters that allow the ants to quickly find the food and gather it all to their home. Use the Notebook included in the model to
visualize a graph of the food collection using your optimized parameters.

### Step 4 - Termite Modeling

Create a new agent-based model to study the collective
behavior of [termites](http://en.wikipedia.org/wiki/Termite).
In particular, you will be modeling how termites organize to build large
structures without a leader.
There will be two types of agents in the world, `Termite` and `Environment`.

{% include tip.html content="Look to the Forest Fire
model for how to get started." %}

#### Environment

The `Environment` of the world will have two states, `DIRT` and `EMPTY`. Make the `DIRT`
state appear yellow, and the `EMPTY` state be black. In this model,
the `Environment` will not need to update its state, only hold information for the
`Termite` class to manipulate.

#### Termite

We will use three states to model our `Termite` behavior, `FORAGE`, `LOOK`, and `DROP`.

* When a `Termite` is in the `FORAGE` state, they wander randomly around the world.
  If they step on top of an `Environment` cell that contains `DIRT`, they pick it up
  by making their current cell `EMTPY`, and change their own state to `LOOK`.

* In the `LOOK` state, the `Termite` is looking for another piece of `DIRT`. They will
  again wander around the world randomly until they are standing on a cell with
  `DIRT`. When this happens, they change their state to `DROP`.

* Finally, a `Termite` in the `DROP` state is now looking for an `EMPTY` `Environment` cell in the
  world. They wander randomly until they find this `EMPTY` cell, then put their
  `DIRT` into the cell. They then take 5 random steps, and finally change to the
  `FORAGE` state. This last piece helps them not to immediately pick up the
  piece of `DIRT` they just dropped.

#### Model

Initialize your model with the following parameters

* `height` = 40
* `width` = 40
* `num_dirt` = 200
* `num_termites` = 50

This will make a 40x40 world, with 200 random pieces of the environment selected
to be `DIRT`, and with 50 `Termite` agents, placed them randomly in the world to start.

Call the step method of the scheduler, and make sure to stop the model from
running if the scheduler time is greater than 200.

Following the Forest Fire and Ant models above,
write a `server.py` that will allow you to
visualize your termites. Use the `ant.png` file to display a termite on the screen.
You do not need to create sliders, but are welcome to do so if you want.

Visualize your model using the `mesa runserver` method to display the grid.

#### Counting Piles

We would like to know how the number of piles changes over time. We can define a
pile as a connected group of pieces of `DIRT`. To count the piles, we can
implement the following algorithm as a static method in the model:

* initialize a boolean array the same size as the grid called `marking`.
* set everywhere in `marking` to `False`.
* examine each space in the grid systematically, row by column.
* if a grid space with a piece of `DIRT` is found, and the corresponding spot in `marking` is `False`
    * increment the number of piles
    * starting here, perform a recursive search to find the extent of the pile.
        * for each orthogonal neighbor (N, E, S, W) that is a piece of `DIRT` and is marked `False`
            * mark it to be `True`.
            * recursively search its neighbors.

#### Evaluation

Perform a parameter sweep on `num_termites`, from 20 to 80, incrementing by 5, running each parameter choice 4 times, and record the number of piles at
the end of the simulation.

Include in your writeup
screen shots from the start and end of your model.
Describe what you see in terms of the formation of piles of dirt.

## Grading

* 10 points for augmenting the forest fire model described in step 1.
* 5 points for adding a wind parameter to diffusion in step 2.
* 5 points for finding good parameters for the ant model through step 3.
* 15 points for writing a termite model in step 4.
* 5 points for well-written explanations of your models and research,
and discussion of each graph throughout.
