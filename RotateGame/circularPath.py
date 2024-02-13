from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math


def ReturnAngleOneAndAngleTwo(positions1, index1, positions2, index2, currMajorCircleCenter):
    angle1 = math.atan2(positions1[index1][1]-currMajorCircleCenter[1], positions1[index1][0]-currMajorCircleCenter[0])
    angle2 = math.atan2(positions2[index2][1]-currMajorCircleCenter[1], positions2[index2][0]-currMajorCircleCenter[0])
    print("point 1:", positions1[index1])
    print("point 2:", positions2[index2])
    print("circleCenter:", currMajorCircleCenter)

    if angle1 < 0:
        angle1 = (2*math.pi)-angle1
    if angle2 < 0:
        angle2 = (2*math.pi)-angle2

    return math.degrees(angle1), math.degrees(angle2)


def AnimateCircle(fig, circleCenters, circleRadii, angles, colors, fixedList, fixedColors,  majorCirclesCenters, majorCirclesRadii):
    for i in range(len(majorCirclesCenters)):
        currCircle = plt.Circle(majorCirclesCenters[i], majorCirclesRadii[i], color='k', fill=False)
        ax.add_patch(currCircle)

    for i in range(len(fixedList)):
        for j in range(len(fixedList[i])):
            ax.scatter(fixedList[i][j][0], fixedList[i][j][1], color=fixedColors[i], marker='o')  # Adjust marker size (s) as needed

    def circle(t, center, radius):
        x = radius * np.cos(t) + center[0]
        y = radius * np.sin(t) + center[1]
        return x, y

    def animation_function(frame):
        for i in range(len(circleRadii)):
            x_point, y_point = circle(t[i][frame], circleCenters[i], circleRadii[i])

            points[i].set_xdata([x_point])
            points[i].set_ydata([y_point])

    t = []
    for item in angles:
        t.append(np.linspace(math.radians(item[0]), math.radians(item[1]), 100))

    # Since plotting a single graph
    points = []
    for item in colors:
        line, = ax.plot(axisLimits/2, axisLimits/2, 'o', color=item)
        points.append(line)
    # center = [axisLimits/2, axisLimits/2]

    animation = FuncAnimation(fig=fig, func=animation_function, frames=len(t[0]), interval=0.1, repeat=False)
    plt.show()


axisLimits = 200

figure, ax = plt.subplots()
ax.axis('equal')
ax.set_xlim(-axisLimits, axisLimits)
ax.set_ylim(-axisLimits, axisLimits)
ax.set_xticks([])
ax.set_yticks([])

fixedList1 = [(20, 113.720327), (0, 103.700661), (0, 126.847103), (-20, 113.720327)]
fixedList2 = [(38.484692, 45.313158), (39.807407, 22.982817), (59.852814, 34.556038), (58.484692, 10.672142)]
fixedList3 = [(-38.484692, 45.313158), (-39.807407, 22.982817), (-59.852814, 34.556038), (-58.484692, 10.672142)]
fixedList4 = [(-108.484692, -39.539656), (-89.807407, -51.850331), (-109.852814, -63.423552), (-88.484692, -74.180672)]
fixedList5 = [(108.484692, -39.539656), (89.807407, -51.850331), (109.852814, -63.423552), (88.484692, -74.180672)]
fixedList6 = [(0, -45.965634), (-20, -55.9853), (20, -55.9853), (0, -69.112076)]
majorCirclesCentersOuter = [(-50, 28.867513), (-50, 28.867513), (0, -57.735027), (0, -57.735027), (50, 28.867513), (50, 28.867513)]
majorCirclesRadiiOuter = [110, 90, 110, 90, 110, 90]

fixedListOuter = [fixedList1, fixedList2, fixedList3, fixedList4, fixedList5, fixedList6]
fixedColorsOuter = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0.5, 0.5), (0.5, 0, 0.5), (0.5, 0.5, 0)]

circleRadius1 = 110
angles1 = (50.48, 237.04)
circleCenter1 = (-50, 28.867513)
color1 = (1, 0, 0)

checkAngle1 = ReturnAngleOneAndAngleTwo(fixedList1, 2, fixedList4, 2, majorCirclesCentersOuter[0])
print("Correct angles:", angles1[0], " ", angles1[1], " Found angle:", checkAngle1)

circleRadius2 = 110
angles2 = (62.96, 249.52)
circleCenter2 = (-50, 28.867513)
color2 = (1, 0, 0)

anglesOuter = [angles1, angles2]
circleRadiiOuter = [circleRadius1, circleRadius2]
circleCentersOuter = [circleCenter1, circleCenter2]
colorsOuter = [color1, color2]

AnimateCircle(figure, circleCentersOuter, circleRadiiOuter, anglesOuter, colorsOuter, fixedListOuter, fixedColorsOuter, majorCirclesCentersOuter, majorCirclesRadiiOuter)

