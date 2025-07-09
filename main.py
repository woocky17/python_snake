import pygame  # Importa la librería principal para gráficos y eventos
from src.core.logic import SnakeGame  # Importa la clase de lógica del juego
from src.ui.draw import (  # Importa las funciones de dibujo
    draw_background_and_borders, draw_apple, draw_snake, draw_head_blink, draw_score, show_gameover_screen
)

# --- CONFIGURACIÓN Y ARRANQUE DEL JUEGO ---
WIDTH = 1920  # Ancho de la ventana
HEIGHT = 1080  # Alto de la ventana
TILE_SIZE = 10  # Tamaño de cada celda
BORDER_COLOR = (0, 0, 0)  # Color del borde
BORDER_THICKNESS = 2  # Grosor del borde
BG_COLOR = (34, 70, 34)  # Color de fondo
SNAKE_COLOR = (144, 238, 144)  # Color de la serpiente
APPLE_COLOR = (213, 50, 80)  # Color de la manzana
SCORE_COLOR = (255, 255, 255)  # Color del texto de puntuación
GAMEOVER_COLOR = (213, 50, 80)  # Color del texto de Game Over
FPS = 15  # Fotogramas por segundo

pygame.init()  # Inicializa pygame

# Crea la ventana principal
window = pygame.display.set_mode((WIDTH, HEIGHT))  # Crea la ventana del juego
pygame.display.set_caption("Juego de la Serpiente")  # Título de la ventana

# Crea las texturas para el fondo, la serpiente y la manzana
background_texture = pygame.Surface(
    (TILE_SIZE, TILE_SIZE))  # Superficie para el fondo
background_texture.fill(BG_COLOR)  # Rellena el fondo
# Superficie para la serpiente
snake_texture = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
snake_texture.fill(SNAKE_COLOR)  # Rellena la serpiente
# Superficie para la manzana
apple_texture = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
apple_texture.fill(APPLE_COLOR)  # Rellena la manzana

# Fuentes para la puntuación y mensajes
font = pygame.font.SysFont("consolas", 15)  # Fuente para la puntuación
font_msg = pygame.font.SysFont(
    "consolas", 15, bold=True)  # Fuente para mensajes

clock = pygame.time.Clock()  # Reloj para controlar FPS
game = SnakeGame(WIDTH, HEIGHT, TILE_SIZE)  # Instancia del juego

# Bucle principal del juego


def main():
    running = True  # Variable para controlar el bucle principal
    while running:
        for event in pygame.event.get():  # Procesa los eventos
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                running = False
            elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                # Permite jugar tanto con flechas como con WASD
                if event.key in (pygame.K_LEFT, pygame.K_a):  # Izquierda
                    game.queue_direction('IZQ')
                elif event.key in (pygame.K_RIGHT, pygame.K_d):  # Derecha
                    game.queue_direction('DER')
                elif event.key in (pygame.K_UP, pygame.K_w):  # Arriba
                    game.queue_direction('ARR')
                elif event.key in (pygame.K_DOWN, pygame.K_s):  # Abajo
                    game.queue_direction('ABA')
        if not game.game_over:  # Si el juego no ha terminado
            game.step()  # Avanza el estado del juego
            state = game.get_state()  # Obtiene el estado actual
            # Dibuja el fondo, la manzana y la serpiente
            draw_background_and_borders(
                window, WIDTH, HEIGHT, TILE_SIZE, background_texture, BORDER_COLOR, BORDER_THICKNESS)
            draw_apple(window, apple_texture,
                       state['food_x'], state['food_y'], TILE_SIZE)
            draw_snake(window, snake_texture, state['snake_body'])
            draw_score(window, state['snake_length'] - 1, font)
            pygame.display.update()  # Actualiza la pantalla
            # Si el juego termina, muestra el efecto de parpadeo y la pantalla de Game Over
            if state['game_over']:
                draw_head_blink(window, state['head'], state['snake_body'], state['food_x'], state['food_y'], TILE_SIZE, background_texture,
                                BORDER_COLOR, BORDER_THICKNESS, apple_texture, snake_texture, state['snake_length'] - 1, font, draw_score)
                pygame.display.update()  # Actualiza la pantalla
                pygame.time.wait(400)  # Espera 400 ms
                # Muestra pantalla de Game Over
                action = show_gameover_screen(window, WIDTH, HEIGHT, font, font_msg,
                                              state['snake_length'] - 1, draw_score, BG_COLOR, GAMEOVER_COLOR, SCORE_COLOR)
                if action == 'salir':  # Si elige salir
                    running = False
                elif action == 'continuar':  # Si elige continuar
                    game.reset()  # Reinicia el juego
        clock.tick(FPS)  # Controla la velocidad del juego
    pygame.quit()  # Sale de pygame


if __name__ == "__main__":
    main()  # Llama a la función principal
