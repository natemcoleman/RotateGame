from matplotlib import pyplot as plt
import math
import numpy as np
import random


class MovingPoint:
    def __init__(self, initPositionIndex, initColor):
        self.positionIndex = initPositionIndex
        self.color = initColor
        self.hasBeenMoved = False


class TheCube:
    def __init__(self):
        self.points = CreateAllPoints()


def PlotAllPoints(currAx, points, delayVal, plotPointNum):
    currAx.clear()
    currAx.axis('equal')
    currAx.set_xticks([])
    currAx.set_yticks([])
    plt.ion()
    majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()
    colors = ReturnColors()
    for i in range(len(majorCirclesCenters)):
        currCircle = plt.Circle(majorCirclesCenters[i], majorCirclesRadii[i], color='k', fill=False)
        currAx.add_patch(currCircle)
        addDist = majorCirclesRadii[i]*0.707
        if i < 2:
            currAx.text(majorCirclesCenters[i][0]-addDist, majorCirclesCenters[i][1]+addDist, str(i+1),
                        verticalalignment='bottom', horizontalalignment='right')
        elif i < 4:
            currAx.text(majorCirclesCenters[i][0] + addDist, majorCirclesCenters[i][1] + addDist, str(i+1))
        else:
            currAx.text(majorCirclesCenters[i][0], majorCirclesCenters[i][1] - majorCirclesRadii[i], str(i+1))

    pointPositions = ReturnPositions()
    counterNum = 0
    for point in points:
        currAx.scatter(pointPositions[point.positionIndex][0], pointPositions[point.positionIndex][1], color=colors[point.color], linewidths=5)
        if plotPointNum:
            currAx.text(pointPositions[point.positionIndex][0], pointPositions[point.positionIndex][1], str(counterNum), verticalalignment='bottom', horizontalalignment='right')
        counterNum += 1
        if delayVal > 0:
            plt.pause(delayVal)
    plt.show()


def ResetPoints(points):
    for pointIndex in range(len(points)):
        points[pointIndex].positionIndex = pointIndex


def Rotate(points, circleNum, CW):
    allMovements = ReturnCircleMovements()
    movements = allMovements[circleNum]
    for move in movements:
        for point in points:
            if move[CW] == point.positionIndex and point.hasBeenMoved is False:
                point.positionIndex = move[not CW]
                point.hasBeenMoved = True

    for point in points:
        point.hasBeenMoved = False


def CheckIfFaceIsSolved(faceIndex, points):
    solved = True

    face = ReturnFaces()[faceIndex]
    currFaceColors = []
    for faceIndex in face:
        for point in points:
            if point.positionIndex == faceIndex:
                currFaceColors.append(point.color)
    if not all(element == currFaceColors[0] for element in currFaceColors):
        return False

    return solved


def CheckIfSolved(points):
    solved = True

    for i in range(6):
        faceSolvedBool = CheckIfFaceIsSolved(i, points)
        if not faceSolvedBool:
            return False

    print("SOLVED!")
    return solved


def FindFaceWithMaxSameColor(points):
    faces = ReturnFaces()
    maxColorsOnFace = 0
    elementsOnMaxFace = []
    elementCountsOnMaxFace = []
    facesIndex = 0
    maxFacesIndex = -1
    for face in faces:
        currFaceColors = []
        for faceIndex in face:
            for point in points:
                if point.positionIndex == faceIndex:
                    currFaceColors.append(point.color)

        elements = []
        element_counts = []

        for currColor in currFaceColors:
            if currColor in elements:
                index = elements.index(currColor)
                element_counts[index] += 1
            else:
                elements.append(currColor)
                element_counts.append(1)
        if max(element_counts) > maxColorsOnFace:
            maxColorsOnFace = max(element_counts)
            elementsOnMaxFace = elements
            elementCountsOnMaxFace = element_counts
            maxFacesIndex = facesIndex
        facesIndex += 1

    maxColorNum = elementsOnMaxFace[elementCountsOnMaxFace.index(max(elementCountsOnMaxFace))]
    return maxFacesIndex, maxColorNum


def ReturnCubeSidesBasedOnMainColor(maxFacesIndex):
    # 0 - R = The right face
    # 1 - L = The left face
    # 2 - U = The top face
    # 3 - D = The bottom face
    # 4 - F = The face at the front
    # 5 - B = The face at the back
    face1Option = [4, 3, 5, 1, 2, 6]
    face2Option = [5, 1, 6, 2, 4, 3]
    face3Option = [2, 6, 4, 3, 1, 5]
    face4Option = [6, 2, 3, 4, 5, 1]
    face5Option = [6, 2, 1, 5, 3, 4]
    face6Option = [3, 4, 2, 6, 1, 5]

    returnFaces = [face1Option, face2Option, face3Option, face4Option, face5Option, face6Option]

    return returnFaces[maxFacesIndex]


