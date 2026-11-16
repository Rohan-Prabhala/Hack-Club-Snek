# https://www.pygame.org/docs/tut/ChimpLineByLine.html | the loading resources and game objects section

import pygame

from typing import Optional

import Helper

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, folder_name: Optional[str], image_name: Optional[str], width: float, height: float):
        super().__init__()

        if (folder_name is None) ^ (image_name is None):
            raise ValueError("Folder name and image name need to either BOTH be assigned or BOTH be None! You can't have an image without a folder and vice versa!")

        if not image_name is None and not folder_name is None:
            self.image = Helper.load_image(folder_name, image_name, width, height)
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((0, 0, 0))

        self.rect: pygame.FRect = self.image.get_frect()

    def set_position(self, position: pygame.math.Vector2):
        self.rect.center = (position.x, position.y)

    # def move(self, distance: pygame.math.Vector2):
    #     self.pos = self.pos.move(distance.x, distance.y)