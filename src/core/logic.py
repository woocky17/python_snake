import random  # Importa la librería random para posiciones aleatorias

# Clase principal que gestiona la lógica del juego de la serpiente


class SnakeGame:
    def __init__(self, width, height, cell_size=10):
        # Inicializa el juego con el tamaño de pantalla y celda
        self.width = width  # Ancho del área de juego
        self.height = height  # Alto del área de juego
        self.cell_size = cell_size  # Tamaño de cada celda
        self.reset()  # Inicializa el estado del juego

    def reset(self):
        # Reinicia el estado del juego
        self.x = self.width // 2  # Posición inicial X de la serpiente
        self.y = self.height // 2  # Posición inicial Y de la serpiente
        self.dx = 0  # Desplazamiento X
        self.dy = 0  # Desplazamiento Y
        self.direction = None  # Dirección actual
        self.direction_queue = []  # Cola de direcciones
        self.snake_body = []  # Lista de segmentos de la serpiente
        self.snake_length = 1  # Longitud inicial
        self.food_x, self.food_y = self.random_food_position()  # Posición de la comida
        self.game_over = False  # Estado de fin de juego
        self.quit = False  # Estado de salida

    def random_food_position(self):
        # Genera una posición aleatoria para la comida
        x = round(random.randrange(0, self.width - self.cell_size) /
                  10.0) * 10.0  # X aleatoria
        y = round(random.randrange(0, self.height -
                  self.cell_size) / 10.0) * 10.0  # Y aleatoria
        return x, y  # Devuelve la posición

    def queue_direction(self, new_dir):
        # Añade una nueva dirección a la cola si es válida
        # Si la cola está vacía o la última no es igual
        if not self.direction_queue or self.direction_queue[-1] != new_dir:
            # Si no es la opuesta a la actual
            if self.direction != self.opposite_direction(new_dir):
                self.direction_queue.append(new_dir)  # Añade la dirección

    def opposite_direction(self, dir):
        # Devuelve la dirección opuesta
        return {'IZQ': 'DER', 'DER': 'IZQ', 'ARR': 'ABA', 'ABA': 'ARR'}.get(dir)

    def step(self):
        # Avanza un paso en el juego (mueve la serpiente y gestiona colisiones)
        if self.direction_queue:  # Si hay direcciones en la cola
            new_dir = self.direction_queue.pop(
                0)  # Toma la siguiente dirección
            # Si no es la opuesta
            if new_dir != self.opposite_direction(self.direction):
                self.direction = new_dir  # Cambia la dirección
                if new_dir == 'IZQ':  # Izquierda
                    self.dx = -self.cell_size
                    self.dy = 0
                elif new_dir == 'DER':  # Derecha
                    self.dx = self.cell_size
                    self.dy = 0
                elif new_dir == 'ARR':  # Arriba
                    self.dy = -self.cell_size
                    self.dx = 0
                elif new_dir == 'ABA':  # Abajo
                    self.dy = self.cell_size
                    self.dx = 0
        next_x = self.x + self.dx  # Calcula la siguiente posición X
        next_y = self.y + self.dy  # Calcula la siguiente posición Y
        # Colisión con el borde
        if next_x >= self.width or next_x < 0 or next_y >= self.height or next_y < 0:
            self.game_over = True  # Marca el juego como terminado
            return
        self.x = next_x  # Actualiza la posición X
        self.y = next_y  # Actualiza la posición Y
        head = [self.x, self.y]  # Nueva cabeza
        self.snake_body.append(head)  # Añade la cabeza al cuerpo
        if len(self.snake_body) > self.snake_length:  # Si el cuerpo es más largo que la longitud
            del self.snake_body[0]  # Elimina el segmento más antiguo
        # Colisión con uno mismo
        # Itera sobre el cuerpo menos la cabeza
        for segment in self.snake_body[:-1]:
            if segment == head:  # Si la cabeza toca el cuerpo
                self.game_over = True  # Termina el juego
                return
        # Colisión con la comida
        if self.x == self.food_x and self.y == self.food_y:  # Si la cabeza está en la comida
            self.food_x, self.food_y = self.random_food_position()  # Nueva comida
            self.snake_length += 1  # Aumenta la longitud

    def get_state(self):
        # Devuelve el estado actual del juego
        return {
            'snake_body': self.snake_body,  # Lista de segmentos
            'snake_length': self.snake_length,  # Longitud
            'food_x': self.food_x,  # X de la comida
            'food_y': self.food_y,  # Y de la comida
            'head': [self.x, self.y],  # Posición de la cabeza
            'game_over': self.game_over,  # Estado de fin de juego
            'quit': self.quit,  # Estado de salida
            'direction': self.direction,  # Dirección actual
        }

    def get_state(self):
        return {
            'snake_body': self.snake_body,
            'snake_length': self.snake_length,
            'food_x': self.food_x,
            'food_y': self.food_y,
            'head': [self.x, self.y],
            'game_over': self.game_over,
            'quit': self.quit,
            'direction': self.direction,
        }