def SolveCube(points):
    # 0 - R = The right face
    # 1 - L = The left face
    # 2 - U = The top face
    # 3 - D = The bottom face
    # 4 - F = The face at the front
    # 5 - B = The face at the back

    faceWithMaxColorIndex, maxColor = FindFaceWithMaxSameColor(points)
    faces = ReturnFaces()
    # faceWithMaxColor = faces[faceWithMaxColorIndex]
    # faceRelationsBasedOnMaxFace = ReturnCubeSidesBasedOnMainColor(faceWithMaxColorIndex)
    # print("The right face is face ", faceRelationsBasedOnMaxFace[0])
    # print("The left face is face ", faceRelationsBasedOnMaxFace[1])
    # print("The top face is face ", faceRelationsBasedOnMaxFace[2])
    # print("The bottom face is face ", faceRelationsBasedOnMaxFace[3])
    # print("The front face is face ", faceRelationsBasedOnMaxFace[4])
    # print("The back face is face ", faceRelationsBasedOnMaxFace[5])
    # print("faceWithMaxColor:", faceWithMaxColor)
    nit = 0
    numFacesSolved = 0
    # while not CheckIfFaceIsSolved(0, points) or not CheckIfFaceIsSolved(1, points):
    while not CheckIfFaceIsSolved(faceWithMaxColorIndex, points):
        Rotate(points, random.randint(0, 5), random.randint(0, 1))
        nit += 1
    print(nit)
    print("Face ", faceWithMaxColorIndex, " is solved:", CheckIfFaceIsSolved(faceWithMaxColorIndex, points))


def FullyRandomizeCube(points):
    newIndices = list(range(len(points)))

    random.shuffle(newIndices)
    for pointIndex in range(len(points)):
        points[pointIndex].positionIndex = newIndices[pointIndex]


def RandomizeCube(points, numRandomRotations):
    random_values = [random.randint(0, 5) for _ in range(numRandomRotations)]
    random_bools = [random.choice([True, False]) for _ in range(numRandomRotations)]

    for randomIndex in range(numRandomRotations):
        Rotate(points, random_values[randomIndex], random_bools[randomIndex])
        print("Circle:", random_values[randomIndex]+1, " CW:", random_bools[randomIndex])


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


def ReturnColors():
    return ['#b80a31', '#0044af', '#009c46', 'm', '#ffd600', '#ff5700']


def CreateAllPoints():
    red1 = MovingPoint(0, 0)
    red2 = MovingPoint(1, 0)
    red3 = MovingPoint(2, 0)
    red4 = MovingPoint(3, 0)

    blue1 = MovingPoint(4, 1)
    blue2 = MovingPoint(5, 1)
    blue3 = MovingPoint(6, 1)
    blue4 = MovingPoint(7, 1)

    green1 = MovingPoint(8, 2)
    green2 = MovingPoint(9, 2)
    green3 = MovingPoint(10, 2)
    green4 = MovingPoint(11, 2)

    purple1 = MovingPoint(12, 3)
    purple2 = MovingPoint(13, 3)
    purple3 = MovingPoint(14, 3)
    purple4 = MovingPoint(15, 3)

    yellow1 = MovingPoint(16, 4)
    yellow2 = MovingPoint(17, 4)
    yellow3 = MovingPoint(18, 4)
    yellow4 = MovingPoint(19, 4)

    cyan1 = MovingPoint(20, 5)
    cyan2 = MovingPoint(21, 5)
    cyan3 = MovingPoint(22, 5)
    cyan4 = MovingPoint(23, 5)

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
    majorCirclesCenters = [(-50, 28.867513), (-50, 28.867513), (50, 28.867513), (50, 28.867513), (0, -57.735027), (0, -57.735027)]
    majorCirclesRadii = [110, 90, 110, 90, 110, 90]
    return majorCirclesCenters, majorCirclesRadii


# def ReturnAngleOneAndAngleTwo(index1, index2, currMajorCircleCenter):
#     positions = ReturnPositions()
#
#     circleCenter = ReturnCircleCoordsAndRadii()[0][currMajorCircleCenter]
#     angle1 = math.atan2(positions[index1][1] - circleCenter[1],
#                         positions[index1][0] - circleCenter[0])
#     angle2 = math.atan2(positions[index2][1] - circleCenter[1],
#                         positions[index2][0] - circleCenter[0])
#
#     if angle1 < 0:
#         angle1 = (2 * math.pi) - angle1
#     if angle2 < 0:
#         angle2 = (2 * math.pi) - angle2
#
#     return angle1, angle2

