from matplotlib import pyplot as plt


class MovingPoint:
    def __init__(self, initPositionIndex, initColor):
        self.positionIndex = initPositionIndex
        self.color = initColor
        self.hasBeenMoved = False


def PlotAllPoints(ax, points, positions, delayVal, majorCirclesCenters, majorCirclesRadii):
    for i in range(len(majorCirclesCenters)):
        currCircle = plt.Circle(majorCirclesCenters[i], majorCirclesRadii[i], color='k', fill=False)
        ax.add_patch(currCircle)
    counterNum = 0
    for point in points:
        ax.scatter(positions[point.positionIndex][0], positions[point.positionIndex][1], color=point.color)
        ax.text(positions[point.positionIndex][0], positions[point.positionIndex][1], str(counterNum), verticalalignment='bottom', horizontalalignment='right')
        counterNum += 1
        if delayVal > 0:
            plt.pause(delayVal)
    plt.show()


def Rotate(points, CCW, movements):
    for move in movements:
        for point in points:
            if CCW:
                if move[0] == point.positionIndex and point.hasBeenMoved is False:
                    point.positionIndex = move[1]
                    point.hasBeenMoved = True
            else:
                if move[1] == point.positionIndex and point.hasBeenMoved is False:
                    point.positionIndex = move[0]
                    point.hasBeenMoved = True
    for point in points:
        point.hasBeenMoved = False


majorCirclesCentersOuter = [(-50, 28.867513), (-50, 28.867513), (0, -57.735027), (0, -57.735027), (50, 28.867513), (50, 28.867513)]
majorCirclesRadiiOuter = [110, 90, 110, 90, 110, 90]

# positions defined by coordinates. Faces defined by indices of coordinates. rotatingCircleX moves from index 0 to 1 in tuple, defining movement rotations for any rotation. Clockwise rotations just flip 1 to 0
positions = [(0, 126.847103), (-20, 113.720327), (20, 113.720327), (0, 103.700661), (-38.484692, 45.313158), (-59.852814, 34.556038), (-39.807407, 22.982817), (-58.484692, 10.672142), (38.484692, 45.313158), (59.852814, 34.556038), (39.807407, 22.982817), (58.484692, 10.672142), (-108.484692, -39.539656), (-89.807407, -51.850331), (-109.852814, -63.423552), (-88.484692, -74.180672), (0, -45.965634), (-20, -55.9853), (20, -55.9853), (0, -69.112076), (108.484692, -39.539656), (89.807407, -51.850331), (109.852814, -63.423552), (88.484692, -74.180672)]
face1 = [0, 1, 2, 3]
face2 = [4, 5, 6, 7]
face3 = [8, 9, 10, 11]
face4 = [12, 13, 14, 15]
face5 = [16, 17, 18, 19]
face6 = [20, 21, 22, 23]
rotateCircle1CounterClockwise = [(0, 15), (2, 14), (15, 18), (14, 19), (18, 9), (19, 11), (9, 0), (11, 2), (21, 20), (20, 22), (22, 23), (23, 21)]
rotateCircle2CounterClockwise = [(1, 13), (3, 12), (13, 16), (12, 17), (16, 8), (17, 10), (8, 1), (10, 3), (4, 5), (5, 7), (7, 6), (6, 4)]
rotateCircle3CounterClockwise = [(0, 5), (1, 7), (5, 17), (7, 19), (17, 23), (19, 22), (23, 0), (22, 1), (13, 15), (15, 14), (14, 12), (12, 13)]
rotateCircle4CounterClockwise = [(2, 4), (3, 6), (4, 16), (6, 18), (16, 21), (18, 20), (21, 2), (20, 3), (9, 8), (8, 10), (10, 11), (11, 9)]
rotateCircle5CounterClockwise = [(4, 12), (5, 14), (12, 22), (14, 20), (22, 9), (20, 8), (9, 4), (8, 5), (2, 3), (3, 1), (1, 0), (0, 2)]
rotateCircle6CounterClockwise = [(6, 13), (7, 15), (13, 23), (15, 21), (23, 11), (21, 10), (11, 6), (10, 7), (16, 17), (17, 19), (19, 18), (18, 16)]

red1 = MovingPoint(0, '#b80a31')
red2 = MovingPoint(1, '#b80a31')
red3 = MovingPoint(2, '#b80a31')
red4 = MovingPoint(3, '#b80a31')

blue1 = MovingPoint(4, '#0044af')
blue2 = MovingPoint(5, '#0044af')
blue3 = MovingPoint(6, '#0044af')
blue4 = MovingPoint(7, '#0044af')

green1 = MovingPoint(8, '#009c46')
green2 = MovingPoint(9, '#009c46')
green3 = MovingPoint(10, '#009c46')
green4 = MovingPoint(11, '#009c46')

purple1 = MovingPoint(12, 'm')
purple2 = MovingPoint(13, 'm')
purple3 = MovingPoint(14, 'm')
purple4 = MovingPoint(15, 'm')

yellow1 = MovingPoint(16, '#ffd600')
yellow2 = MovingPoint(17, '#ffd600')
yellow3 = MovingPoint(18, '#ffd600')
yellow4 = MovingPoint(19, '#ffd600')

cyan1 = MovingPoint(20, '#ff5700')
cyan2 = MovingPoint(21, '#ff5700')
cyan3 = MovingPoint(22, '#ff5700')
cyan4 = MovingPoint(23, '#ff5700')

allPoints = [red1, red2, red3, red4, blue1, blue2, blue3, blue4, green1, green2, green3, green4, purple1, purple2, purple3, purple4, yellow1, yellow2, yellow3, yellow4, cyan1, cyan2, cyan3, cyan4]

axisLimits = 200
fig, ax = plt.subplots()
ax.axis('equal')
ax.set_xlim(-axisLimits, axisLimits)
ax.set_ylim(-axisLimits, axisLimits)
ax.set_xticks([])
ax.set_yticks([])
plt.ion()

PlotAllPoints(ax, allPoints, positions, 0.1, majorCirclesCentersOuter, majorCirclesRadiiOuter)
Rotate(allPoints, True, rotateCircle5CounterClockwise)
plt.ioff()
Rotate(allPoints, False, rotateCircle1CounterClockwise)
Rotate(allPoints, True, rotateCircle1CounterClockwise)
Rotate(allPoints, False, rotateCircle5CounterClockwise)

PlotAllPoints(ax, allPoints, positions, 0.1, majorCirclesCentersOuter, majorCirclesRadiiOuter)

