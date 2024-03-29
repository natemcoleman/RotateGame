import Library32
import pygame

pygame.init()

theCube = Library32.TheCube()

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
            rotateCircleIndex = Library32.GetClosestLargeCircle(mouse_x, mouse_y)
            moves.append((rotateCircleIndex, keys[pygame.K_SPACE]))
            Library32.Rotate(screen, theCube.points, rotateCircleIndex, keys[pygame.K_SPACE])
            # if keys[pygame.K_SPACE]:
            #     print("Rotated circle", rotateCircleIndex + 1, "Clockwise")
            # else:
            #     print("Rotated circle", rotateCircleIndex + 1, "Counter-Clockwise")

            Library32.CheckIfSolved(theCube.points)

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_r]:
                Library32.ResetPoints(theCube.points)
                moves = []

            elif pygame.key.get_pressed()[pygame.K_x]:
                numRandomRotations = 3
                moves = Library32.RandomizeCube(screen, theCube.points, numRandomRotations, moves)

            # elif pygame.key.get_pressed()[pygame.K_v]:
            #     Library32.FullyRandomizeCube(theCube.points)

            # elif pygame.key.get_pressed()[pygame.K_a]:
            #     moves = Library32.SolveCube(screen, theCube.points, moves)

            elif pygame.key.get_pressed()[pygame.K_z]:
                if len(moves) > 0:
                    Library32.Rotate(screen, theCube.points, moves[len(moves)-1][0], not moves[len(moves)-1][1])
                    moves.pop()
                    Library32.CheckIfSolved(theCube.points)

    Library32.updateGameScreen(screen, theCube.points)
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()








