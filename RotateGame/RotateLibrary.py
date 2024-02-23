import math
import numpy as np
import random
import pygame
import pygame.gfxdraw


class Type22:
    def __init__(self):
        self.circleRadius = 10
        self.numFrames = 50
        self.animationType = 1
        face1 = [0, 1]
        face2 = [2, 3]
        face5 = [4, 6]
        face6 = [5, 7]
        self.faces = [face1, face2, face5, face6]
        self.positions = [(0, 45.825757), (-13.671875, 36.962208), (13.671875, 36.962208), (0, 31.721444), (0, -31.721444),
                    (-13.671875, -36.962208), (13.671875, -36.962208), (0, -45.825757)]
        self.colors = [(184, 10, 49), (0, 68, 175), (0, 156, 70), (255, 0, 255), (255, 214, 0), (255, 87, 0)]

        red1 = MovingPoint(0, 0)
        red2 = MovingPoint(1, 0)
        red3 = MovingPoint(2, 1)
        blue1 = MovingPoint(3, 1)
        yellow3 = MovingPoint(4, 4)
        cyan1 = MovingPoint(5, 5)
        cyan2 = MovingPoint(6, 4)
        cyan3 = MovingPoint(7, 5)
        self.points = [red1, red2, red3, blue1, yellow3, cyan1, cyan2, cyan3]

        rotateCircle1CCW = [(0, 2), (2, 6), (6, 7), (7, 0)]
        rotateCircle2CCW = [(1, 3), (3, 4), (4, 5), (5, 1)]
        rotateCircle4CCW = [(0, 7), (7, 5), (5, 1), (1, 0)]
        rotateCircle5CCW = [(2, 6), (6, 4), (4, 3), (3, 2)]

        self.circleMovements = [rotateCircle1CCW, rotateCircle2CCW, rotateCircle4CCW, rotateCircle5CCW]

        mediumRadius = 75 / 2
        largeRadius = 100 / 2
        rotateCircle1CCW = [(-20, 0, largeRadius), (-20, 0, largeRadius), (-20, 0, largeRadius),
                                (-20, 0, largeRadius), (-20, 0, largeRadius), (-20, 0, largeRadius)]
        rotateCircle2CCW = [(-20, 0, mediumRadius), (-20, 0, mediumRadius), (-20, 0, mediumRadius),
                                (-20, 0, mediumRadius), (-20, 0, mediumRadius), (-20, 0, mediumRadius)]
        rotateCircle4CCW = [(20, 0, largeRadius), (20, 0, largeRadius), (20, 0, largeRadius), (20, 0, largeRadius),
                                (20, 0, largeRadius), (20, 0, largeRadius)]
        rotateCircle5CCW = [(20, 0, mediumRadius), (20, 0, mediumRadius), (20, 0, mediumRadius),
                                (20, 0, mediumRadius), (20, 0, mediumRadius), (20, 0, mediumRadius)]

        self.circleMovementRotations = [rotateCircle1CCW, rotateCircle2CCW, rotateCircle4CCW, rotateCircle5CCW]

        majorCirclesCenters = [(-20, 0), (-20, 0), (20, 0), (20, 0)]
        majorCirclesRadii = [largeRadius, mediumRadius, largeRadius, mediumRadius]
        self.circleCoordsAndRadii = majorCirclesCenters, majorCirclesRadii


