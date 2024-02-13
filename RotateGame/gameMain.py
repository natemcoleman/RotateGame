import TwoMain
from matplotlib import pyplot as plt

rotations = TwoMain.ReturnCircleMovements()
allPoints = TwoMain.CreateAllPoints()
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

TwoMain.PlotAllPoints(ax, allPoints, 0, False)
TwoMain.Rotate(allPoints, 5, True)
TwoMain.Rotate(allPoints, 1, True)
TwoMain.Rotate(allPoints, 1, False)
TwoMain.Rotate(allPoints, 5, False)

print(TwoMain.CheckIfSolved(allPoints))
plt.ioff()
TwoMain.PlotAllPoints(ax, allPoints, 0, False)











