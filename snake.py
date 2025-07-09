import pygame
import time
import random

# Inicialización de pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la pantalla
ancho = 600
alto = 400

# Configurar la ventana
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Serpiente")

# Configuración de la serpiente
tamanio_celda = 10
velocidad = 15

clock = pygame.time.Clock()

# Fuente para mostrar la puntuación
fuente = pygame.font.SysFont("bahnschrift", 25)


def mostrar_puntuacion(puntuacion):
    texto = fuente.render("Puntuación: " + str(puntuacion), True, blanco)
    ventana.blit(texto, [10, 10])


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
            ventana.fill(negro)
            mensaje = fuente.render(
                "¡Perdiste! Presiona C para continuar o Q para salir", True, rojo)
            ventana.blit(mensaje, [ancho / 6, alto / 3])
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

        ventana.fill(negro)
        pygame.draw.rect(ventana, verde, [
                         comida_x, comida_y, tamanio_celda, tamanio_celda])

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
            pygame.draw.rect(
                ventana, azul, [segmento[0], segmento[1], tamanio_celda, tamanio_celda])

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
