import RotateLibrary
import pygame

pygame.init()

theCube = RotateLibrary.TheCube(41)
numRandomRotationsForSolution = 5
width, height = 800, 600
numRandomRotationsShuffle = 3

solutionCube = RotateLibrary.TheCube(theCube.typeNum)

solutionScreen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("2D Rubiks Cube")

randomOrder = RotateLibrary.CreateRandomOrder(solutionCube, solutionScreen, numRandomRotationsForSolution)
RotateLibrary.ShowSolution(solutionCube, solutionScreen, randomOrder)

moves = []
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            keys = pygame.key.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rotateCircleIndex = RotateLibrary.GetClosestLargeCircle(theCube, mouse_x, mouse_y)
            moves.append((rotateCircleIndex, keys[pygame.K_SPACE]))
            RotateLibrary.Rotate(screen, theCube, rotateCircleIndex, keys[pygame.K_SPACE], randomOrder, 0.75) #problem here
            RotateLibrary.CheckIfSolved(theCube, randomOrder)

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_r]:
                moves = []
                randomOrder = RotateLibrary.CreateRandomOrder(solutionCube, solutionScreen, numRandomRotationsForSolution)

            elif pygame.key.get_pressed()[pygame.K_x]:
                moves = RotateLibrary.RandomizeCube(screen, theCube, numRandomRotationsShuffle, moves, randomOrder)

            elif pygame.key.get_pressed()[pygame.K_a]:
                moves = RotateLibrary.SolveCube(screen, theCube, moves, randomOrder)

            elif pygame.key.get_pressed()[pygame.K_z]:
                if len(moves) > 0:
                    RotateLibrary.Rotate(screen, theCube, moves[len(moves)-1][0], not moves[len(moves)-1][1], randomOrder, 0.75)
                    moves.pop()
                    RotateLibrary.CheckIfSolved(theCube, randomOrder)
    RotateLibrary.updateGameScreen(screen, theCube, randomOrder) 
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
