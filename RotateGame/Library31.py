import math
import numpy as np
import random
import pygame
import pygame.gfxdraw


class MovingPoint:
    def __init__(self, initPositionIndex, initColor):
        self.positionIndex = initPositionIndex
        self.color = initColor
        self.hasBeenMoved = False


class TheCube:
    def __init__(self):
        self.points = CreateAllPoints()


def GetClosestLargeCircle(mouseX, mouseY):
    offset = 0.75
    pointPositions = ReturnPositions()
    majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()

    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h
    # Unpack the vector into separate lists for the first and second elements
    first_elements, second_elements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    max_first = max(first_elements)
    min_first = min(first_elements)
    max_second = max(second_elements)
    min_second = min(second_elements)

    rangeY = (max_second - min_second) + max(majorCirclesRadii) * 2
    rangeX = (max_first - min_first) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX

    else:
        scaleVal = screenHeight / rangeY

    majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    closest_circle_index = None
    min_distance_to_edge = float('inf')

    for i, (center_x, center_y) in enumerate(majorCirclesCenters):
        distance_to_center = math.sqrt((mouseX - (screenWidth * offset) - center_x * scaleVal) ** 2 + (
                mouseY - (screenHeight / 2) - center_y * scaleVal) ** 2)
        distance_to_edge = abs(distance_to_center - majorCirclesRadii[i] * scaleVal)

        # Update the closest circle if the current circle is closer
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

    if theta2 < 0 < theta1:
        theta1 -= 2 * math.pi

    returnCoords = []

    # Cosing spacing allows for acceleration and deceleration of points
    t = np.linspace(0, np.pi, numPoints)  # Create a linearly spaced vector from 0 to pi
    equally_spaced_vector = theta1 + 0.5 * (1 - np.cos(t)) * (theta2 - theta1)

    if CCW:
        equally_spaced_vector = np.flipud(equally_spaced_vector)

    if circleRadius < 0:
        # Linear Path
        xCoords = np.linspace(startPos[0], endPos[0], numPoints)
        yCoords = np.linspace(startPos[1], endPos[1], numPoints)
        for currIndex in range(numPoints):
            returnCoords.append((xCoords[currIndex], yCoords[currIndex]))
    else:
        for i in range(len(equally_spaced_vector)):
            initialCoords = pol2cart(circleRadius, equally_spaced_vector[i])
            returnCoords.append((initialCoords[0] + circleCenter[0], initialCoords[1] + circleCenter[1]))

    return returnCoords


def GetXYRotationCoords(points, rotationIndex, CCW):
    returnCoords = []
    numPoints = 50

    allMovements = ReturnCircleMovements()
    movements = allMovements[rotationIndex]
    pointPositions = ReturnPositions()

    for pointIndex in range(len(points)):
        currentPointVec = []

        if any(points[pointIndex].positionIndex in my_tuple for my_tuple in movements):
            startPoint = pointPositions[points[pointIndex].positionIndex]
            endPoint = ()
            centerRotation = (0, 0)
            centerRadius = 100
            centersAndRadii = ReturnCircleMovementRotations()[rotationIndex]

            for moveIndex in range(len(movements)):
                if movements[moveIndex][CCW] == points[pointIndex].positionIndex:
                    endPoint = pointPositions[movements[moveIndex][not CCW]]
                    centerRotation = (centersAndRadii[moveIndex][0], centersAndRadii[moveIndex][1])
                    centerRadius = centersAndRadii[moveIndex][2]

            currentPointVec = XYCoordinatesFromLocationChange(startPoint, endPoint, centerRotation, centerRadius,
                                                              numPoints, CCW)
        else:
            for currInd in range(numPoints):
                currentPointVec.append(pointPositions[points[pointIndex].positionIndex])
        returnCoords.append(currentPointVec)

    return returnCoords


