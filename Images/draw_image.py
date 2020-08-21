
""" Script to draw background images """

import pygame


def draw_background():
    """ Draw image of certain color, in checkered pattern """
    surface = pygame.display.set_mode((480, 480))
    for y in range(0, 480):
        for x in range(0, 480):
            if (x + y) % 2 == 0:  # every even square
                r = pygame.Rect((x * 20, y * 20), (20, 20))
                pygame.draw.rect(surface, (44, 190, 36), r)
            else:
                rr = pygame.Rect((x * 20, y * 20), (20, 20))
                pygame.draw.rect(surface, (204, 185, 90), rr)
    pygame.image.save(surface, "game_board2.bmp")


draw_background()
