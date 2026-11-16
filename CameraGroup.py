# https://www.youtube.com/watch?v=u7LPRqrzry8

from typing import Any, Iterable

import pygame

import Helper

from Player import Player

class CameraGroup(pygame.sprite.Group):
    def __init__(self, *sprites, screen: pygame.Surface):
        super().__init__(*sprites)
        
        self.screen = screen
        # camera offset
        self.offset = pygame.math.Vector2(0, 0)

        # ground
        self.ground_surface = Helper.load_image("imgs", "background_TEST.png", 0, 0)
        self.ground_rect = self.ground_surface.get_rect(center = (320, 180))

    def custom_draw(self, offset: pygame.Vector2):
        self.offset = offset

        #  ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.screen.blit(self.ground_surface, (round(ground_offset.x), round(ground_offset.y)))

        #  active elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            new_pos = sprite.rect.topleft
            # if not sprite == Player:
            new_pos -= self.offset
            self.screen.blit(sprite.image, (round(new_pos.x), round(new_pos.y)))