def AnimatePos1ToPos2(screen, points, rotateIndex, CW, solutionVec, offset):
    # Clear the screen
    white = (255, 255, 255)
    screen.fill(white)
    # offset = 0.75
    circle_radius = 20
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    pointPositions = ReturnPositions()
    majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()

    # Unpack the vector into separate lists for the first and second elements
    first_elements, second_elements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    max_first = max(first_elements)
    min_first = min(first_elements)
    max_second = max(second_elements)
    min_second = min(second_elements)

    rangeY = (max_second - min_second) + max(majorCirclesRadii) * 2
    rangeX = (max_first - min_first) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX

    else:
        scaleVal = screenHeight / rangeY

    if offset <=0.25:
        scaleVal *= 0.75

    colors = ReturnColorsRBG()
    DrawSolution(screen, solutionVec)
    # font_size = 36
    # font_size_small = 12
    # font = pygame.font.Font(None, font_size)  # Use the default system font
    # font2 = pygame.font.Font(None, font_size_small)
    # text_color = (0, 0, 0)  # Black

    # for i in range(len(majorCirclesCenters)):
    #     pygame.gfxdraw.aacircle(screen, int((majorCirclesCenters[i][0] * scaleVal + screenWidth / 2)),
    #                             int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
    #                             int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))

    # addDist = majorCirclesRadii[i] * 0.707
    # if i < 2:
    #     text_surface = font.render(str(i + 1), True, text_color)
    #     text_x, text_y = (majorCirclesCenters[i][0] - addDist) * scaleVal + screenWidth / 2, (
    #                 majorCirclesCenters[i][1] + addDist) * scaleVal + screenHeight / 2
    # elif i < 4:
    #     text_surface = font.render(str(i + 1), True, text_color)
    #     text_x, text_y = (majorCirclesCenters[i][0] + addDist) * scaleVal + screenWidth / 2, (
    #                 majorCirclesCenters[i][
    #                     1] + addDist) * scaleVal + screenHeight / 2
    # else:
    #     text_surface = font.render(str(i + 1), True, text_color)
    #     text_x, text_y = majorCirclesCenters[i][0] * scaleVal + screenWidth / 2, (majorCirclesCenters[i][
    #                                                                                   1] - majorCirclesRadii[
    #                                                                                   i]) * scaleVal + screenHeight / 2
    # text_rect = text_surface.get_rect()
    # text_rect.topleft = (text_x, text_y)
    # screen.blit(text_surface, text_rect)

    pointPositions = ReturnPositions()
    for point in points:
        pygame.draw.circle(screen, colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(screen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset))),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), colors[point.color])

    xyCoords = GetXYRotationCoords(points, rotateIndex, CW)

    for frame in range(len(xyCoords[0])):
        # print("frame:", frame)
        screen.fill(white)
        for i in range(len(majorCirclesCenters)):
            pygame.gfxdraw.aacircle(screen, int((majorCirclesCenters[i][0] * scaleVal + (screenWidth * offset))),
                                    int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                    int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))
        for coordIndex in range(len(xyCoords)):
            # print("coordIndex:", coordIndex)
            pygame.draw.circle(screen, colors[points[coordIndex].color], (
                int(xyCoords[coordIndex][frame][0] * scaleVal + (screenWidth * offset)),
                int(xyCoords[coordIndex][frame][1] * scaleVal + screenHeight / 2)),
                               circle_radius * math.sqrt(scaleVal))
            pygame.gfxdraw.aacircle(screen, int((xyCoords[coordIndex][frame][0] * scaleVal + (screenWidth * offset))),
                                    int((xyCoords[coordIndex][frame][1] * scaleVal + screenHeight / 2)),
                                    int(circle_radius * math.sqrt(scaleVal)), colors[points[coordIndex].color])
        if offset > 0.25:
            DrawSolution(screen, solutionVec)
        pygame.display.flip()
        pygame.time.delay(10)


def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y


