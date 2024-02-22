import math
import numpy as np
import random
import pygame
import pygame.gfxdraw


class Type22:
    def __init__(self):
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


class MovingPoint:
    def __init__(self, initPositionIndex, initColor):
        self.positionIndex = initPositionIndex
        self.color = initColor
        self.hasBeenMoved = False


class TheCube:
    def __init__(self):
        self.configuration = Type22()


def GetClosestLargeCircle(currentCube, mouseX, mouseY):
    offset = 0.75
    pointPositions = currentCube.configuration.positions
    majorCirclesCenters, majorCirclesRadii = currentCube.configuration.circleCoordsAndRadii

    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h
    # Unpack the vector into separate lists for the first and second elements
    firstElements, secondElements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    maxFirst = max(firstElements)
    minFirst = min(firstElements)
    maxSecond = max(secondElements)
    minSecond = min(secondElements)

    rangeY = (maxSecond - minSecond) + max(majorCirclesRadii) * 2
    rangeX = (maxFirst - minFirst) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX

    else:
        scaleVal = screenHeight / rangeY

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


def XYCoordinatesFromLocationChange(startPos, endPos, circleCenter, circleRadius, numPoints, CCW):
    if CCW:
        tempPoint = startPos
        startPos = endPos
        endPos = tempPoint

    theta1 = math.atan2(startPos[1] - circleCenter[1], startPos[0] - circleCenter[0])
    theta2 = math.atan2(endPos[1] - circleCenter[1], endPos[0] - circleCenter[0])

    if theta1 < 0 < theta2:
        theta2 -= 2 * math.pi

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
    numPoints = 50

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
                                                              numPoints, CCW)
        else:
            for currInd in range(numPoints):
                currentPointVec.append(pointPositions[currentCube.configuration.points[pointIndex].positionIndex])
        returnCoords.append(currentPointVec)

    return returnCoords


def AnimatePos1ToPos2(screen, currentCube, rotateIndex, CW, solutionVec, offset):
    white = (255, 255, 255)
    screen.fill(white)
    circle_radius = 10
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    pointPositions = currentCube.configuration.positions
    majorCirclesCenters, majorCirclesRadii = currentCube.configuration.circleCoordsAndRadii
    # Unpack the vector into separate lists for the first and second elements
    firstElements, secondElements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    maxFirst = max(firstElements)
    minFirst = min(firstElements)
    maxSecond = max(secondElements)
    minSecond = min(secondElements)

    rangeY = (maxSecond - minSecond) + max(majorCirclesRadii) * 2
    rangeX = (maxFirst - minFirst) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX

    else:
        scaleVal = screenHeight / rangeY

    if offset <= 0.25:
        scaleVal *= 0.75

    scaleVal *= 0.9

    DrawSolution(currentCube, screen, solutionVec)

    pointPositions = currentCube.configuration.positions
    for point in currentCube.configuration.points:
        pygame.draw.circle(screen, currentCube.configuration.colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(screen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset))),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), currentCube.configuration.colors[point.color])

    xyCoords = GetXYRotationCoords(currentCube, rotateIndex, CW)

    for frame in range(len(xyCoords[0])):
        screen.fill(white)
        for i in range(len(majorCirclesCenters)):
            pygame.gfxdraw.aacircle(screen, int((majorCirclesCenters[i][0] * scaleVal + (screenWidth * offset))),
                                    int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                    int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))
        for coordIndex in range(len(xyCoords)):
            pygame.draw.circle(screen, currentCube.configuration.colors[currentCube.configuration.points[coordIndex].color], (
                int(xyCoords[coordIndex][frame][0] * scaleVal + (screenWidth * offset)),
                int(xyCoords[coordIndex][frame][1] * scaleVal + screenHeight / 2)),
                               circle_radius * math.sqrt(scaleVal))
            pygame.gfxdraw.aacircle(screen, int((xyCoords[coordIndex][frame][0] * scaleVal + (screenWidth * offset))),
                                    int((xyCoords[coordIndex][frame][1] * scaleVal + screenHeight / 2)),
                                    int(circle_radius * math.sqrt(scaleVal)), currentCube.configuration.colors[currentCube.configuration.points[coordIndex].color])
        if offset > 0.25:
            DrawSolution(currentCube, screen, solutionVec)
        pygame.display.flip()
        pygame.time.delay(10)


def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y