class Type23:
    def __init__(self):
        self.circleRadius = 8
        self.numFrames = 50
        self.animationType = 1
        face1 = [0, 1, 4]
        face2 = [2, 3, 6]
        face3 = [5, 7, 8]
        face4 = [9, 11, 13]
        face5 = [10, 14, 16]
        face6 = [12, 15, 17]
        self.faces = [face1, face2, face3, face4, face5, face6]

        self.positions = [(0, 45.825757), (-13.671875, 36.962208), (13.671875, 36.962208), (0, 31.721444), (-23.4375, 24.762544), (23.4375, 24.762544), (-9.765625, 22.809155), (9.765625, 22.809155), (0, 15), (0, -15), (-9.765625, -22.809155), (9.765625, -22.809155), (-23.4375, -24.762544), (23.4375, -24.762544), (0, -31.721444), (-13.671875, -36.962208), (13.671875, -36.962208), (0, -45.825757)]

        self.colors = [(184, 10, 49), (0, 68, 175), (0, 156, 70), (255, 0, 255), (255, 214, 0), (255, 87, 0)]

        red1 = MovingPoint(0, 0)
        red2 = MovingPoint(1, 0)
        red3 = MovingPoint(2, 1)

        blue1 = MovingPoint(3, 1)
        blue2 = MovingPoint(4, 0)
        blue3 = MovingPoint(5, 2)

        green1 = MovingPoint(6, 1)
        green2 = MovingPoint(7, 2)
        green3 = MovingPoint(8, 2)

        purple1 = MovingPoint(9, 3)
        purple2 = MovingPoint(10, 4)
        purple3 = MovingPoint(11, 3)

        yellow1 = MovingPoint(12, 5)
        yellow2 = MovingPoint(13, 3)
        yellow3 = MovingPoint(14, 4)

        cyan1 = MovingPoint(15, 5)
        cyan2 = MovingPoint(16, 4)
        cyan3 = MovingPoint(17, 5)

        self.points = [red1, red2, red3, blue1, blue2, blue3, green1, green2, green3, purple1, purple2,
                purple3, yellow1, yellow2, yellow3, cyan1, cyan2, cyan3]

        rotateCircle1CCW = [(0, 2), (2, 5), (5, 13), (13, 16), (16, 17), (17, 0)]
        rotateCircle2CCW = [(1, 3), (3, 7), (7, 11), (11, 14), (14, 15), (15, 1)]
        rotateCircle3CCW = [(4, 6), (6, 8), (8, 9), (9, 10), (10, 12), (12, 4)]
        rotateCircle4CCW = [(0, 17), (17, 15), (15, 12), (12, 4), (4, 1), (1, 0)]
        rotateCircle5CCW = [(2, 16), (16, 14), (14, 10), (10, 6), (6, 3), (3, 2)]
        rotateCircle6CCW = [(5, 13), (13, 11), (11, 9), (9, 8), (8, 7), (7, 5)]

        self.circleMovements = [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW, rotateCircle4CCW, rotateCircle5CCW,
                rotateCircle6CCW]

        mediumRadius = 75 / 2
        largeRadius = 100 / 2
        smallRadius = 50 / 2
        rotateCircle1CCW = [(-20, 0, largeRadius), (-20, 0, largeRadius), (-20, 0, largeRadius), (-20, 0, largeRadius),
                            (-20, 0, largeRadius), (-20, 0, largeRadius)]
        rotateCircle2CCW = [(-20, 0, mediumRadius), (-20, 0, mediumRadius), (-20, 0, mediumRadius),
                            (-20, 0, mediumRadius), (-20, 0, mediumRadius), (-20, 0, mediumRadius)]
        rotateCircle3CCW = [(-20, 0, smallRadius), (-20, 0, smallRadius), (-20, 0, smallRadius), (-20, 0, smallRadius),
                            (-20, 0, smallRadius), (-20, 0, smallRadius)]
        rotateCircle4CCW = [(20, 0, largeRadius), (20, 0, largeRadius), (20, 0, largeRadius), (20, 0, largeRadius),
                            (20, 0, largeRadius), (20, 0, largeRadius)]
        rotateCircle5CCW = [(20, 0, mediumRadius), (20, 0, mediumRadius), (20, 0, mediumRadius), (20, 0, mediumRadius),
                            (20, 0, mediumRadius), (20, 0, mediumRadius)]
        rotateCircle6CCW = [(20, 0, smallRadius), (20, 0, smallRadius), (20, 0, smallRadius), (20, 0, smallRadius),
                            (20, 0, smallRadius), (20, 0, smallRadius)]

        self.circleMovementRotations = [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW, rotateCircle4CCW, rotateCircle5CCW,
                rotateCircle6CCW]

        majorCirclesCenters = [(-20, 0), (-20, 0), (-20, 0), (20, 0), (20, 0),
                               (20, 0)]
        majorCirclesRadii = [largeRadius, mediumRadius, smallRadius, largeRadius, mediumRadius, smallRadius]
        self.circleCoordsAndRadii = majorCirclesCenters, majorCirclesRadii