def updateGameScreen(screen, points, solutionVec):
    # Clear the screen
    white = (255, 255, 255)
    screen.fill(white)
    circle_radius = 20
    offset = 0.75  # percent distance from edge
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    pointPositions = ReturnPositions()
    majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()

    # Unpack the vector into separate lists for the first and second elements
    first_elements, second_elements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    max_first = max(first_elements)
    min_first = min(first_elements)
    max_second = max(second_elements)
    min_second = min(second_elements)

    rangeY = (max_second - min_second) + max(majorCirclesRadii) * 2
    rangeX = (max_first - min_first) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX

    else:
        scaleVal = screenHeight / rangeY

    colors = ReturnColorsRBG()

    # font_size = 36
    # font_size_small = 12
    # font = pygame.font.Font(None, font_size)  # Use the default system font
    # font2 = pygame.font.Font(None, font_size_small)
    # text_color = (0, 0, 0)  # Black

    for i in range(len(majorCirclesCenters)):
        pygame.gfxdraw.aacircle(screen, int(((majorCirclesCenters[i][0] * scaleVal) + (screenWidth * offset))),
                                int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))
        # pygame.draw.circle(screen, (0, 0, 0), (majorCirclesCenters[i][0] + screenWidth/2, majorCirclesCenters[i][1] + screenHeight/2), majorCirclesRadii[i], outlineWith)

        # addDist = majorCirclesRadii[i] * 0.707
        # if i < 2:
        #     text_surface = font.render(str(i + 1), True, text_color)
        #     text_x, text_y = (majorCirclesCenters[i][0] - addDist)*scaleVal + screenWidth/2, (majorCirclesCenters[i][1] + addDist)*scaleVal + screenHeight/2
        # elif i < 4:
        #     text_surface = font.render(str(i + 1), True, text_color)
        #     text_x, text_y = (majorCirclesCenters[i][0] + addDist)*scaleVal + screenWidth / 2, (majorCirclesCenters[i][
        #         1] + addDist)*scaleVal + screenHeight / 2
        # else:
        #     text_surface = font.render(str(i + 1), True, text_color)
        #     text_x, text_y = majorCirclesCenters[i][0]*scaleVal + screenWidth / 2, (majorCirclesCenters[i][
        #         1] - majorCirclesRadii[i])*scaleVal + screenHeight / 2
        # text_rect = text_surface.get_rect()
        # text_rect.topleft = (text_x, text_y)
        # screen.blit(text_surface, text_rect)

    pointPositions = ReturnPositions()
    counterNum = 0
    for point in points:
        pygame.draw.circle(screen, colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset)),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(screen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset))),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), colors[point.color])

        # if True:
        #     # currAx.text(pointPositions[point.positionIndex][0], pointPositions[point.positionIndex][1], str(counterNum),
        #     #             verticalalignment='bottom', horizontalalignment='right')
        #     text_surface = font2.render(str(counterNum), True, text_color)
        #     text_x, text_y = pointPositions[point.positionIndex][0] + screenWidth / 2, pointPositions[point.positionIndex][1] + screenHeight / 2
        #     text_rect = text_surface.get_rect()
        #     text_rect.topleft = (text_x, text_y)
        #     screen.blit(text_surface, text_rect)
        counterNum += 1
    DrawSolution(screen, solutionVec)
    if CheckIfSolved(points, solutionVec):
        font_size = 48
        font = pygame.font.Font(None, font_size)  # Use the default system font
        text_color = (0, 0, 0)  # Black

        text_surface = font.render("SOLVED!", True, text_color)
        text_x = (pygame.display.Info().current_w - text_surface.get_width()) // 2
        text_y = 25
        text_rect = text_surface.get_rect()
        text_rect.topleft = (text_x, text_y)
        screen.blit(text_surface, text_rect)


