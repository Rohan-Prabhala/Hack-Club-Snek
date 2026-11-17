import pygame

import os

def load_image(path: str, scale_factor: int):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (image.width*scale_factor, image.height*scale_factor))
    return image

def get_path(*paths: str) -> str:
    return os.path.join(*paths)

def load_sound(name: str):
    pass