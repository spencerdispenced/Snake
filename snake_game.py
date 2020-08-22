
import pygame

from snake import Snake
from food import Food
from settings import Settings

from game_functions import Game_Functions


def main():
    """ main function to run game """
    pygame.init()
    clock = pygame.time.Clock()
    s = Settings()

    snake = Snake(s.width, s.height, 
                  s.game_display, s.snake_color_1,
                  s.snake_color_2, s.border_color)
    food = Food(s.game_display, s.food_color, s.width, s.height)
    gf = Game_Functions(s.game_display, s.width, s.height, snake, food)

    gf.start_message()
    gf.play_music()

    game_running = True
    while game_running:
        while not snake.alive:
            # After game over, ask player if they want to continue
            gf.game_over()

            if gf.check_restart():
                gf.play_music()
                break
            else:
                game_running = False
                break

        # Regular game actions
        gf.check_events()
        s.draw_screen()
        gf.show_score()
        gf.show_high_score()
        snake.move()
        gf.check_food_collision()
        gf.check_wall_collisions()
        food.draw_food()

        clock.tick(snake.speed)  # controls speed of while loop

# TODO
# High score is 315


if __name__ == "__main__":
    main()
