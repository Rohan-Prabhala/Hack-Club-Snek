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

        # box setup - DOESNT WORK
        # self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        # l = self.camera_borders['left']
        # t = self.camera_borders['top']
        # w = self.screen.get_size()[0] - (l + self.camera_borders['right'])
        # h = self.screen.get_size()[1] - (t + self.camera_borders['bottom'])
        # self.camera_rect = pygame.Rect(l,t,w,h)

        # ground
        self.ground_surface = Helper.load_image("imgs", "background_TEST.png", 0, 0)
        self.ground_rect = self.ground_surface.get_rect(center = (320, 180))

    def custom_draw(self, offset: pygame.Vector2, player: Player, draw_debug: bool):
        # box camera doesnt work!

        # assert player.sprite is not None

        # if self.camera_rect.left < player.sprite.rect.left:
        #     self.camera_rect.left = player.sprite.rect.left

        # self.offset.x = self.camera_rect.left = self.camera_borders['left']
        # self.offset.y = self.camera_rect.top - self.camera_borders['top']

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
        # if draw_debug:
        #     pygame.draw.rect(self.screen, 'yellow', self.camera_rect, 5)