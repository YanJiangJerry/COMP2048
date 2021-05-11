# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway
import reader

# N = max(128, len(init_array) * 2)
# N = 128
N = 1024
init_point = N // 4

# create the game of life object
life = conway.GameOfLife(N)

# test cases
# life.insertBlinker((0,0))
# life.insertGlider((0, 0))  # works correctly because glider glides as expected
# life.insertGliderGun((0, 0))  # shift the left block right one square

# read from file
f_name = input("Filename: ")
init_array = reader.read_file(f_name)
life.insert_from_file(init_array, (init_point,init_point))

cells = life.getStates()  # initial state

# -------------------------------
# plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)


def animate(i):
    """perform animation step"""
    global life

    life.evolve()
    cellsUpdated = life.getStates()

    img.set_array(cellsUpdated)

    return img,


interval = 20  # ms

# animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
