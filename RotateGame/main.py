import RotateLibrary
import pygame

pygame.init()

theCube = RotateLibrary.TheCube()
solutionCube = RotateLibrary.TheCube()

width, height = 800, 600
solutionScreen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("2D Rubiks Cube")

randomOrder = RotateLibrary.CreateRandomOrder(solutionCube, solutionScreen)
RotateLibrary.ShowSolution(solutionCube, solutionScreen, randomOrder)

moves = []
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Enable OpenGL acceleration for smoother rendering
# pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
# pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

# Game loop
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
            # RotateLibrary.CheckIfSolved(theCube, randomOrder)

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_r]:
                moves = []
                randomOrder = RotateLibrary.CreateRandomOrder(solutionCube, solutionScreen)

            elif pygame.key.get_pressed()[pygame.K_x]:
                numRandomRotations = 3
                moves = RotateLibrary.RandomizeCube(screen, theCube, numRandomRotations, moves, randomOrder)

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