def DrawSolution(screen, solutionVec):
    tempPoints = CreateAllPoints()
    for pointIndex in range(len(tempPoints)):
        tempPoints[pointIndex].positionIndex = solutionVec[pointIndex]

    circle_radius = 20
    offset = 0.25  # percent distance from edge
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    pointPositions = ReturnPositions()
    majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()

    # Unpack the vector into separate lists for the first and second elements
    first_elements, second_elements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    max_first = max(first_elements)
    min_first = min(first_elements)
    max_second = max(second_elements)
    min_second = min(second_elements)

    rangeY = (max_second - min_second) + max(majorCirclesRadii) * 2
    rangeX = (max_first - min_first) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth / 2 < screenHeight:
        scaleVal = (screenWidth / 2) / rangeX

    else:
        scaleVal = screenHeight / rangeY

    scaleVal *= 0.75

    colors = ReturnColorsRBG()

    for i in range(len(majorCirclesCenters)):
        pygame.gfxdraw.aacircle(screen, int((majorCirclesCenters[i][0] * scaleVal + (screenWidth * offset))),
                                int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))

    pointPositions = ReturnPositions()
    for point in tempPoints:
        pygame.draw.circle(screen, colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset)),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(screen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + (screenWidth * offset))),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), colors[point.color])

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


def Rotate(screen, points, circleNum, CW, solutionVec, offsetVal):
    allMovements = ReturnCircleMovements()
    movements = allMovements[circleNum]

    AnimatePos1ToPos2(screen, points, circleNum, CW, solutionVec, offsetVal)

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


def CheckIfSolved(points, correctOrder):
    solved = True

    for checkIndex in range(len(points)):
        if points[checkIndex].positionIndex != correctOrder[checkIndex]:
            return False

    # print("SOLVED!")
    return solved


def CreateRandomOrder(screen):
    tempPoints = CreateAllPoints()

    numRandomRotations = 5
    offsetVal = 0.25

    random_values = [random.randint(0, 2) for _ in range(numRandomRotations)]
    random_bools = [random.choice([True, False]) for _ in range(numRandomRotations)]

    for randomIndex in range(numRandomRotations):
        solutionVec = []
        for pointIndex in range(len(tempPoints)):
            solutionVec.append(tempPoints[pointIndex].positionIndex)

        Rotate(screen, tempPoints, random_values[randomIndex], random_bools[randomIndex], solutionVec, offsetVal)

    solutionVec = []
    for pointIndex in range(len(tempPoints)):
        solutionVec.append(tempPoints[pointIndex].positionIndex)

    # newIndices = list(range(len(tempPoints)))
    # random.shuffle(newIndices)

    return solutionVec


