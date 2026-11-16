import pygame

from typing import Optional

from GameSprite import GameSprite 

# Typing is very confusing but im trynna make it so that the sprite HAS to be game sprite or the entity doesnt need to have a sprite
class Entity ():
    def __init__(self, sprite: Optional[GameSprite], hitbox: Optional[pygame.FRect], position: pygame.math.Vector2, initial_velocity: pygame.Vector2):
        if sprite is None and hitbox is None:
            raise ValueError("This entity needs to at least have a sprite or rect passed into it!")
        
        self.sprite = sprite

        self.current_velocity = initial_velocity

        if hitbox is not None:
            self.hitbox = hitbox
        elif sprite is not None:
            self.hitbox = sprite.rect.copy()

        self.position = position
        self.update_sprite()

    def update(self,  delta_time: float):
        self.position += self.current_velocity * delta_time
        self.update_sprite()

    def update_sprite(self):
        if self.sprite is not None:
            self.sprite.set_position(self.position)
            self.hitbox.center = self.position

    # to draw the hitbox and the visual thingy of the surface
    def draw_debug(self, window: pygame.Surface):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 3)

        if self.sprite is not None:
            pygame.draw.rect(window, (255, 255, 0), self.sprite.rect, 3)

    