class Type31:
    def __init__(self):
        self.circleRadius = 20
        self.numFrames = 50
        self.animationType = 2
        face1 = [0]
        face2 = [1]
        face3 = [2]
        face4 = [3]
        face5 = [4]
        face6 = [5]
        self.faces = [face1, face2, face3, face4, face5, face6]

        self.positions = [(0, 56.276921), (-73.737244, 42.572217), (73.737244, 42.572217), (-48.737244, -28.138461),
            (48.737244, -28.138461), (0, -85.144435)]

        self.colors = [(184, 10, 49), (0, 68, 175), (0, 156, 70), (255, 0, 255), (255, 214, 0), (255, 87, 0)]

        red = MovingPoint(0, 0)
        blue = MovingPoint(1, 1)
        green = MovingPoint(2, 2)
        purple = MovingPoint(3, 3)
        yellow = MovingPoint(4, 4)
        cyan = MovingPoint(5, 5)
        self.points = [red, blue, green, purple, yellow, cyan]

        rotateCircle1CCW = [(1, 3), (3, 4), (4, 2), (2, 1)]
        rotateCircle2CCW = [(1, 5), (5, 4), (4, 0), (0, 1)]
        rotateCircle3CCW = [(0, 3), (3, 5), (5, 2), (2, 0)]

        self.circleMovements = [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW]

        largeRadius = 75
        rotateCircle1CCW = [(0, 28.867513, largeRadius), (0, 28.867513, largeRadius), (0, 28.867513, largeRadius),
                            (0, 28.867513, largeRadius)]
        rotateCircle2CCW = [(-25, -14.433757, largeRadius), (-25, -14.433757, largeRadius),
                            (-25, -14.433757, largeRadius),
                            (-25, -14.433757, largeRadius)]
        rotateCircle3CCW = [(25, -14.433757, largeRadius), (25, -14.433757, largeRadius), (25, -14.433757, largeRadius),
                            (25, -14.433757, largeRadius)]

        self.circleMovementRotations = [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW]

        largeRadius = 75
        majorCirclesCenters = [(0, 28.867513), (-25, -14.433757), (25, -14.433757)]
        majorCirclesRadii = [largeRadius, largeRadius, largeRadius]
        self.circleCoordsAndRadii = majorCirclesCenters, majorCirclesRadii


