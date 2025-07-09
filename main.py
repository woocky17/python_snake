# src/snakegame/main.py

import pygame
from src.core.logic import SnakeGame
from src.ui.draw import (
    draw_background_and_borders, draw_apple, draw_snake, draw_head_blink, draw_score, show_gameover_screen
)

# --- CONFIGURACIÓN ---
WIDTH = 600
HEIGHT = 400
TILE_SIZE = 10
BORDER_COLOR = (0, 0, 0)
BORDER_THICKNESS = 2
BG_COLOR = (34, 70, 34)
SNAKE_COLOR = (144, 238, 144)
APPLE_COLOR = (213, 50, 80)
SCORE_COLOR = (255, 255, 255)
GAMEOVER_COLOR = (213, 50, 80)
FPS = 15

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de la Serpiente")

background_texture = pygame.Surface((TILE_SIZE, TILE_SIZE))
background_texture.fill(BG_COLOR)
snake_texture = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
snake_texture.fill(SNAKE_COLOR)
apple_texture = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
apple_texture.fill(APPLE_COLOR)

font = pygame.font.SysFont("consolas", 15)
font_msg = pygame.font.SysFont("consolas", 15, bold=True)

clock = pygame.time.Clock()
game = SnakeGame(WIDTH, HEIGHT, TILE_SIZE)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.queue_direction('IZQ')
                elif event.key == pygame.K_RIGHT:
                    game.queue_direction('DER')
                elif event.key == pygame.K_UP:
                    game.queue_direction('ARR')
                elif event.key == pygame.K_DOWN:
                    game.queue_direction('ABA')
        if not game.game_over:
            game.step()
            state = game.get_state()
            draw_background_and_borders(
                window, WIDTH, HEIGHT, TILE_SIZE, background_texture, BORDER_COLOR, BORDER_THICKNESS)
            draw_apple(window, apple_texture,
                       state['food_x'], state['food_y'], TILE_SIZE)
            draw_snake(window, snake_texture, state['snake_body'])
            draw_score(window, state['snake_length'] - 1, font)
            pygame.display.update()
            if state['game_over']:
                draw_head_blink(window, state['head'], state['snake_body'], state['food_x'], state['food_y'], TILE_SIZE, background_texture,
                                BORDER_COLOR, BORDER_THICKNESS, apple_texture, snake_texture, state['snake_length'] - 1, font, draw_score)
                pygame.display.update()
                pygame.time.wait(400)
                action = show_gameover_screen(window, WIDTH, HEIGHT, font, font_msg,
                                              state['snake_length'] - 1, draw_score, BG_COLOR, GAMEOVER_COLOR, SCORE_COLOR)
                if action == 'salir':
                    running = False
                elif action == 'continuar':
                    game.reset()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
