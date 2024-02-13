from matplotlib import pyplot as plt
import math


class MovingPoint:
    def __init__(self, initPositionIndex, initColor):
        self.positionIndex = initPositionIndex
        self.color = initColor
        self.hasBeenMoved = False


class TheCube:
    def __init__(self):
        self.points = CreateAllPoints()


def PlotAllPoints(currAx, points, delayVal, plotPointNum):
    pointPositions = ReturnPositions()
    counterNum = 0
    for point in points:
        currAx.scatter(pointPositions[point.positionIndex][0], pointPositions[point.positionIndex][1], color=point.color)
        if plotPointNum:
            currAx.text(pointPositions[point.positionIndex][0], pointPositions[point.positionIndex][1], str(counterNum), verticalalignment='bottom', horizontalalignment='right')
        counterNum += 1
        if delayVal > 0:
            plt.pause(delayVal)
    plt.show()


def Rotate(points, circleNum, CW):
    allMovements = ReturnCircleMovements()
    movements = allMovements[circleNum]
    for move in movements:
        for point in points:
            if move[CW] == point.positionIndex and point.hasBeenMoved is False:
                if point.positionIndex == 0:
                    ReturnAngleOneAndAngleTwo(point.positionIndex, move[not CW], circleNum)

                point.positionIndex = move[not CW]
                point.hasBeenMoved = True

    for point in points:
        point.hasBeenMoved = False


def CheckIfSolved(points):
    checkIndexNum = 0
    solved = True
    for point in points:
        if point.positionIndex != checkIndexNum:
            return False
        checkIndexNum += 1
    return solved



def ReturnFaces():
    face1 = [0, 1, 2, 3]
    face2 = [4, 5, 6, 7]
    face3 = [8, 9, 10, 11]
    face4 = [12, 13, 14, 15]
    face5 = [16, 17, 18, 19]
    face6 = [20, 21, 22, 23]
    return [face1, face2, face3, face4, face5, face6]



def ReturnPositions():
    return [(0, 126.847103), (-20, 113.720327), (20, 113.720327), (0, 103.700661), (-38.484692, 45.313158),
                 (-59.852814, 34.556038), (-39.807407, 22.982817), (-58.484692, 10.672142), (38.484692, 45.313158),
                 (59.852814, 34.556038), (39.807407, 22.982817), (58.484692, 10.672142), (-108.484692, -39.539656),
                 (-89.807407, -51.850331), (-109.852814, -63.423552), (-88.484692, -74.180672), (0, -45.965634),
                 (-20, -55.9853), (20, -55.9853), (0, -69.112076), (108.484692, -39.539656), (89.807407, -51.850331),
                 (109.852814, -63.423552), (88.484692, -74.180672)]


def CreateAllPoints():
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

    return [red1, red2, red3, red4, blue1, blue2, blue3, blue4, green1, green2, green3, green4, purple1, purple2,
                 purple3, purple4, yellow1, yellow2, yellow3, yellow4, cyan1, cyan2, cyan3, cyan4]


def ReturnCircleMovements():
    rotateCircle1CCW = [(0, 15), (2, 14), (15, 18), (14, 19), (18, 9), (19, 11), (9, 0), (11, 2), (21, 20), (20, 22),
                        (22, 23), (23, 21)]
    rotateCircle2CCW = [(1, 13), (3, 12), (13, 16), (12, 17), (16, 8), (17, 10), (8, 1), (10, 3), (4, 5), (5, 7),
                        (7, 6), (6, 4)]
    rotateCircle3CCW = [(0, 5), (1, 7), (5, 17), (7, 19), (17, 23), (19, 22), (23, 0), (22, 1), (13, 15), (15, 14),
                        (14, 12), (12, 13)]
    rotateCircle4CCW = [(2, 4), (3, 6), (4, 16), (6, 18), (16, 21), (18, 20), (21, 2), (20, 3), (9, 8), (8, 10),
                        (10, 11), (11, 9)]
    rotateCircle5CCW = [(4, 12), (5, 14), (12, 22), (14, 20), (22, 9), (20, 8), (9, 4), (8, 5), (2, 3), (3, 1), (1, 0),
                        (0, 2)]
    rotateCircle6CCW = [(6, 13), (7, 15), (13, 23), (15, 21), (23, 11), (21, 10), (11, 6), (10, 7), (16, 17), (17, 19),
                        (19, 18), (18, 16)]

    return [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW, rotateCircle4CCW, rotateCircle5CCW, rotateCircle6CCW]


def ReturnCircleCoordsAndRadii():
    majorCirclesCenters = [(-50, 28.867513), (-50, 28.867513), (0, -57.735027), (0, -57.735027), (50, 28.867513),
                                (50, 28.867513)]
    majorCirclesRadii = [110, 90, 110, 90, 110, 90]
    return majorCirclesCenters, majorCirclesRadii


def ReturnAngleOneAndAngleTwo(index1, index2, currMajorCircleCenter):
    positions = ReturnPositions()

    circleCenter = ReturnCircleCoordsAndRadii()[0][currMajorCircleCenter]
    angle1 = math.atan2(positions[index1][1] - circleCenter[1],
                        positions[index1][0] - circleCenter[0])
    angle2 = math.atan2(positions[index2][1] - circleCenter[1],
                        positions[index2][0] - circleCenter[0])

    if angle1 < 0:
        angle1 = (2 * math.pi) - angle1
    if angle2 < 0:
        angle2 = (2 * math.pi) - angle2


    return angle1, angle2



