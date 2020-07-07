---
layout: work
type: Lab
num: 7
worktitle: Agent-Based Modeling
---

## Overview

In this lab, you will use [Mesa](https://github.com/projectmesa/mesa) to
implement an Agent-Based Model to model the collective
behavior of [termites](http://en.wikipedia.org/wiki/Termite).
In particular, you will be modeling how termites organize to build large
structures without a leader.

## Description

There will be two types of agents in the world, `Termite`s and `Environment`.

### Step 1 - Environment

The `Environment` of the world will have two states, `DIRT` and `EMPTY`. Make the `DIRT`
state appear yellow, and the `EMPTY` state be black. In this model,
the `Environment` will not need to update its state, only hold information for the
`Termite` class to manipulate.

{% include tip.html content="Look to the Forest Fire
model for how to get started on the Environment." %}

Initialize your model with the following parameters

* height = 40
* width = 40
* num_dirt = 200

This will make a 40x40 world, with 200 random pieces of the environment selected
to be `DIRT`.

### Step 2 - Termite

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

Create 50 `Termite` agents, and place them randomly in the world to start.

### Step 3 - Sliders

num_dirt

num_termites

## Evaluation

Run your model for 1000 iterations. Write a lab report, including
screen shots from the start and end of your model.
Describe what you see in terms of the formation of piles of dirt.

## Grading

* To earn a 5, demonstrate
* To earn a 10, do the above and
* To earn a 14, do the above and
* To earn a 17, do the above and
* To earn a 20, do the above and
