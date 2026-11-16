import pygame

from typing import Optional

from InputHandler import InputHandler

from GameSprite import GameSprite 
from Entity import Entity

class Player(Entity):
    def __init__(self, sprite: GameSprite | None, hitbox: pygame.FRect | None, position: pygame.math.Vector2):
        super().__init__(sprite, hitbox, position, pygame.Vector2(0.0, 0.0))

        self.walk_speed = 200
        self.run_speed = 300
        self.input_vector_normalized = pygame.math.Vector2(0.0, 0.0)

    def update_input(self, input_handler: InputHandler):
        self.input_vector_normalized = input_handler.input_vector_normalized
        if input_handler.shift_pressed:
            self.current_velocity = self.input_vector_normalized * self.run_speed
        else:
            self.current_velocity = self.input_vector_normalized * self.walk_speed

    def update(self, delta_time):
        super().update(delta_time)