# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import lang_ant

"""
Langton's Ant

Created on 2021-04-25

@author: Rick
"""

# ask for the rules string and create a dictionary of rules for the ant

"""
    Langton's Ant is Turing complete because the ant can move back and forth
    and can read and write.  Using this behaviour you can set up an initial
    state for the ant to simulate logic gates and have the ant run any program
    for you.
"""

# rules strings: LR = basic ant
#                RLR = Chaos
#                LRRRRRLLR = fills grid
#                RLRLRLRLRLR = quicker highway
accept = "RL"
rule_string = ""
while rule_string == "" or not all(c in accept for c in rule_string):
    rule_string = input("Enter rule string: ")

rules = dict((k, v) for k, v in enumerate(rule_string))
num_rules = len(rule_string)

# create ant and lattice
N = 128
midpoint = N // 2
ant = lang_ant.Ant(midpoint, midpoint, 'W')
lattice = lang_ant.LangAnt(ant, rules, N)

cells = lattice.getStates()  # initial state

# -------------------------------
# plot cells
fig = plt.figure()

img = plt.imshow(cells, cmap="gnuplot2", vmin=0, vmax=(num_rules - 1), animated=True)


def animate(i):
    """perform animation step"""
    global lattice

    lattice.step()
    cells_updated = lattice.getStates()

    img.set_array(cells_updated)

    return img,


interval = 0  # ms

# animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
