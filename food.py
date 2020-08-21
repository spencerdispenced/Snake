
import pygame
import random


class Food:
    """ Create a food object """
    def __init__(self, game_display, color, screen_width, screen_height):
        self.game_display = game_display
        self.food_color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.add_food()  # set an intitial food position

    def draw_food(self):
        """ Draw the food to the screen """
        pygame.draw.rect(self.game_display,
                         self.food_color,
                         [self.position[0], self.position[1], 20, 20])
        pygame.display.update()

    def add_food(self):
        """ Add food in random position within bounds of game board """
        self.position = [random.randrange(0, self.screen_width-20, 20),
                         random.randrange(80, self.screen_height-20, 20)]
