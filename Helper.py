import pygame

import os

def load_image(folder_name: str, image_name: str, width: float, height: float):
    image = pygame.image.load(os.path.join(folder_name, image_name)).convert_alpha()
    # image = pygame.transform.scale(image, (width, height))
    return image

def load_sound(name: str):
    pass