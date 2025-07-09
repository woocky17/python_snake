# src/snakegame/ui/draw.py
import pygame  # Importa la librería pygame

# Dibuja el fondo de la pantalla y los bordes del área de juego


def draw_background_and_borders(surface, width, height, tile_size, background_texture, border_color, border_thickness):
    # Rellena el fondo con la textura en mosaico
    for i in range(0, width, tile_size):  # Itera sobre el ancho en pasos de tile_size
        for j in range(0, height, tile_size):  # Itera sobre el alto en pasos de tile_size
            # Dibuja la textura de fondo en la posición (i, j)
            surface.blit(background_texture, (i, j))
    # Dibuja el borde alrededor del área de juego
    pygame.draw.rect(surface, border_color, (0, 0, width, height),
                     border_thickness)  # Dibuja un rectángulo como borde


# Dibuja la manzana (comida) en la posición indicada
def draw_apple(surface, apple_texture, food_x, food_y, tile_size):
    # Centra la textura de la manzana en la celda
    apple_rect = apple_texture.get_rect(center=(
        # Calcula el rectángulo centrado
        food_x + tile_size // 2, food_y + tile_size // 2))
    # Dibuja la manzana en la posición calculada
    surface.blit(apple_texture, apple_rect.topleft)


# Dibuja el cuerpo de la serpiente
def draw_snake(surface, snake_texture, snake_body):
    # Dibuja cada segmento de la serpiente
    for segment in snake_body:  # Itera sobre cada segmento de la serpiente
        # Dibuja el segmento en la posición correspondiente
        surface.blit(snake_texture, (segment[0], segment[1]))


# Hace parpadear la cabeza de la serpiente cuando choca (efecto de colisión)
def draw_head_blink(surface, head, snake_body, food_x, food_y, tile_size, background_texture, border_color, border_thickness, apple_texture, snake_texture, score, font, draw_score, blink_times=3):
    for _ in range(blink_times):  # Repite el parpadeo la cantidad de veces indicada
        # Dibuja el fondo y la manzana
        draw_background_and_borders(surface, surface.get_width(), surface.get_height(
        ), tile_size, background_texture, border_color, border_thickness)  # Fondo y bordes
        draw_apple(surface, apple_texture, food_x,
                   food_y, tile_size)  # Manzana
        # Dibuja el cuerpo de la serpiente (sin la cabeza)
        # Itera sobre todos los segmentos menos la cabeza
        for segment in snake_body[:-1]:
            # Dibuja el segmento
            surface.blit(snake_texture, (segment[0], segment[1]))
        # Dibuja la cabeza parpadeando en rojo
        # Crea una superficie para la cabeza
        head_flash = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
        head_flash.fill((255, 0, 0))  # La pinta de rojo
        surface.blit(head_flash, (head[0], head[1]))  # Dibuja la cabeza roja
        draw_score(surface, score, font)  # Dibuja la puntuación
        pygame.display.update()  # Actualiza la pantalla
        pygame.time.wait(150)  # Espera 150 ms
        # Dibuja de nuevo la cabeza normal
        draw_background_and_borders(surface, surface.get_width(), surface.get_height(
        ), tile_size, background_texture, border_color, border_thickness)  # Fondo y bordes
        draw_apple(surface, apple_texture, food_x,
                   food_y, tile_size)  # Manzana
        for segment in snake_body[:-1]:  # Dibuja el cuerpo sin la cabeza
            surface.blit(snake_texture, (segment[0], segment[1]))
        # Dibuja la cabeza normal
        surface.blit(snake_texture, (head[0], head[1]))
        draw_score(surface, score, font)  # Dibuja la puntuación
        pygame.display.update()  # Actualiza la pantalla
        pygame.time.wait(150)  # Espera 150 ms


# Dibuja la puntuación en pantalla
def draw_score(surface, score, font, color=(255, 255, 255), margin=10):
    # Renderiza el texto de la puntuación
    text = font.render(f"Puntuación: {score}", True, color)
    text_rect = text.get_rect()  # Obtiene el rectángulo del texto
    # Posiciona el texto en la esquina inferior izquierda
    text_rect.topleft = (margin, surface.get_height() -
                         text_rect.height - margin)
    surface.blit(text, text_rect)  # Dibuja el texto en la pantalla


# Muestra la pantalla de Game Over y espera a que el usuario decida continuar o salir
def show_gameover_screen(surface, width, height, font, font_msg, score, draw_score, color_bg, color_msg, color_score):
    while True:  # Bucle hasta que el usuario pulse una tecla válida
        surface.fill(color_bg)  # Rellena el fondo con el color de Game Over
        message = font_msg.render(
            # Renderiza el mensaje
            "¡Perdiste! Presiona C para continuar o Q para salir", True, color_msg)
        message_rect = message.get_rect(
            center=(width // 2, height // 3))  # Centra el mensaje
        surface.blit(message, message_rect)  # Dibuja el mensaje en pantalla
        # Dibuja la puntuación final
        draw_score(surface, score, font, color_score)
        pygame.display.update()  # Actualiza la pantalla
        for event in pygame.event.get():  # Espera eventos del usuario
            if event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if event.key == pygame.K_q:  # Si es Q, salir
                    return 'salir'
                if event.key == pygame.K_c:  # Si es C, continuar
                    return 'continuar'
