import pygame

TITLE = "Game"
SIZE = (1000, 600)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    # keys = pygame.key.get_pressed()

    return True


def draw():
    screen.fill((0, 0, 0))
    # screen.blit()


def game_logic():
    pass


def run_game():
    while handle_events():
        game_logic()

        draw()

        pygame.display.update(window_rect)

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    window_rect = pygame.Rect((0, 0), SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption(TITLE)
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
    run_game()