import TwoMain
from matplotlib import pyplot as plt
import keyboard
import pygame

theCube = TwoMain.TheCube()

fig, ax = plt.subplots()
TwoMain.PlotAllPoints(ax, theCube.points, 0, False)


def update_plot(event):
    inputVal = event.key

    if inputVal == 'r':
        TwoMain.ResetPoints(theCube.points)
        TwoMain.PlotAllPoints(ax, theCube.points, 0, False)

    elif inputVal == 'x':
        numRandomRotations = 3
        TwoMain.RandomizeCube(theCube.points, numRandomRotations)
        TwoMain.PlotAllPoints(ax, theCube.points, 0, False)

    elif inputVal == 'v':
        TwoMain.FullyRandomizeCube(theCube.points)
        TwoMain.PlotAllPoints(ax, theCube.points, 0, False)

    elif inputVal == 'a':
        TwoMain.SolveCube(theCube.points)
        TwoMain.PlotAllPoints(ax, theCube.points, 0, False)

    elif inputVal != ' ':
        inputVal = int(event.key) - 1

        if inputVal >= 6 or inputVal <= -1:
            plt.close()
        else:
            TwoMain.Rotate(theCube.points, inputVal, not keyboard.is_pressed(' '))
            TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
            TwoMain.CheckIfSolved(theCube.points)


plt.connect('key_press_event', update_plot)

while plt.fignum_exists(1):
    plt.waitforbuttonpress()

plt.close()