def updateGameScreen(screen, currentCube, solutionVec):
    # Clear the screen
    white = (255, 255, 255)
    screen.fill(white)
    circle_radius = 10
    offset = 0.75  # percent distance from edge
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    pointPositions = currentCube.configuration.positions
    majorCirclesCenters, majorCirclesRadii = currentCube.configuration.circleCoordsAndRadii
    # Unpack the vector into separate lists for the first and second elements
    firstElements, secondElements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    maxFirst = max(firstElements)
    minFirst = min(firstElements)
    maxSecond = max(secondElements)
    minSecond = min(secondElements)

    rangeY = (maxSecond - minSecond) + max(majorCirclesRadii) * 2
    rangeX = (maxFirst - minFirst) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX

    else:
        scaleVal = screenHeight / rangeY

    scaleVal *= 0.9

    for i in range(len(majorCirclesCenters)):
        pygame.gfxdraw.aacircle(screen, int(((majorCirclesCenters[i][0] * scaleVal) + (screenWidth * offset))),
                                int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))

    pointPositions = currentCube.configuration.positions
    counterNum = 0
    for point in currentCube.configuration.points:
        pygame.draw.circle(screen, currentCube.configuration.colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset)),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(screen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset))),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), currentCube.configuration.colors[point.color])

        counterNum += 1
    DrawSolution(currentCube, screen, solutionVec)
    if CheckIfSolved(currentCube, solutionVec):
        font_size = 48
        font = pygame.font.Font(None, font_size)  # Use the default system font
        text_color = (0, 0, 0)  # Black

        text_surface = font.render("SOLVED!", True, text_color)
        text_x = (pygame.display.Info().current_w - text_surface.get_width()) // 2
        text_y = 25
        text_rect = text_surface.get_rect()
        text_rect.topleft = (text_x, text_y)
        screen.blit(text_surface, text_rect)


def DrawSolution(currentCube, screen, solutionVec):
    tempCube = TheCube()
    tempPoints = tempCube.configuration.points

    for pointIndex in range(len(tempPoints)):
        tempPoints[pointIndex].positionIndex = solutionVec[pointIndex]

    circle_radius = 10
    offset = 0.25  # percent distance from edge
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    pointPositions = currentCube.configuration.positions
    majorCirclesCenters, majorCirclesRadii = currentCube.configuration.circleCoordsAndRadii

    # Unpack the vector into separate lists for the first and second elements
    firstElements, secondElements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    maxFirst = max(firstElements)
    minFirst = min(firstElements)
    maxSecond = max(secondElements)
    minSecond = min(secondElements)

    rangeY = (maxSecond - minSecond) + max(majorCirclesRadii) * 2
    rangeX = (maxFirst - minFirst) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX

    else:
        scaleVal = screenHeight / rangeY

    scaleVal *= 0.75

    scaleVal *= 0.9

    for i in range(len(majorCirclesCenters)):
        pygame.gfxdraw.aacircle(screen, int((majorCirclesCenters[i][0] * scaleVal + (screenWidth * offset))),
                                int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))

    pointPositions = currentCube.configuration.positions
    for point in tempPoints:
        pygame.draw.circle(screen, currentCube.configuration.colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset)),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(screen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset))),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), currentCube.configuration.colors[point.color])

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


def CreateRandomOrder(tempSolutionCube, screen):
    tempPoints = tempSolutionCube.configuration.points

    numRandomRotations = 5
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

    for tempPointIndex in range(len(tempPoints)):
        tempPoints[tempPointIndex].positionIndex = correctOrder[tempPointIndex]

    white = (255, 255, 255)
    solutionScreen.fill(white)
    circle_radius = 20
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    pointPositions = currentCube.configuration.positions
    majorCirclesCenters, majorCirclesRadii = currentCube.configuration.circleCoordsAndRadii

    # Unpack the vector into separate lists for the first and second elements
    firstElements, secondElements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    maxFirst = max(firstElements)
    minFirst = min(firstElements)
    maxSecond = max(secondElements)
    minSecond = min(secondElements)

    rangeY = (maxSecond - minSecond) + max(majorCirclesRadii) * 2
    rangeX = (maxFirst - minFirst) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth < screenHeight:
        scaleVal = screenWidth / rangeX

    else:
        scaleVal = screenHeight / rangeY

    for i in range(len(majorCirclesCenters)):
        pygame.gfxdraw.aacircle(solutionScreen, int((majorCirclesCenters[i][0] * scaleVal + screenWidth / 2)),
                                int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))

    pointPositions = currentCube.configuration.positions
    counterNum = 0
    for point in tempPoints:
        pygame.draw.circle(solutionScreen, currentCube.configuration.colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(solutionScreen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2)),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), currentCube.configuration.colors[point.color])

        counterNum += 1
    pygame.display.flip()


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


def RandomizeCube(screen, currentCube, numRandomRotations, cubeMoves, solutionVec):
    random_values = [random.randint(0, len(currentCube.configuration.circleMovements)-1) for _ in range(numRandomRotations)]
    random_bools = [random.choice([True, False]) for _ in range(numRandomRotations)]
    offsetVal = 0.75

    for randomIndex in range(numRandomRotations):
        Rotate(screen, currentCube, random_values[randomIndex], random_bools[randomIndex], solutionVec, offsetVal)
        cubeMoves.append((random_values[randomIndex], random_bools[randomIndex]))

    return cubeMoves

