# https://www.youtube.com/watch?v=u7LPRqrzry8

from typing import Any, Iterable

import pygame

import Helper

class CameraGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)

        # camera offset
        self.offset = pygame.math.Vector2(0, 0)

        # ground
        # self.ground_surface = Helper.load_image("", "", 2, 2)
        # self.ground_rect = self.ground_surface.get_rect(topleft = (0, 0))

    def custom_draw(self, screen):
        #  ground
        # ground_offset = self.ground_rect.topleft + self.offset
        # screen.blit(self.ground_surface, self.ground_rect)

        #  active elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft + self.offset
            screen.blit(sprite.image, offset_pos)