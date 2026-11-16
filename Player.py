import pygame

from typing import Optional

from InputHandler import InputHandler

from GameSprite import GameSprite 
from Entity import Entity, Collision_Type

class Player(Entity):
    def __init__(self, sprite: GameSprite | None, hitbox: pygame.FRect | None, position: pygame.math.Vector2):
        super().__init__(sprite, hitbox, position, pygame.Vector2(0.0, 0.0), Collision_Type.PLAYER)

        self.walk_speed = 192
        self.run_speed = 288
        self.input_vector_normalized = pygame.math.Vector2(0.0, 0.0)

    def update_input(self, input_handler: InputHandler):
        self.input_vector_normalized = input_handler.input_vector_normalized
        if input_handler.shift_pressed:
            self.current_velocity = self.input_vector_normalized * self.run_speed
        else:
            self.current_velocity = self.input_vector_normalized * self.walk_speed

    def update(self, delta_time):
        super().update(delta_time)

    def on_collision_with(self, other: Entity):
        super().on_collision_with(other)

    def on_collision(self):
        return super().on_collision()