def ShowSolution(solutionScreen, correctOrder):
    tempPoints = CreateAllPoints()

    for tempPointIndex in range(len(tempPoints)):
        tempPoints[tempPointIndex].positionIndex = correctOrder[tempPointIndex]

    white = (255, 255, 255)
    solutionScreen.fill(white)
    circle_radius = 20
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    pointPositions = ReturnPositions()
    majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()

    # Unpack the vector into separate lists for the first and second elements
    first_elements, second_elements = zip(*pointPositions)
    # Find maximum and minimum values for the first and second elements
    max_first = max(first_elements)
    min_first = min(first_elements)
    max_second = max(second_elements)
    min_second = min(second_elements)

    rangeY = (max_second - min_second) + max(majorCirclesRadii) * 2
    rangeX = (max_first - min_first) + max(majorCirclesRadii) * 2
    scaleVal = 1

    if screenWidth < screenHeight:
        scaleVal = screenWidth / rangeX

    else:
        scaleVal = screenHeight / rangeY

    colors = ReturnColorsRBG()

    for i in range(len(majorCirclesCenters)):
        pygame.gfxdraw.aacircle(solutionScreen, int((majorCirclesCenters[i][0] * scaleVal + screenWidth / 2)),
                                int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))

    pointPositions = ReturnPositions()
    counterNum = 0
    for point in tempPoints:
        pygame.draw.circle(solutionScreen, colors[point.color], (
            int(pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2),
            int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                           circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(solutionScreen,
                                int((pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2)),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), colors[point.color])

        counterNum += 1
    pygame.display.flip()


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


def SolveCube(screen, points, cubeMoves, solutionVec):  # BAD
    # 0 - R = The right face
    # 1 - L = The left face
    # 2 - U = The top face
    # 3 - D = The bottom face
    # 4 - F = The face at the front
    # 5 - B = The face at the back

    faceWithMaxColorIndex, maxColor = FindFaceWithMaxSameColor(points)
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
    while not CheckIfFaceIsSolved(faceWithMaxColorIndex, points):
        rotateInt = random.randint(0, 5)
        randDir = random.randint(0, 1)
        Rotate(screen, points, rotateInt, randDir, solutionVec, 0.75)
        cubeMoves.append((rotateInt, randDir))
        nit += 1
    print(nit)
    print("Face ", faceWithMaxColorIndex, " is solved:", CheckIfFaceIsSolved(faceWithMaxColorIndex, points))

    return cubeMoves


def FullyRandomizeCube(points):
    newIndices = list(range(len(points)))

    random.shuffle(newIndices)
    for pointIndex in range(len(points)):
        points[pointIndex].positionIndex = newIndices[pointIndex]


def RandomizeCube(screen, points, numRandomRotations, cubeMoves, solutionVec):
    random_values = [random.randint(0, 2) for _ in range(numRandomRotations)]
    random_bools = [random.choice([True, False]) for _ in range(numRandomRotations)]
    offsetVal = 0.75

    for randomIndex in range(numRandomRotations):
        Rotate(screen, points, random_values[randomIndex], random_bools[randomIndex], solutionVec, offsetVal)
        cubeMoves.append((random_values[randomIndex], random_bools[randomIndex]))
        # if random_bools[randomIndex]:
        #     print("Rotated circle", random_values[randomIndex] + 1, "Clockwise")
        # else:
        #     print("Rotated circle", random_values[randomIndex] + 1, "Counter-Clockwise")

    return cubeMoves


def ReturnFaces():
    face1 = [0]
    face2 = [1]
    face3 = [2]
    face4 = [3]
    face5 = [4]
    face6 = [5]
    return [face1, face2, face3, face4, face5, face6]


def ReturnPositions():
    return [(0, 56.276921), (-73.737244, 42.572217), (73.737244, 42.572217), (-48.737244, -28.138461),
            (48.737244, -28.138461), (0, -85.144435)]


def ReturnColorsRBG():
    return [(184, 10, 49), (0, 68, 175), (0, 156, 70), (255, 0, 255), (255, 214, 0), (255, 87, 0)]


def CreateAllPoints():
    red = MovingPoint(0, 0)

    blue = MovingPoint(1, 1)

    green = MovingPoint(2, 2)

    purple = MovingPoint(3, 3)

    yellow = MovingPoint(4, 4)

    cyan = MovingPoint(5, 5)

    return [red, blue, green, purple, yellow, cyan]


def ReturnCircleMovements():
    rotateCircle1CCW = [(1, 3), (3, 4), (4, 2), (2, 1)]
    rotateCircle2CCW = [(1, 5), (5, 4), (4, 0), (0, 1)]
    rotateCircle3CCW = [(0, 3), (3, 5), (5, 2), (2, 0)]

    return [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW]


def ReturnCircleMovementRotations():
    largeRadius = 75
    rotateCircle1CCW = [(0, 28.867513, largeRadius), (0, 28.867513, largeRadius), (0, 28.867513, largeRadius),
                        (0, 28.867513, largeRadius)]
    rotateCircle2CCW = [(-25, -14.433757, largeRadius), (-25, -14.433757, largeRadius), (-25, -14.433757, largeRadius),
                        (-25, -14.433757, largeRadius)]
    rotateCircle3CCW = [(25, -14.433757, largeRadius), (25, -14.433757, largeRadius), (25, -14.433757, largeRadius),
                        (25, -14.433757, largeRadius)]

    return [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW]


def ReturnCircleCoordsAndRadii():
    largeRadius = 75
    majorCirclesCenters = [(0, 28.867513), (-25, -14.433757), (25, -14.433757)]
    majorCirclesRadii = [largeRadius, largeRadius, largeRadius]
    return majorCirclesCenters, majorCirclesRadii
