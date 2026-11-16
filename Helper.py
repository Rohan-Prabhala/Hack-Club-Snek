import pygame

def load_image(name: str, width: float, height: float):
    image = pygame.image.load(name).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image

def load_sound(name: str):
    pass