import Library22
import pygame

pygame.init()

theCube = Library22.TheCube()

width, height = 800, 600
solutionScreen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("2D Rubiks Cube")

randomOrder = Library22.CreateRandomOrder(solutionScreen)
# print(randomOrder)
Library22.ShowSolution(solutionScreen, randomOrder)

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
            rotateCircleIndex = Library22.GetClosestLargeCircle(mouse_x, mouse_y)
            moves.append((rotateCircleIndex, keys[pygame.K_SPACE]))
            Library22.Rotate(screen, theCube.points, rotateCircleIndex, keys[pygame.K_SPACE], randomOrder, 0.75)
            # if keys[pygame.K_SPACE]:
            #     print("Rotated circle", rotateCircleIndex + 1, "Clockwise")
            # else:
            #     print("Rotated circle", rotateCircleIndex + 1, "Counter-Clockwise")

            Library22.CheckIfSolved(theCube.points, randomOrder)

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_r]:
                # Library22.ResetPoints(theCube.points)
                moves = []
                randomOrder = Library22.CreateRandomOrder(solutionScreen)

            elif pygame.key.get_pressed()[pygame.K_x]:
                numRandomRotations = 3
                moves = Library22.RandomizeCube(screen, theCube.points, numRandomRotations, moves, randomOrder)
            # elif pygame.key.get_pressed()[pygame.K_v]:
            #     moves = []
            #     Library22.FullyRandomizeCube(theCube.points)

            elif pygame.key.get_pressed()[pygame.K_a]:
                moves = Library22.SolveCube(screen, theCube.points, moves, randomOrder)

            elif pygame.key.get_pressed()[pygame.K_z]:
                if len(moves) > 0:
                    Library22.Rotate(screen, theCube.points, moves[len(moves)-1][0], not moves[len(moves)-1][1], randomOrder, 0.75)
                    moves.pop()
                    Library22.CheckIfSolved(theCube.points, randomOrder)

    Library22.updateGameScreen(screen, theCube.points, randomOrder)
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
