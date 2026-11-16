# https://www.pygame.org/docs/tut/ChimpLineByLine.html | the loading resources and game objects section

import pygame

from typing import Optional

import Helper

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name: Optional[str], width: float, height: float):
        super().__init__()

        if not image_name == None:
            self.image = Helper.load_image(image_name, width, height)
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((0, 0, 0))

        self.rect: pygame.FRect = self.image.get_frect()

    def set_position(self, position: pygame.math.Vector2):
        self.rect.center = (position.x, position.y)

    def move(self, distance: pygame.math.Vector2):
        self.pos = self.pos.move(distance.x, distance.y)