# src/snakegame/ui/draw.py

import pygame


def draw_background_and_borders(surface, width, height, tile_size, background_texture, border_color, border_thickness):
    for i in range(0, width, tile_size):
        for j in range(0, height, tile_size):
            surface.blit(background_texture, (i, j))
    pygame.draw.rect(surface, border_color,
                     (0, 0, width, height), border_thickness)


def draw_apple(surface, apple_texture, food_x, food_y, tile_size):
    apple_rect = apple_texture.get_rect(
        center=(food_x + tile_size // 2, food_y + tile_size // 2))
    surface.blit(apple_texture, apple_rect.topleft)


def draw_snake(surface, snake_texture, snake_body):
    for segment in snake_body:
        surface.blit(snake_texture, (segment[0], segment[1]))


def draw_head_blink(surface, head, snake_body, food_x, food_y, tile_size, background_texture, border_color, border_thickness, apple_texture, snake_texture, score, font, draw_score, blink_times=3):
    for _ in range(blink_times):
        draw_background_and_borders(surface, surface.get_width(), surface.get_height(
        ), tile_size, background_texture, border_color, border_thickness)
        draw_apple(surface, apple_texture, food_x, food_y, tile_size)
        for segment in snake_body[:-1]:
            surface.blit(snake_texture, (segment[0], segment[1]))
        head_flash = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
        head_flash.fill((255, 0, 0))
        surface.blit(head_flash, (head[0], head[1]))
        draw_score(surface, score, font)
        pygame.display.update()
        pygame.time.wait(150)
        draw_background_and_borders(surface, surface.get_width(), surface.get_height(
        ), tile_size, background_texture, border_color, border_thickness)
        draw_apple(surface, apple_texture, food_x, food_y, tile_size)
        for segment in snake_body[:-1]:
            surface.blit(snake_texture, (segment[0], segment[1]))
        surface.blit(snake_texture, (head[0], head[1]))
        draw_score(surface, score, font)
        pygame.display.update()
        pygame.time.wait(150)


def draw_score(surface, score, font, color=(255, 255, 255), margin=10):
    text = font.render(f"Puntuación: {score}", True, color)
    text_rect = text.get_rect()
    text_rect.topleft = (margin, surface.get_height() -
                         text_rect.height - margin)
    surface.blit(text, text_rect)


def show_gameover_screen(surface, width, height, font, font_msg, score, draw_score, color_bg, color_msg, color_score):
    while True:
        surface.fill(color_bg)
        message = font_msg.render(
            "¡Perdiste! Presiona C para continuar o Q para salir", True, color_msg)
        message_rect = message.get_rect(center=(width // 2, height // 3))
        surface.blit(message, message_rect)
        draw_score(surface, score, font, color_score)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return 'salir'
                if event.key == pygame.K_c:
                    return 'continuar'