class Type32:
    def __init__(self):
        self.circleRadius = 8
        self.numFrames = 50
        self.animationType = 2
        face1 = [0, 1, 2, 3]
        face2 = [4, 5, 6, 7]
        face3 = [8, 9, 10, 11]
        face4 = [12, 13, 14, 15]
        face5 = [16, 17, 18, 19]
        face6 = [20, 21, 22, 23]
        self.faces = [face1, face2, face3, face4, face5, face6]
        self.positions = [(0, 126.847103), (-20, 113.720327), (20, 113.720327), (0, 103.700661), (-38.484692, 45.313158),
         (-59.852814, 34.556038), (-39.807407, 22.982817), (-58.484692, 10.672142), (38.484692, 45.313158),
         (59.852814, 34.556038), (39.807407, 22.982817), (58.484692, 10.672142), (-108.484692, -39.539656),
         (-89.807407, -51.850331), (-109.852814, -63.423552), (-88.484692, -74.180672), (0, -45.965634),
         (-20, -55.9853), (20, -55.9853), (0, -69.112076), (108.484692, -39.539656), (89.807407, -51.850331),
         (109.852814, -63.423552), (88.484692, -74.180672)]

        self.colors = [(184, 10, 49), (0, 68, 175), (0, 156, 70), (255, 0, 255), (255, 214, 0), (255, 87, 0)]

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

        self.points = [red1, red2, red3, red4, blue1, blue2, blue3, blue4, green1, green2, green3, green4, purple1, purple2,
                purple3, purple4, yellow1, yellow2, yellow3, yellow4, cyan1, cyan2, cyan3, cyan4]

        rotateCircle1CCW = [(0, 15), (2, 14), (15, 18), (14, 19), (18, 9), (19, 11), (9, 0), (11, 2), (21, 20),
                            (20, 22),
                            (22, 23), (23, 21)]
        rotateCircle2CCW = [(1, 13), (3, 12), (13, 16), (12, 17), (16, 8), (17, 10), (8, 1), (10, 3), (4, 5), (5, 7),
                            (7, 6), (6, 4)]
        rotateCircle3CCW = [(0, 5), (1, 7), (5, 17), (7, 19), (17, 23), (19, 22), (23, 0), (22, 1), (13, 15), (15, 14),
                            (14, 12), (12, 13)]
        rotateCircle4CCW = [(2, 4), (3, 6), (4, 16), (6, 18), (16, 21), (18, 20), (21, 2), (20, 3), (9, 8), (8, 10),
                            (10, 11), (11, 9)]
        rotateCircle5CCW = [(4, 12), (5, 14), (12, 22), (14, 20), (22, 9), (20, 8), (9, 4), (8, 5), (2, 3), (3, 1),
                            (1, 0),
                            (0, 2)]
        rotateCircle6CCW = [(6, 13), (7, 15), (13, 23), (15, 21), (23, 11), (21, 10), (11, 6), (10, 7), (16, 17),
                            (17, 19),
                            (19, 18), (18, 16)]

        self.circleMovements = [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW, rotateCircle4CCW, rotateCircle5CCW,
                rotateCircle6CCW]

        smallRadius = -10
        rotateCircle1CCW = [(-50, 28.867513, 110), (-50, 28.867513, 110), (-50, 28.867513, 110), (-50, 28.867513, 110),
                            (-50, 28.867513, 110), (-50, 28.867513, 110), (-50, 28.867513, 110), (-50, 28.867513, 110),
                            (99.15740125, -57.24855275, smallRadius), (99.15740125, -57.24855275, smallRadius),
                            (99.15740125, -57.24855275, smallRadius), (99.15740125, -57.24855275, smallRadius)]
        rotateCircle2CCW = [(-50, 28.867513, 90), (-50, 28.867513, 90), (-50, 28.867513, 90), (-50, 28.867513, 90),
                            (-50, 28.867513, 90), (-50, 28.867513, 90), (-50, 28.867513, 90), (-50, 28.867513, 90),
                            (-50, 28.867513, smallRadius), (-50, 28.867513, smallRadius),
                            (-50, 28.867513, smallRadius), (-50, 28.867513, smallRadius)]
        rotateCircle3CCW = [(50, 28.867513, 110), (50, 28.867513, 110), (50, 28.867513, 110), (50, 28.867513, 110),
                            (50, 28.867513, 110), (50, 28.867513, 110), (50, 28.867513, 110), (50, 28.867513, 110),
                            (-99.15740125, -57.24855275, smallRadius), (-99.15740125, -57.24855275, smallRadius),
                            (-99.15740125, -57.24855275, smallRadius), (-99.15740125, -57.24855275, smallRadius)]
        rotateCircle4CCW = [(50, 28.867513, 90), (50, 28.867513, 90), (50, 28.867513, 90), (50, 28.867513, 90),
                            (50, 28.867513, 90), (50, 28.867513, 90), (50, 28.867513, 90), (50, 28.867513, 90),
                            (50, 28.867513, smallRadius), (50, 28.867513, smallRadius),
                            (50, 28.867513, smallRadius), (50, 28.867513, smallRadius)]
        rotateCircle5CCW = [(0, -57.735027, 110), (0, -57.735027, 110), (0, -57.735027, 110), (0, -57.735027, 110),
                            (0, -57.735027, 110), (0, -57.735027, 110), (0, -57.735027, 110), (0, -57.735027, 110),
                            (0, 114.4971045, smallRadius), (0, 114.4971045, smallRadius), (0, 114.4971045, smallRadius),
                            (0, 114.4971045, smallRadius)]
        rotateCircle6CCW = [(0, -57.735027, 90), (0, -57.735027, 90), (0, -57.735027, 90), (0, -57.735027, 90),
                            (0, -57.735027, 90), (0, -57.735027, 90), (0, -57.735027, 90), (0, -57.735027, 90),
                            (0, -57.735027, smallRadius), (0, -57.735027, smallRadius),
                            (0, -57.735027, smallRadius), (0, -57.735027, smallRadius)]

        self.circleMovementRotations = [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW, rotateCircle4CCW, rotateCircle5CCW,
                rotateCircle6CCW]

        majorCirclesCenters = [(-50, 28.867513), (-50, 28.867513), (50, 28.867513), (50, 28.867513), (0, -57.735027),
                               (0, -57.735027)]
        majorCirclesRadii = [110, 90, 110, 90, 110, 90]
        self.circleCoordsAndRadii = majorCirclesCenters, majorCirclesRadii


