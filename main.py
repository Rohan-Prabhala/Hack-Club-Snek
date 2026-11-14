# quick intro: https://www.youtube.com/watch?v=blLLtdv4tvo&t=108s
# repo example: https://github.com/PythonProgramming/pygame-tutorial-series
# primer: https://realpython.com/pygame-a-primer/
# random beginners guide: https://www.youtube.com/watch?v=_BIAu6396-A&t=229s

import pygame
import random

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("wasd")

player = pygame.surface.Surface((300, 300))
player.fill((255, 255, 255))
player = pygame.image.load("imgs/New Piskel-1.png.png").convert_alpha()
player = pygame.transform.scale(player, (300, 300))

player_x = 0
player_y = 0

player_vel_x = 0
player_vel_y = 0

falling_object = pygame.surface.Surface((50, 50))
falling_object.fill((0, 0, 0))

falling_object_x = 0
falling_object_y = 0

falling_object_vel_x = 0
falling_object_vel_y = 100

def collision_detection():
    return (player_x <= (falling_object_x + int (falling_object.width)) and
            (player_x + player.width) >= falling_object_x and
            player_y <= (falling_object_y + falling_object.height + 5) and
            (player_y + player.height) >= falling_object_y
    )

game_state = 1

running = True

clock = pygame.time.Clock()

delta_time = 0.1

font = pygame.font.SysFont("Arial", 36)

while running:
    # take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -200
            if event.key == pygame.K_RIGHT:
                player_vel_x = 200
        else:
            player_vel_x = 0
            player_vel_y = 0

    if collision_detection():
        falling_object_y = 0
        falling_object_x = random.randint(0, window.width-50)

    if falling_object_y >= 600:
        player_x, player_y = 1000, 1000
        player_vel_x, player_vel_y = 0, 0

        falling_object_x, falling_object_y = 1000, 1000
        falling_object_vel_x, falling_object_vel_y = 0,0

        game_state = 2

    # output
    window.fill((255, 255, 255))

    if game_state == 2:
        text_surface = font.render('GAME OVER', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(400,300))
        window.blit(text_surface, text_rect)

    if game_state == 1:
        player_x += player_vel_x * delta_time
        player_vel_y += player_vel_y * delta_time
        window.blit(player, (player_x, player_y))

        falling_object_x += falling_object_vel_x * delta_time
        falling_object_y += falling_object_vel_y * delta_time
        window.blit(falling_object, (falling_object_x, falling_object_y))

    elif game_state == 2:
        pass

    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
