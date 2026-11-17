# https://www.pygame.org/docs/tut/ChimpLineByLine.html | the loading resources and game objects section

import pygame

from typing import Optional

import Helper

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, *paths: str, width: float, height: float, scale_factor: int = 1):
        super().__init__()

        if paths:
            self.image = Helper.load_image(Helper.get_path(*paths), scale_factor)
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((0, 0, 0))

        self.rect: pygame.FRect = self.image.get_frect()

    def set_position(self, position: pygame.math.Vector2):
        self.rect.center = (position.x, position.y)

    # def move(self, distance: pygame.math.Vector2):
    #     self.pos = self.pos.move(distance.x, distance.y)