class MovingPoint:
    def __init__(self, initPositionIndex, initColor):
        self.positionIndex = initPositionIndex
        self.color = initColor
        self.hasBeenMoved = False


class TheCube:
    def __init__(self, typeNum):
        self.typeNum = typeNum
        if typeNum == 23:
            self.configuration = Type23()
        elif typeNum == 31:
            self.configuration = Type31()
        elif typeNum == 32:
            self.configuration = Type32()
        else:
            self.configuration = Type22()


def GetClosestLargeCircle(currentCube, mouseX, mouseY):
    offset = 0.75
    scaleVal = ReturnScaleVal(currentCube)
    scaleVal *= 0.9

    majorCirclesCenters, majorCirclesRadii = currentCube.configuration.circleCoordsAndRadii
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    closest_circle_index = None
    min_distance_to_edge = float('inf')

    for i, (center_x, center_y) in enumerate(majorCirclesCenters):
        distance_to_center = math.sqrt((mouseX - (screenWidth * offset) - center_x * scaleVal) ** 2 + (
                mouseY - (screenHeight / 2) - center_y * scaleVal) ** 2)
        distance_to_edge = abs(distance_to_center - majorCirclesRadii[i] * scaleVal)

        if distance_to_edge < min_distance_to_edge:
            min_distance_to_edge = distance_to_edge
            closest_circle_index = i

    return closest_circle_index


def XYCoordinatesFromLocationChange(startPos, endPos, circleCenter, circleRadius, numPoints, CCW, animationType):
    if CCW:
        tempPoint = startPos
        startPos = endPos
        endPos = tempPoint

    theta1 = math.atan2(startPos[1] - circleCenter[1], startPos[0] - circleCenter[0])
    theta2 = math.atan2(endPos[1] - circleCenter[1], endPos[0] - circleCenter[0])
    if animationType == 1:
        if theta1 < 0 < theta2:
            theta2 -= 2 * math.pi
    elif animationType == 2:
        if theta2 < 0 < theta1:
            theta1 -= 2 * math.pi

    returnCoords = []

    # Cosing spacing allows for acceleration and deceleration of points
    t = np.linspace(0, np.pi, numPoints)
    equally_spaced_vector = theta1 + 0.5 * (1 - np.cos(t)) * (theta2 - theta1)

    if CCW:
        equally_spaced_vector = np.flipud(equally_spaced_vector)

    if circleRadius < 0:  # Linear Path
        xCoords = np.linspace(startPos[0], endPos[0], numPoints)
        yCoords = np.linspace(startPos[1], endPos[1], numPoints)
        for currIndex in range(numPoints):
            returnCoords.append((xCoords[currIndex], yCoords[currIndex]))
    else:
        for i in range(len(equally_spaced_vector)):
            initialCoords = pol2cart(circleRadius, equally_spaced_vector[i])
            returnCoords.append((initialCoords[0] + circleCenter[0], initialCoords[1] + circleCenter[1]))

    return returnCoords


