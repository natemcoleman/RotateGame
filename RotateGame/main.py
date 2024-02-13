import TwoMain
from matplotlib import pyplot as plt

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

TwoMain.Rotate(theCube.points, 0, True)
TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
plt.pause(delayNum)
print(TwoMain.CheckIfSolved(theCube.points))

TwoMain.Rotate(theCube.points, 1, True)
TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
plt.pause(delayNum)
#
# TwoMain.Rotate(theCube.points, 0, False)
# TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
# plt.pause(delayNum)
#
# TwoMain.Rotate(theCube.points, 4, False)

print(TwoMain.CheckIfSolved(theCube.points))
plt.ioff()
TwoMain.PlotAllPoints(ax, theCube.points, 0, False)











