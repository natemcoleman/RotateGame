import TwoMain
from matplotlib import pyplot as plt
import keyboard

rotations = TwoMain.ReturnCircleMovements()
# allPoints = TwoMain.CreateAllPoints()
theCube = TwoMain.TheCube()

majorCirclesCenters, majorCirclesRadii = TwoMain.ReturnCircleCoordsAndRadii()

axisLimits = 200
fig, ax = plt.subplots()
ax.axis('equal')
ax.set_xlim(-axisLimits, axisLimits)
ax.set_ylim(-axisLimits, axisLimits)
ax.set_xticks([])
ax.set_yticks([])
plt.ion()

for i in range(len(majorCirclesCenters)):
    currCircle = plt.Circle(majorCirclesCenters[i], majorCirclesRadii[i], color='k', fill=False)
    ax.add_patch(currCircle)

delayNum = 2
TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
plt.pause(delayNum)
#
# TwoMain.Rotate(theCube.points, 0, True)
# TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
# plt.pause(delayNum)
# print(TwoMain.CheckIfSolved(theCube.points))
#
# TwoMain.Rotate(theCube.points, 1, True)
# TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
# plt.pause(delayNum)
#
# TwoMain.Rotate(theCube.points, 0, False)
# TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
# plt.pause(delayNum)
#
# TwoMain.Rotate(theCube.points, 4, False)

# print(TwoMain.CheckIfSolved(theCube.points))
# plt.ioff()
# TwoMain.PlotAllPoints(ax, theCube.points, 0, False)

def update_plot(event):
    inputVal = event.key
    if keyboard.is_pressed('c'):
        CWBool = False
    else:
        CWBool = True

    if inputVal != 'c':
        inputVal = int(event.key) - 1

        if inputVal >= 6 or inputVal <= -1:
            plt.close()
        else:
            TwoMain.Rotate(theCube.points, inputVal, CWBool)
            TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
            print("Solved:", TwoMain.CheckIfSolved(theCube.points))
            plt.pause(0.25)

# Connect the update_plot function to keyboard input
plt.connect('key_press_event', update_plot)

while plt.fignum_exists(1):
    plt.waitforbuttonpress()

# Close the plot when done
plt.close()