def GetXYRotationCoords(currentCube, rotationIndex, CCW):
    returnCoords = []

    allMovements = currentCube.configuration.circleMovements
    movements = allMovements[rotationIndex]
    pointPositions = currentCube.configuration.positions

    for pointIndex in range(len(currentCube.configuration.points)):
        currentPointVec = []

        if any(currentCube.configuration.points[pointIndex].positionIndex in currTuple for currTuple in movements):
            startPoint = pointPositions[currentCube.configuration.points[pointIndex].positionIndex]
            endPoint = ()
            centerRotation = (float('inf'), float('inf'))
            centerRadius = float('inf')
            centersAndRadii = currentCube.configuration.circleMovementRotations[rotationIndex]

            for moveIndex in range(len(movements)):
                if movements[moveIndex][CCW] == currentCube.configuration.points[pointIndex].positionIndex:
                    endPoint = pointPositions[movements[moveIndex][not CCW]]
                    centerRotation = (centersAndRadii[moveIndex][0], centersAndRadii[moveIndex][1])
                    centerRadius = centersAndRadii[moveIndex][2]

            currentPointVec = XYCoordinatesFromLocationChange(startPoint, endPoint, centerRotation, centerRadius,
                                                              currentCube.configuration.numFrames, CCW, currentCube.configuration.animationType)
        else:
            for currInd in range(currentCube.configuration.numFrames):
                currentPointVec.append(pointPositions[currentCube.configuration.points[pointIndex].positionIndex])
        returnCoords.append(currentPointVec)

    return returnCoords


def ReturnScaleVal(tempCube):
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h
    majorCirclesCenters, majorCirclesRadii = tempCube.configuration.circleCoordsAndRadii
    # Unpack the vector into separate lists for the first and second elements
    xVals, yVals = zip(*tempCube.configuration.positions)
    maxX = max(xVals)
    minX = min(xVals)
    maxY = max(yVals)
    minY = min(yVals)

    rangeY = (maxY - minY) + max(majorCirclesRadii) * 2
    rangeX = (maxX - minX) + max(majorCirclesRadii) * 2

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX
    else:
        scaleVal = screenHeight / rangeY

    return scaleVal*0.9


def PlotMajorCircleCenters(screen, currentCube, scaleVal, offset):
    majorCirclesCenters, majorCirclesRadii = currentCube.configuration.circleCoordsAndRadii
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    for i in range(len(majorCirclesCenters)):
        pygame.gfxdraw.aacircle(screen, int((majorCirclesCenters[i][0] * scaleVal + (screenWidth * offset))),
                                int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))


def DrawPoints(screen, currentCube, scaleVal, offset):
    pointPositions = currentCube.configuration.positions
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    for point in currentCube.configuration.points:
        pygame.draw.circle(screen, currentCube.configuration.colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset)),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           currentCube.configuration.circleRadius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(screen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset))),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(currentCube.configuration.circleRadius * math.sqrt(scaleVal)),
                                currentCube.configuration.colors[point.color])


