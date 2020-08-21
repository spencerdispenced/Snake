
""" Functions for general running of game """
import pygame
from time import sleep


class Game_Functions():

    def __init__(self, game_display, width, height, snake, food):
        self.game_display = game_display
        self.width = width
        self.height = height
        self.snake = snake
        self.food = food
        self.score = 0
        self.score_multiplyer = 1
        self.high_score = self.__get_high_score()

    def check_events(self):
        """ check movement and quit events in game """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:  # prevent exact reverse direction
                if event.key == pygame.K_UP and not self.snake.direction == "DOWN":
                    self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and not self.snake.direction == "UP":
                    self.snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and not self.snake.direction == "RIGHT":
                    self.snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and not self.snake.direction == "LEFT":
                    self.snake.direction = "RIGHT"
                elif event.key == pygame.K_p:
                    self.pause()
                else:
                    continue

    def check_wall_collisions(self):
        """ Lose game if snake runs into edge of screen """
        snake_head_x_pos = self.snake.get_head()[0]
        snake_head_y_pos = self.snake.get_head()[1]
        if (
                snake_head_x_pos >= self.width or
                snake_head_x_pos < 0 or
                snake_head_y_pos >= self.height or
                snake_head_y_pos < 60
              ):

            self.snake.alive = False  # game over when snake runs over edge of screen

    def check_food_collision(self):
        if self.food.position == self.snake.get_head():
            eat_sound = pygame.mixer.Sound("Sounds/apple_crunch.wav")  # https://freesound.org/s/20267/
            pygame.mixer.Sound.play(eat_sound)
            self.snake.length += 1
            self.snake.speed += 0.5
            self.score += round((self.score_multiplyer))
            self.__check_high_score()
            self.score_multiplyer += 0.5  # score improves at increasing rate
            self.food.add_food()  # add another food object

        elif self.food.position in self.snake.get_body():  # food shouldn't appear inside snake
            self.food.add_food()

    def play_music(self):
        """ load and play game music """
        pygame.mixer.music.load("Sounds/game_music.wav")  # https://freesound.org/s/172561/
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # loop forever

    def game_over(self):
        """ Game over music and score and restart display"""
        pygame.mixer.music.stop()
        game_over_sound = pygame.mixer.Sound("Sounds/game_over.wav")  # https://freesound.org/s/76376/
        pygame.mixer.Sound.play(game_over_sound)

        # set up upper image for game over screen
        self.__render_and_blit(f"You Lost! Score is {self.score}")

        # set up lower image for game over screen, different parameters
        message_2_str = "Press Y to start over or N to quit"
        message_2 = pygame.font.SysFont("comicsansms", 20).render(message_2_str, True, (255, 255, 255))
        message_2_rect = self.__create_and_center_rect(message_2)
        message_2_rect.centery += 100  # move lower than message_1
        self.game_display.blit(message_2, message_2_rect)
        pygame.display.update()

    def start_message(self):
        """ Display message before game starts """
        self.__render_and_blit("Press any key to start")
        while True:  # wait until a key is pressed to start game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    return

    def check_restart(self):
        """ Check if user wants to restart the game """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        self.snake.reset()
                        self.reset_score()
                        return True

                    if event.key == pygame.K_n or event.key == pygame.K_q:
                        return False

    def pause(self):
        """ Pause the game """
        self.__render_and_blit("Paused, press p to resume")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return

    def show_score(self):
        """ Show score on screen """
        score_str = f"Score: {self.score}"
        score_image = pygame.font.SysFont(None, 35).render(
                             score_str, True, (0, 0, 0), (255, 255, 255))
        score_rect = score_image.get_rect()
        self.game_display.blit(score_image, score_rect)

    def show_high_score(self):
        """ Show a persistant high score on screen """
        score_str = f" High Score: {self.high_score}"
        score_image = pygame.font.SysFont(None, 35).render(
                             score_str, True, (0, 0, 0), (255, 255, 255))
        score_rect = score_image.get_rect()
        game_rect = self.game_display.get_rect()
        game_rect.left += 40
        self.game_display.blit(score_image, game_rect.midtop)

    def reset_score(self):
        """ Reset the score """
        self.score = 0
        self.score_multiplyer = 1

    def __create_and_center_rect(self, msg):
        """ Get rect and set center values """
        message_rect = msg.get_rect()
        message_rect.centerx = int(self.width / 2)
        message_rect.centery = int(self.height / 2)
        return message_rect

    def __render_and_blit(self, msg):
        """ Print messages to screen, comic sans, 35pt, center of screen """
        message = pygame.font.SysFont("comicsansms", 35).render(msg, True, (255, 255, 255))
        message_rect = self.__create_and_center_rect(message)
        self.game_display.blit(message, message_rect)
        pygame.display.update()

    def __get_high_score(self):
        """ Read file to get high score """
        file_name = "high_score.txt"
        try:
            file = open(file_name, 'r+')
        except FileNotFoundError:
            try:
                file = open(file_name, 'x')
            except IOError:
                raise Exception(f"File '{file_name}' could not be created")
            file.close()
            try:
                file = open(file_name, 'r+')
            except IOError:
                raise Exception(f"File '{file_name}' could not be opened")

        high_score = file.read()
        file.close()
        if high_score == '':
            return (0)
        else:
            return int(high_score)

    def __write_high_score(self, score):
        """ write new high score to file """
        try:
            file = open("high_score.txt", 'r+')
        except IOError:
            raise Exception(f"File '{file_name}' could not be opened")
        file.write(score)
        file.close()

    def __check_high_score(self):
        """ check high score and write to file """
        if self.score > self.high_score:
            self.high_score = self.score
            self.__write_high_score(str(self.score))
