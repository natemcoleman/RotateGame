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

    if screenWidth < screenHeight:
        scaleVal = screenWidth / rangeX

    else:
        scaleVal = screenHeight / rangeY

    majorCirclesCenters, majorCirclesRadii = ReturnCircleCoordsAndRadii()
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h

    closest_circle_index = None
    min_distance_to_edge = float('inf')

    for i, (center_x, center_y) in enumerate(majorCirclesCenters):
        distance_to_center = math.sqrt((mouseX - (screenWidth / 2) - center_x * scaleVal) ** 2 + (
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

    if theta1 < 0 < theta2:
        theta2 -= 2 * math.pi

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
            initalCoords = pol2cart(circleRadius, equally_spaced_vector[i])
            returnCoords.append((initalCoords[0] + circleCenter[0], initalCoords[1] + circleCenter[1]))

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


def AnimatePos1ToPos2(screen, points, rotateIndex, CW):
    # Clear the screen
    white = (255, 255, 255)
    screen.fill(white)
    circle_radius = 10
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

    font_size = 36
    font_size_small = 12
    font = pygame.font.Font(None, font_size)  # Use the default system font
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
        pygame.gfxdraw.aacircle(screen, int((pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2)),
                                int((pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)),
                                int(circle_radius * math.sqrt(scaleVal)), colors[point.color])

    xyCoords = GetXYRotationCoords(points, rotateIndex, CW)

    for frame in range(len(xyCoords[0])):
        # print("frame:", frame)
        screen.fill(white)
        for i in range(len(majorCirclesCenters)):
            pygame.gfxdraw.aacircle(screen, int((majorCirclesCenters[i][0] * scaleVal + screenWidth / 2)),
                                    int((majorCirclesCenters[i][1] * scaleVal + screenHeight / 2)),
                                    int(majorCirclesRadii[i] * scaleVal), (0, 0, 0))
        for coordIndex in range(len(xyCoords)):
            # print("coordIndex:", coordIndex)
            pygame.draw.circle(screen, colors[points[coordIndex].color], (
                int(xyCoords[coordIndex][frame][0] * scaleVal + screenWidth / 2),
                int(xyCoords[coordIndex][frame][1] * scaleVal + screenHeight / 2)),
                               circle_radius * math.sqrt(scaleVal))
            pygame.gfxdraw.aacircle(screen, int((xyCoords[coordIndex][frame][0] * scaleVal + screenWidth / 2)),
                                    int((xyCoords[coordIndex][frame][1] * scaleVal + screenHeight / 2)),
                                    int(circle_radius * math.sqrt(scaleVal)), colors[points[coordIndex].color])
        pygame.display.flip()
        pygame.time.delay(10)


def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y


def updateGameScreen(screen, points):
    # Clear the screen
    white = (255, 255, 255)
    screen.fill(white)
    circle_radius = 10
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

    font_size = 36
    font_size_small = 12
    font = pygame.font.Font(None, font_size)  # Use the default system font
    font2 = pygame.font.Font(None, font_size_small)
    text_color = (0, 0, 0)  # Black

    for i in range(len(majorCirclesCenters)):
        pygame.gfxdraw.aacircle(screen, int((majorCirclesCenters[i][0] * scaleVal + screenWidth / 2)),
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
        int(pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2),
        int(pointPositions[point.positionIndex][1] * scaleVal + screenHeight / 2)), circle_radius * math.sqrt(scaleVal))
        pygame.gfxdraw.aacircle(screen, int((pointPositions[point.positionIndex][0] * scaleVal + screenWidth / 2)),
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

    if CheckIfSolved(points):
        font_size = 48
        font = pygame.font.Font(None, font_size)  # Use the default system font
        text_color = (0, 0, 0)  # Black

        text_surface = font.render("SOLVED!", True, text_color)
        text_x = (pygame.display.Info().current_w - text_surface.get_width()) // 2
        text_y = 25
        text_rect = text_surface.get_rect()
        text_rect.topleft = (text_x, text_y)
        screen.blit(text_surface, text_rect)


def ResetPoints(points):
    for pointIndex in range(len(points)):
        points[pointIndex].positionIndex = pointIndex


def Rotate(screen, points, circleNum, CW):
    allMovements = ReturnCircleMovements()
    movements = allMovements[circleNum]

    AnimatePos1ToPos2(screen, points, circleNum, CW)

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

    # print("SOLVED!")
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


def SolveCube(screen, points, cubeMoves):  # BAD
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
        rotateInt = random.randint(0, 5)
        randDir = random.randint(0, 1)
        Rotate(screen, points, rotateInt, randDir)
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


def RandomizeCube(screen, points, numRandomRotations, cubeMoves):
    random_values = [random.randint(0, len(ReturnCircleMovements())-1) for _ in range(numRandomRotations)]
    random_bools = [random.choice([True, False]) for _ in range(numRandomRotations)]

    for randomIndex in range(numRandomRotations):
        Rotate(screen, points, random_values[randomIndex], random_bools[randomIndex])
        cubeMoves.append((random_values[randomIndex], random_bools[randomIndex]))
        # if random_bools[randomIndex]:
        #     print("Rotated circle", random_values[randomIndex] + 1, "Clockwise")
        # else:
        #     print("Rotated circle", random_values[randomIndex] + 1, "Counter-Clockwise")

    return cubeMoves


def ReturnFaces():
    face1 = [0, 1, 4]
    face2 = [2, 3, 6]
    face3 = [5, 7, 8]
    face4 = [9, 11, 13]
    face5 = [10, 14, 16]
    face6 = [12, 15, 17]
    return [face1, face2, face3, face4, face5, face6]


def ReturnPositions():
    return [(0, 45.825757), (-13.671875, 36.962208), (13.671875, 36.962208), (0, 31.721444), (-23.4375, 24.762544), (23.4375, 24.762544), (-9.765625, 22.809155), (9.765625, 22.809155), (0, 15), (0, -15), (-9.765625, -22.809155), (9.765625, -22.809155), (-23.4375, -24.762544), (23.4375, -24.762544), (0, -31.721444), (-13.671875, -36.962208), (13.671875, -36.962208), (0, -45.825757)]


def ReturnColorsRBG():
    return [(184, 10, 49), (0, 68, 175), (0, 156, 70), (255, 0, 255), (255, 214, 0), (255, 87, 0)]


def CreateAllPoints():
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

    return [red1, red2, red3, blue1, blue2, blue3, green1, green2, green3, purple1, purple2,
            purple3, yellow1, yellow2, yellow3, cyan1, cyan2, cyan3]


def ReturnCircleMovements():
    rotateCircle1CCW = [(0, 2), (2, 5), (5, 13), (13, 16), (16, 17), (17, 0)]
    rotateCircle2CCW = [(1, 3), (3, 7), (7, 11), (11, 14), (14, 15), (15, 1)]
    rotateCircle3CCW = [(4, 6), (6, 8), (8, 9), (9, 10), (10, 12), (12, 4)]
    rotateCircle4CCW = [(0, 17), (17, 15), (15, 12), (12, 4), (4, 1), (1, 0)]
    rotateCircle5CCW = [(2, 16), (16, 14), (14, 10), (10, 6), (6, 3), (3, 2)]
    rotateCircle6CCW = [(5, 13), (13, 11), (11, 9), (9, 8), (8, 7), (7, 5)]

    return [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW, rotateCircle4CCW, rotateCircle5CCW, rotateCircle6CCW]


def ReturnCircleMovementRotations():
    smallRadius = 50/2
    mediumRadius = 75/2
    largeRadius = 100/2
    rotateCircle1CCW = [(-20, 0, largeRadius), (-20, 0, largeRadius), (-20, 0, largeRadius), (-20, 0, largeRadius), (-20, 0, largeRadius), (-20, 0, largeRadius)]
    rotateCircle2CCW = [(-20, 0, mediumRadius), (-20, 0, mediumRadius), (-20, 0, mediumRadius), (-20, 0, mediumRadius), (-20, 0, mediumRadius), (-20, 0, mediumRadius)]
    rotateCircle3CCW = [(-20, 0, smallRadius), (-20, 0, smallRadius), (-20, 0, smallRadius), (-20, 0, smallRadius), (-20, 0, smallRadius), (-20, 0, smallRadius)]
    rotateCircle4CCW = [(20, 0, largeRadius), (20, 0, largeRadius), (20, 0, largeRadius), (20, 0, largeRadius), (20, 0, largeRadius), (20, 0, largeRadius)]
    rotateCircle5CCW = [(20, 0, mediumRadius), (20, 0, mediumRadius), (20, 0, mediumRadius), (20, 0, mediumRadius), (20, 0, mediumRadius), (20, 0, mediumRadius)]
    rotateCircle6CCW = [(20, 0, smallRadius), (20, 0, smallRadius), (20, 0, smallRadius), (20, 0, smallRadius), (20, 0, smallRadius), (20, 0, smallRadius)]

    return [rotateCircle1CCW, rotateCircle2CCW, rotateCircle3CCW, rotateCircle4CCW, rotateCircle5CCW, rotateCircle6CCW]


def ReturnCircleCoordsAndRadii():
    smallRadius = 50/2
    mediumRadius = 75/2
    largeRadius = 100/2
    majorCirclesCenters = [(-20, 0), (-20, 0), (-20, 0), (20, 0), (20, 0),
                           (20, 0)]
    majorCirclesRadii = [largeRadius, mediumRadius, smallRadius, largeRadius, mediumRadius, smallRadius]
    return majorCirclesCenters, majorCirclesRadii
