import pygame

import os
import sys

def load_image(path: str, scale_factor: int):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (image.width*scale_factor, image.height*scale_factor))
    return image

# def resource_path(relative_path):
#     base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
#     return os.path.join(base_path, relative_path)

def get_path(*paths: str) -> str:
    return os.path.join(*paths)

def load_sound(name: str):
    pass