# majorCirclesCentersOuter = [(-50, 28.867513), (-50, 28.867513), (0, -57.735027), (0, -57.735027), (50, 28.867513), (50, 28.867513)]
# majorCirclesRadiiOuter = [110, 90, 110, 90, 110, 90]

# positions defined by coordinates. Faces defined by indices of coordinates. rotatingCircleX moves from index 0 to 1 in tuple, defining movement rotations for any rotation. Clockwise rotations just flip 1 to 0
# positions = [(0, 126.847103), (-20, 113.720327), (20, 113.720327), (0, 103.700661), (-38.484692, 45.313158), (-59.852814, 34.556038), (-39.807407, 22.982817), (-58.484692, 10.672142), (38.484692, 45.313158), (59.852814, 34.556038), (39.807407, 22.982817), (58.484692, 10.672142), (-108.484692, -39.539656), (-89.807407, -51.850331), (-109.852814, -63.423552), (-88.484692, -74.180672), (0, -45.965634), (-20, -55.9853), (20, -55.9853), (0, -69.112076), (108.484692, -39.539656), (89.807407, -51.850331), (109.852814, -63.423552), (88.484692, -74.180672)]

# rotateCircle1CCW = [(0, 15), (2, 14), (15, 18), (14, 19), (18, 9), (19, 11), (9, 0), (11, 2), (21, 20), (20, 22), (22, 23), (23, 21)]
# rotateCircle2CCW = [(1, 13), (3, 12), (13, 16), (12, 17), (16, 8), (17, 10), (8, 1), (10, 3), (4, 5), (5, 7), (7, 6), (6, 4)]
# rotateCircle3CCW = [(0, 5), (1, 7), (5, 17), (7, 19), (17, 23), (19, 22), (23, 0), (22, 1), (13, 15), (15, 14), (14, 12), (12, 13)]
# rotateCircle4CCW = [(2, 4), (3, 6), (4, 16), (6, 18), (16, 21), (18, 20), (21, 2), (20, 3), (9, 8), (8, 10), (10, 11), (11, 9)]
# rotateCircle5CCW = [(4, 12), (5, 14), (12, 22), (14, 20), (22, 9), (20, 8), (9, 4), (8, 5), (2, 3), (3, 1), (1, 0), (0, 2)]
# rotateCircle6CCW = [(6, 13), (7, 15), (13, 23), (15, 21), (23, 11), (21, 10), (11, 6), (10, 7), (16, 17), (17, 19), (19, 18), (18, 16)]


# red1 = MovingPoint(0, '#b80a31')
# red2 = MovingPoint(1, '#b80a31')
# red3 = MovingPoint(2, '#b80a31')
# red4 = MovingPoint(3, '#b80a31')
#
# blue1 = MovingPoint(4, '#0044af')
# blue2 = MovingPoint(5, '#0044af')
# blue3 = MovingPoint(6, '#0044af')
# blue4 = MovingPoint(7, '#0044af')
#
# green1 = MovingPoint(8, '#009c46')
# green2 = MovingPoint(9, '#009c46')
# green3 = MovingPoint(10, '#009c46')
# green4 = MovingPoint(11, '#009c46')
#
# purple1 = MovingPoint(12, 'm')
# purple2 = MovingPoint(13, 'm')
# purple3 = MovingPoint(14, 'm')
# purple4 = MovingPoint(15, 'm')
#
# yellow1 = MovingPoint(16, '#ffd600')
# yellow2 = MovingPoint(17, '#ffd600')
# yellow3 = MovingPoint(18, '#ffd600')
# yellow4 = MovingPoint(19, '#ffd600')
#
# cyan1 = MovingPoint(20, '#ff5700')
# cyan2 = MovingPoint(21, '#ff5700')
# cyan3 = MovingPoint(22, '#ff5700')
# cyan4 = MovingPoint(23, '#ff5700')
#
# allPoints = [red1, red2, red3, red4, blue1, blue2, blue3, blue4, green1, green2, green3, green4, purple1, purple2, purple3, purple4, yellow1, yellow2, yellow3, yellow4, cyan1, cyan2, cyan3, cyan4]

# rotations = ReturnCircleMovements()
# allPoints = CreateAllPoints()
# majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()

# axisLimits = 200
# fig, ax = plt.subplots()
# ax.axis('equal')
# ax.set_xlim(-axisLimits, axisLimits)
# ax.set_ylim(-axisLimits, axisLimits)
# ax.set_xticks([])
# ax.set_yticks([])
# plt.ion()
#
#
# for i in range(len(majorCirclesCenters)):
#     currCircle = plt.Circle(majorCirclesCenters[i], majorCirclesRadii[i], color='k', fill=False)
#     ax.add_patch(currCircle)
#
# PlotAllPoints(ax, allPoints, 0, False)
# Rotate(allPoints, 5, True)
# Rotate(allPoints, 1, True)
# Rotate(allPoints, 1, False)
# Rotate(allPoints, 5, False)
#
# print(CheckIfSolved(allPoints))
# plt.ioff()
# PlotAllPoints(ax, allPoints, 0, False)
