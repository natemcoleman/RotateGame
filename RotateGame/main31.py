import Library31
import pygame

pygame.init()

theCube = Library31.TheCube()

width, height = 800, 600
solutionScreen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("2D Rubiks Cube")

randomOrder = Library31.CreateRandomOrder(solutionScreen)
# print(randomOrder)
Library31.ShowSolution(solutionScreen, randomOrder)

moves = []
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
            rotateCircleIndex = Library31.GetClosestLargeCircle(mouse_x, mouse_y)
            moves.append((rotateCircleIndex, keys[pygame.K_SPACE]))
            Library31.Rotate(screen, theCube.points, rotateCircleIndex, keys[pygame.K_SPACE], randomOrder, 0.75)
            # if keys[pygame.K_SPACE]:
            #     print("Rotated circle", rotateCircleIndex + 1, "Clockwise")
            # else:
            #     print("Rotated circle", rotateCircleIndex + 1, "Counter-Clockwise")

            Library31.CheckIfSolved(theCube.points, randomOrder)

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_r]:
                # Library31.ResetPoints(theCube.points)
                moves = []
                randomOrder = Library31.CreateRandomOrder(solutionScreen)

            elif pygame.key.get_pressed()[pygame.K_x]:
                numRandomRotations = 3
                moves = Library31.RandomizeCube(screen, theCube.points, numRandomRotations, moves, randomOrder)
            # elif pygame.key.get_pressed()[pygame.K_v]:
            #     moves = []
            #     Library31.FullyRandomizeCube(theCube.points)

            elif pygame.key.get_pressed()[pygame.K_a]:
                moves = Library31.SolveCube(screen, theCube.points, moves, randomOrder)

            elif pygame.key.get_pressed()[pygame.K_z]:
                if len(moves) > 0:
                    Library31.Rotate(screen, theCube.points, moves[len(moves)-1][0], not moves[len(moves)-1][1], randomOrder, 0.75)
                    moves.pop()
                    Library31.CheckIfSolved(theCube.points, randomOrder)

    Library31.updateGameScreen(screen, theCube.points, randomOrder)
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
