import TwoMain
from matplotlib import pyplot as plt
import keyboard
import pygame
import numpy as np

pygame.init()

theCube = TwoMain.TheCube()
#
# fig, ax = plt.subplots()
# TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
#
# def update_plot(event):
#     inputVal = event.key
#
#     if inputVal == 'r':
#         TwoMain.ResetPoints(theCube.points)
#         TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
#
#     elif inputVal == 'x':
#         numRandomRotations = 3
#         TwoMain.RandomizeCube(theCube.points, numRandomRotations)
#         TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
#
#     elif inputVal == 'v':
#         TwoMain.FullyRandomizeCube(theCube.points)
#         TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
#
#     elif inputVal == 'a':
#         TwoMain.SolveCube(theCube.points)
#         TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
#
#     elif inputVal != ' ':
#         inputVal = int(event.key) - 1
#
#         if inputVal >= 6 or inputVal <= -1:
#             plt.close()
#         else:
#             TwoMain.Rotate(theCube.points, inputVal, not keyboard.is_pressed(' '))
#             TwoMain.PlotAllPoints(ax, theCube.points, 0, False)
#             TwoMain.CheckIfSolved(theCube.points)
#
#
# plt.connect('key_press_event', update_plot)
#
# while plt.fignum_exists(1):
#     plt.waitforbuttonpress()
#
# plt.close()

tempVec = [(108.484692, -39.539656), (89.807407, -51.850331),
                 (109.852814, -63.423552), (88.484692, -74.180672)]
totalX = 0
totalY = 0
for i in range(len(tempVec)):
    totalY += tempVec[i][1]
    totalX += tempVec[i][0]
average_x = totalX/len(tempVec)
average_y = totalY/len(tempVec)
print(average_x)
print(average_y)

moves = []
# Set up window
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("2D Rubiks Cube")

# Enable OpenGL acceleration for smoother rendering
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            keys = pygame.key.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rotateCircleIndex = TwoMain.GetClosestLargeCircle(mouse_x, mouse_y)
            moves.append((rotateCircleIndex, keys[pygame.K_SPACE]))
            TwoMain.Rotate(screen, theCube.points, rotateCircleIndex, keys[pygame.K_SPACE])
            if keys[pygame.K_SPACE]:
                print("Rotated circle", rotateCircleIndex + 1, "Clockwise")
            else:
                print("Rotated circle", rotateCircleIndex + 1, "Counter-Clockwise")

            TwoMain.CheckIfSolved(theCube.points)

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_r]:
                TwoMain.ResetPoints(theCube.points)
                moves = []

            elif pygame.key.get_pressed()[pygame.K_x]:
                numRandomRotations = 3
                moves = TwoMain.RandomizeCube(screen, theCube.points, numRandomRotations, moves)

            elif pygame.key.get_pressed()[pygame.K_v]:
                TwoMain.FullyRandomizeCube(theCube.points)

            elif pygame.key.get_pressed()[pygame.K_a]:
                moves = TwoMain.SolveCube(theCube.points, moves)

            elif pygame.key.get_pressed()[pygame.K_z]:
                if len(moves) > 0:
                    TwoMain.Rotate(theCube.points, moves[len(moves)-1][0], not moves[len(moves)-1][1])
                    moves.pop()
                    TwoMain.CheckIfSolved(theCube.points)

    TwoMain.updateGameScreen(screen, theCube.points)
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()








