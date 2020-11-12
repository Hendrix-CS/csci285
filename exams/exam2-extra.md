---
layout: work
type: Exam
num: 2
worktitle: Painters
---

## Description

These questions can be attempted to recover points on exam 2.

## Chemical Reaction

![Neuron Diagram](../assets/images/neuron.png){: .pull-right .w-50 .img-fluid}

One piece of [computational neuroscience](https://en.wikipedia.org/wiki/Computational_neuroscience) involves the simulation of individual neurons.
Mathematical models with differential equations can be written to capture the
flow of chemicals across neurons and emulate the spiking and bursting behavior
over time.

One of the more straight-forward [biological neuron models](https://en.wikipedia.org/wiki/Biological_neuron_model) is the [Hindmarsh-Rose](https://en.wikipedia.org/wiki/Hindmarsh%E2%80%93Rose_model). Three variables, `x`, `y`,
and `z` capture pieces of the membrane and ion channels, with `x` showing the
spiking of the neuron activation over time.

### Step 1

Write a function to implement the Hindmarsh-Rose neuron model so that it can be
simulated using the Runga-Kutta 4 method we implemented in class. Use the equations
and recommended parameters from the Wikipedia page linked above for `a`, `b`, `c`, `d`, `r`, `s`, and `x_R`.

### Step 2

Run a simulation of your function for 2000 timesteps, using a `dt` of 0.01, and let `I` equal 2. Use [1, 1, 2] as your initial values for `x`, `y`, and `z`.
Plot the trajectory of the `x` variable over time, and discuss what you observe.

### Step 3

Run a simulation of your function for 2000 timesteps, using a `dt` of 0.01, and let `I` equal 1. Use [1, 1, 2] as your initial values for `x`, `y`, and `z`.
Plot the trajectory of the `x` variable over time, and discuss what you observe.

### Step 4

Run a simulation of your function for 2000 timesteps, using a `dt` of 0.01, and let `I` alternate between 1 and 2 every 400 timesteps. Use [1, 1, 2] as your initial values for `x`, `y`, and `z`.
Plot the trajectory of the `x` variable over time, and discuss what you observe.

## Painters

### Step 5

You are an artist interested in creating collaborative abstract art. You have hired the painters to paint the world and make paintings for you.

* Create an agent class called Environment to store the color of each cell in the world. This agent has one property, their color, which is initially "GREEN".

* Create an agent class called Painter which will wander the world and paint the Environment. This agent has one property, their color, which is initially "GREEN". In their step function, they should randomly wander around the world.

* Set up the model to have height of 50 and width of 50, with an Environment cell in each coordinate.

* Add to your model 30 Painters in each of two colors, red and white. These Painters should be placed randomly in the world.

### Step 6

You must next add code to have the turtles paint the world. The turtles follow a simple rule: if they see an empty (green) patch, paint it with their own color, then wiggle. You need to
Draw a state transition diagram to describe this behavior.
Create a Wiggle procedure
Create a Paint procedure (use an if statement)
Add a forever block that includes these two procedures
Run this model and report on the resulting painting in the world.

Question 3
You hire another set of turtles, but they are not entirely reliable. As before, if they see a green patch, they color it with their color, but if they see a patch that is already colored but is not their own color, they change into that color and start painting with this new color. For example, a red turtle encounters a white patch, causing it to become a white turtle. This turtle is now painting green patches white.
Draw a state transition diagram to describe this behavior.
Create a Paint2 procedure (use if statements)
Replace Paint with Paint2 in your forever block
Run this model. Discuss any differences between the paintings from the turtles in Question 2 and Question 3.

Question 4
You hire a third set of turtles, which follow a slightly different set of rules. If they encounter a green patch, they paint it their color, but if they encounter a colored patch that is not their own, they first change into that color then color this patch green. For example, a red turtle encounters a white patch, causing it to become a white turtle and paint the white patch green, and this turtle is now painting green patches white.
Draw a state transition diagram to describe this behavior.
Create a Paint3 procedure (use if statements)
Replace Paint2 with Paint3 in your forever block
Run this model. Discuss any differences between this model and the models in Questions 2 and Questions 3. Why do you think this model behaves the way it does? Which pictures do you prefer and why?



## Handin and Grading

Turn in your Jupyter Notebooks, and the zip of the Painter project, on Moodle in the Exam 2 folder.

{% include important.html content="Add readable labels to your axes,
include a title for each graph you generate, discuss your results,
and cite all of your references and resources used to complete
this exam." %}
