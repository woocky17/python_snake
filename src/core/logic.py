# src/snakegame/core/logic.py

import random

TILE_SIZE = 10


class SnakeGame:
    def __init__(self, width, height, cell_size=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.reset()

    def reset(self):
        self.x = self.width // 2
        self.y = self.height // 2
        self.dx = 0
        self.dy = 0
        self.direction = None
        self.direction_queue = []
        self.snake_body = []
        self.snake_length = 1
        self.food_x, self.food_y = self.random_food_position()
        self.game_over = False
        self.quit = False

    def random_food_position(self):
        x = round(random.randrange(
            0, self.width - self.cell_size) / 10.0) * 10.0
        y = round(random.randrange(
            0, self.height - self.cell_size) / 10.0) * 10.0
        return x, y

    def queue_direction(self, new_dir):
        if not self.direction_queue or self.direction_queue[-1] != new_dir:
            if self.direction != self.opposite_direction(new_dir):
                self.direction_queue.append(new_dir)

    def opposite_direction(self, dir):
        return {'IZQ': 'DER', 'DER': 'IZQ', 'ARR': 'ABA', 'ABA': 'ARR'}.get(dir)

    def step(self):
        if self.direction_queue:
            new_dir = self.direction_queue.pop(0)
            if new_dir != self.opposite_direction(self.direction):
                self.direction = new_dir
                if new_dir == 'IZQ':
                    self.dx = -self.cell_size
                    self.dy = 0
                elif new_dir == 'DER':
                    self.dx = self.cell_size
                    self.dy = 0
                elif new_dir == 'ARR':
                    self.dy = -self.cell_size
                    self.dx = 0
                elif new_dir == 'ABA':
                    self.dy = self.cell_size
                    self.dx = 0
        next_x = self.x + self.dx
        next_y = self.y + self.dy
        # Border collision
        if next_x >= self.width or next_x < 0 or next_y >= self.height or next_y < 0:
            self.game_over = True
            return
        self.x = next_x
        self.y = next_y
        head = [self.x, self.y]
        self.snake_body.append(head)
        if len(self.snake_body) > self.snake_length:
            del self.snake_body[0]
        # Self collision
        for segment in self.snake_body[:-1]:
            if segment == head:
                self.game_over = True
                return
        # Food collision
        if self.x == self.food_x and self.y == self.food_y:
            self.food_x, self.food_y = self.random_food_position()
            self.snake_length += 1

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