def AnimatePos1ToPos2(screen, currentCube, rotateIndex, CW, solutionVec, offset):
    screen.fill((255, 255, 255))
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    scaleVal = ReturnScaleVal(currentCube)
    if offset <= 0.25:
        scaleVal *= 0.75

    DrawSolution(screen, solutionVec, currentCube.typeNum)
    DrawPoints(screen, currentCube, scaleVal, offset)

    xyCoords = GetXYRotationCoords(currentCube, rotateIndex, CW)

    for frame in range(len(xyCoords[0])):
        screen.fill((255, 255, 255))
        PlotMajorCircleCenters(screen, currentCube, scaleVal, offset)
        for coordIndex in range(len(xyCoords)):
            pygame.draw.circle(screen, currentCube.configuration.colors[currentCube.configuration.points[coordIndex].color], (
                int(xyCoords[coordIndex][frame][0] * scaleVal + (screenWidth * offset)),
                int(xyCoords[coordIndex][frame][1] * scaleVal + screenHeight / 2)),
                               currentCube.configuration.circleRadius * math.sqrt(scaleVal))
            pygame.gfxdraw.aacircle(screen, int((xyCoords[coordIndex][frame][0] * scaleVal + (screenWidth * offset))),
                                    int((xyCoords[coordIndex][frame][1] * scaleVal + screenHeight / 2)),
                                    int(currentCube.configuration.circleRadius * math.sqrt(scaleVal)), currentCube.configuration.colors[currentCube.configuration.points[coordIndex].color])
        if offset > 0.25:
            DrawSolution(screen, solutionVec, currentCube.typeNum)
        pygame.display.flip()
        pygame.time.delay(10)


def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y


def updateGameScreen(screen, currentCube, solutionVec):
    screen.fill((255, 255, 255))
    offset = 0.75  # percent distance from edge

    scaleVal = ReturnScaleVal(currentCube)

    PlotMajorCircleCenters(screen, currentCube, scaleVal, offset)
    DrawPoints(screen, currentCube, scaleVal, offset)
    DrawSolution(screen, solutionVec, currentCube.typeNum)

    if CheckIfSolved(currentCube, solutionVec):
        DrawSolvedTitle(screen)


def DrawSolvedTitle(screen):
    font_size = 48
    font = pygame.font.Font(None, font_size)  # Use the default system font
    text_color = (0, 0, 0)  # Black

    text_surface = font.render("SOLVED!", True, text_color)
    text_x = (pygame.display.Info().current_w - text_surface.get_width()) // 2
    text_y = 25
    text_rect = text_surface.get_rect()
    text_rect.topleft = (text_x, text_y)
    screen.blit(text_surface, text_rect)


def DrawSolution(screen, solutionVec, typeNum):
    tempCube = TheCube(typeNum)
    tempPoints = tempCube.configuration.points

    for pointIndex in range(len(tempPoints)):
        tempPoints[pointIndex].positionIndex = solutionVec[pointIndex]

    offset = 0.25  # percent distance from edge

    scaleVal = ReturnScaleVal(tempCube)
    scaleVal *= 0.75

    PlotMajorCircleCenters(screen, tempCube, scaleVal, offset)
    DrawPoints(screen, tempCube, scaleVal, offset)

    DrawMatchTitle(screen)


def DrawMatchTitle(screen):
    font_size = 36
    font = pygame.font.Font(None, font_size)  # Use the default system font
    text_color = (0, 0, 0)  # Black

    text_surface = font.render("Match this pattern", True, text_color)
    text_x = (pygame.display.Info().current_w - text_surface.get_width()) * 0.19
    text_y = 125
    text_rect = text_surface.get_rect()
    text_rect.topleft = (text_x, text_y)
    screen.blit(text_surface, text_rect)


def ResetPoints(points):
    for pointIndex in range(len(points)):
        points[pointIndex].positionIndex = pointIndex


def Rotate(screen, currentCube, circleNum, CW, solutionVec, offsetVal):
    allMovements = currentCube.configuration.circleMovements
    movements = allMovements[circleNum]
    AnimatePos1ToPos2(screen, currentCube, circleNum, CW, solutionVec, offsetVal)

    for move in movements:
        for point in currentCube.configuration.points:
            if move[CW] == point.positionIndex and point.hasBeenMoved is False:
                point.positionIndex = move[not CW]
                point.hasBeenMoved = True

    for point in currentCube.configuration.points:
        point.hasBeenMoved = False


def CheckIfFaceIsSolved(faceIndex, currentCube):
    solved = True

    face = currentCube.configuration.faces[faceIndex]
    currFaceColors = []
    for faceIndex in face:
        for point in currentCube.configuration.points:
            if point.positionIndex == faceIndex:
                currFaceColors.append(point.color)
    if not all(element == currFaceColors[0] for element in currFaceColors):
        return False

    return solved


