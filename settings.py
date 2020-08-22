
import pygame


class Settings():
    """ Creates the general screen and color settings"""
    __instance__ = None

    def __init__(self):
        """ Singleton class """
        if Settings.__instance__ is None:
            Settings.__instance__ = self
        else:
            raise Exception("Cannot create another settings class")

        self.width = 480
        self.height = 480
        self.snake_color_1 = (0, 0, 0)  # Black
        self.snake_color_2 = (255, 255, 0)  # Yellow
        self.food_color = (255, 0, 0)  # Red
        self.border_color = (255, 255, 255)  # White
        self.game_display = self.init_screen()
        self.game_board = pygame.image.load("Images/game_board.bmp")

    def init_screen(self):
        """ Setup the initial screen parameters """
        game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Spencers Snake Game")

        return game_display

    def draw_screen(self):
        """ Draw the screen """
        game_board_size = pygame.Rect(0, 60, 480, 420)  # create game board sized rect
        self.game_display.fill(self.border_color)  # fill background as white
        self.game_display.blit(self.game_board, game_board_size)  # send image to background
