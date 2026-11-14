# https://www.pygame.org/docs/tut/ChimpLineByLine.html | the loading resources and game objects section

import pygame

class GameObject(pygame.sprite.Sprite):

    def load_image(self, name, width, height):
        image = pygame.image.load(name).convert_alpha()
        image = pygame.transform.scale(image, width, height)
        return image

    def __init__(self, image_name, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(image_name, width, height)
        self.pos = self.image.get_rect().move(0, height)

    # def move(self):
    #     self.pos = self.pos.move(self.speed, 0)
    #     if self.pos.right > 600:
    #         self.pos.left = 0