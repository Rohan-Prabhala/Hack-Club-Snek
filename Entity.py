import pygame

from typing import Optional
from enum import Enum, auto

from GameSprite import GameSprite 

# when doing the slideshow, it told me to do folktale when first learning python so i did that
# my folktale project is when i learned how to use enums in python which is something i frequently like to use in unity game dev
class Collision_Type(Enum):
    GHOST = auto()
    BLOCKABLE = auto()
    PLAYER = auto()

# Typing is very confusing but im trynna make it so that the sprite HAS to be game sprite or the entity doesnt need to have a sprite
class Entity ():
    def __init__(self, sprite: Optional[GameSprite], hitbox: Optional[pygame.FRect], position: pygame.math.Vector2, initial_velocity: pygame.Vector2, collision_type: Collision_Type):
        if sprite is None and hitbox is None:
            raise ValueError("This entity needs to at least have a sprite or rect passed into it!")

        self.collision_type = collision_type
        self.sprite = sprite

        self.current_velocity = initial_velocity

        if hitbox is not None:
            self.hitbox = hitbox
        elif sprite is not None:
            self.hitbox = sprite.rect.copy()

        self.position = position
        self.update_sprite()

    def set_position(self, new_position: pygame.Vector2):
        self.position = new_position
        self.hitbox.center = self.position
        self.update_sprite()

    def update(self,  delta_time: float):
        self.set_position(self.position + self.current_velocity * delta_time)

    def update_sprite(self):
        if self.sprite is not None:
            self.sprite.set_position(self.position)

    def on_collision_with(self, other: Entity):
        self.on_collision()
        other.on_collision()

    def on_collision(self):
        pass

    # to draw the hitbox and the visual thingy of the surface
    def draw_debug(self, window: pygame.Surface):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)

        if self.sprite is not None:
            pygame.draw.rect(window, (255, 255, 0), self.sprite.rect, 1)

    

