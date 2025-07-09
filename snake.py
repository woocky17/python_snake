import pygame
import random
import os

# Inicialización de pygame
pygame.init()


# Definir colores
blanco = (255, 255, 255)
fondo = (34, 70, 34)  # Verde oscuro
rojo = (213, 50, 80)
verde_claro = (144, 238, 144)  # Verde claro para la serpiente
azul = (50, 153, 213)

# Tamaño de celda para texturas
TILE_SIZE = 10


# Dimensiones de la pantalla
ancho = 600
alto = 400

# Configurar la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Serpiente")

# Crear "texturas" de colores planos
background_texture = pygame.Surface((TILE_SIZE, TILE_SIZE))
background_texture.fill(fondo)

snake_texture = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
snake_texture.fill(verde_claro)


# Escalar la manzana para que ocupe más que una celda (por ejemplo, 1.5x)
APPLE_SIZE = int(TILE_SIZE * 1.5)
apple_texture = pygame.image.load("assets/apple.png").convert_alpha()
apple_texture = pygame.transform.scale(apple_texture, (APPLE_SIZE, APPLE_SIZE))

# Configuración de la serpiente
tamanio_celda = 10
velocidad = 15

clock = pygame.time.Clock()


# Fuente para mostrar la puntuación y mensajes
fuente = pygame.font.SysFont("consolas", 15)
fuente_mensaje = pygame.font.SysFont("consolas", 15, bold=True)


def mostrar_puntuacion(puntuacion):
    texto = fuente.render("Puntuación: " + str(puntuacion), True, blanco)
    # Mostrar la puntuación en la esquina inferior izquierda, dejando margen
    texto_rect = texto.get_rect()
    texto_rect.topleft = (10, alto - texto_rect.height - 10)
    ventana.blit(texto, texto_rect)


def juego():
    juego_terminado = False
    juego_cerrado = False

    x = ancho / 2
    y = alto / 2

    dx = 0
    dy = 0
    direccion = None  # Puede ser 'IZQ', 'DER', 'ARR', 'ABA'

    cuerpo_serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho - tamanio_celda) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamanio_celda) / 10.0) * 10.0

    while not juego_terminado:
        while juego_cerrado:
            ventana.fill(fondo)
            mensaje = fuente_mensaje.render(
                "¡Perdiste! Presiona C para continuar o Q para salir", True, rojo)
            # Centrar el mensaje horizontalmente
            mensaje_rect = mensaje.get_rect(center=(ancho // 2, alto // 3))
            ventana.blit(mensaje, mensaje_rect)
            mostrar_puntuacion(longitud_serpiente - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        juego_terminado = True
                        juego_cerrado = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego_terminado = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direccion != 'DER':
                        dx = -tamanio_celda
                        dy = 0
                        direccion = 'IZQ'
                elif event.key == pygame.K_RIGHT:
                    if direccion != 'IZQ':
                        dx = tamanio_celda
                        dy = 0
                        direccion = 'DER'
                elif event.key == pygame.K_UP:
                    if direccion != 'ABA':
                        dy = -tamanio_celda
                        dx = 0
                        direccion = 'ARR'
                elif event.key == pygame.K_DOWN:
                    if direccion != 'ARR':
                        dy = tamanio_celda
                        dx = 0
                        direccion = 'ABA'

        if x >= ancho or x < 0 or y >= alto or y < 0:
            juego_cerrado = True

        x += dx
        y += dy

        # Dibujar fondo con "textura"
        for i in range(0, ancho, TILE_SIZE):
            for j in range(0, alto, TILE_SIZE):
                ventana.blit(background_texture, (i, j))

        # Dibujar la manzana con textura, centrada en la celda
        apple_rect = apple_texture.get_rect(
            center=(comida_x + TILE_SIZE // 2, comida_y + TILE_SIZE // 2))
        ventana.blit(apple_texture, apple_rect.topleft)

        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        cuerpo_serpiente.append(cabeza)

        if len(cuerpo_serpiente) > longitud_serpiente:
            del cuerpo_serpiente[0]

        for segmento in cuerpo_serpiente[:-1]:
            if segmento == cabeza:
                juego_cerrado = True

        for segmento in cuerpo_serpiente:
            ventana.blit(snake_texture, (segmento[0], segmento[1]))

        mostrar_puntuacion(longitud_serpiente - 1)
        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(
                0, ancho - tamanio_celda) / 10.0) * 10.0
            comida_y = round(random.randrange(
                0, alto - tamanio_celda) / 10.0) * 10.0
            longitud_serpiente += 1

        clock.tick(velocidad)

    pygame.quit()
    quit()


juego()