def CheckIfSolved(currentCube, correctOrder):
    solved = True

    for checkIndex in range(len(currentCube.configuration.points)):
        if currentCube.configuration.points[checkIndex].positionIndex != correctOrder[checkIndex]:
            return False

    return solved


def CreateRandomOrder(tempSolutionCube, screen, numRandomRotations):
    tempPoints = tempSolutionCube.configuration.points

    offsetVal = 0.25

    random_values = [random.randint(0, len(tempSolutionCube.configuration.circleMovements)-1) for _ in range(numRandomRotations)]
    random_bools = [random.choice([True, False]) for _ in range(numRandomRotations)]

    for randomIndex in range(numRandomRotations):
        solutionVec = []
        for pointIndex in range(len(tempPoints)):
            solutionVec.append(tempPoints[pointIndex].positionIndex)

        Rotate(screen, tempSolutionCube, random_values[randomIndex], random_bools[randomIndex], solutionVec, offsetVal)
    solutionVec = []
    for pointIndex in range(len(tempPoints)):
        solutionVec.append(tempPoints[pointIndex].positionIndex)

    return solutionVec


def ShowSolution(currentCube, solutionScreen, correctOrder):
    tempPoints = currentCube.configuration.points
    offset = 0.25

    for tempPointIndex in range(len(tempPoints)):
        tempPoints[tempPointIndex].positionIndex = correctOrder[tempPointIndex]

    solutionScreen.fill((255, 255, 255))
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    scaleVal = ReturnScaleVal(currentCube)
    scaleVal /= 0.9
    if screenWidth < screenHeight:
        scaleVal *= 2

    PlotMajorCircleCenters(solutionScreen, currentCube, scaleVal, 0)
    DrawPoints(solutionScreen, currentCube, scaleVal, offset)

    pygame.display.flip()


def RandomizeCube(screen, currentCube, numRandomRotations, cubeMoves, solutionVec):
    random_values = [random.randint(0, len(currentCube.configuration.circleMovements)-1) for _ in range(numRandomRotations)]
    random_bools = [random.choice([True, False]) for _ in range(numRandomRotations)]
    offsetVal = 0.75

    for randomIndex in range(numRandomRotations):
        Rotate(screen, currentCube, random_values[randomIndex], random_bools[randomIndex], solutionVec, offsetVal)
        cubeMoves.append((random_values[randomIndex], random_bools[randomIndex]))

    return cubeMoves


def FindFaceWithMaxSameColor(currentCube):
    faces = currentCube.configuration.faces
    maxColorsOnFace = 0
    elementsOnMaxFace = []
    elementCountsOnMaxFace = []
    facesIndex = 0
    maxFacesIndex = -1
    for face in faces:
        currFaceColors = []
        for faceIndex in face:
            for point in currentCube.configuration.points:
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


def SolveCube(screen, currentCube, cubeMoves, solutionVec):  # BAD
    # 0 - R = The right face
    # 1 - L = The left face
    # 2 - U = The top face
    # 3 - D = The bottom face
    # 4 - F = The face at the front
    # 5 - B = The face at the back

    faceWithMaxColorIndex, maxColor = FindFaceWithMaxSameColor(currentCube.configuration.points)
    # faces = ReturnFaces()
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
    # numFacesSolved = 0
    # while not CheckIfFaceIsSolved(0, points) or not CheckIfFaceIsSolved(1, points):
    while not CheckIfFaceIsSolved(faceWithMaxColorIndex, currentCube.configuration.points):
        rotateInt = random.randint(0, 5)
        randDir = random.randint(0, 1)
        Rotate(screen, currentCube, rotateInt, randDir, solutionVec, 0.75)
        cubeMoves.append((rotateInt, randDir))
        nit += 1
    print(nit)
    print("Face ", faceWithMaxColorIndex, " is solved:", CheckIfFaceIsSolved(faceWithMaxColorIndex, currentCube.configuration.points))

    return cubeMoves

