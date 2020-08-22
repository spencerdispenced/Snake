
import pygame


class Snake:
    """ Create a snake with initial starting position """
    def __init__(self, x_pos, y_pos,
                 game_display, snake_color_1,
                 snake_color_2, border_color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.game_display = game_display
        self.snake_color_1 = snake_color_1
        self.snake_color_2 = snake_color_2
        self.border_color = border_color
        self.POS_CHANGE = 20
        self.reset()

    def reset(self):
        """ Reset snake to initial state """
        self.body = [[int(self.x_pos/2), int(self.y_pos/2)]]  # initial snake starts at center of screen
        self.direction = "UP"
        self.length = 1
        self.alive = True
        self.speed = 10

    def get_body(self):
        return self.body

    def get_head(self):
        return self.body[0]

    def move(self):
        """ Moves the snake based on current direction """
        piece = []
        if self.direction == "UP":
            piece = [self.body[0][0], self.body[0][1] - self.POS_CHANGE]  # create piece at new coordinates
        elif self.direction == "DOWN":
            piece = [self.body[0][0], self.body[0][1] + self.POS_CHANGE]
        elif self.direction == "LEFT":
            piece = [self.body[0][0] - self.POS_CHANGE, self.body[0][1]]
        elif self.direction == "RIGHT":
            piece = [self.body[0][0] + self.POS_CHANGE, self.body[0][1]]

        if piece:
            if piece in self.body:  # Lose game if snake touches itself
                self.alive = False
            else:
                self.body.insert(0, piece)  # insert new piece at head of snake
                if len(self.body) > self.length:
                    self.body.pop()   # delete last piece of snake, if length isnt increased

        self.draw_snake()

    def draw_snake(self):
        """ Draws the snake to the screen """
        snake_body = self.get_body()
        for pos in snake_body:  # draw entire snake
            p = pygame.Rect(pos[0], pos[1], 20, 20)
            if snake_body.index(pos) % 3 == 0:  # every third section is black, others are yellow
                pygame.draw.rect(self.game_display, self.snake_color_1, p)
            else:
                pygame.draw.rect(self.game_display, self.snake_color_2, p)
