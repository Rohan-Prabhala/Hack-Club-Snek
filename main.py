import pygame

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
falling_object.fill((255, 255, 255))

falling_object_x = 0
falling_object_y = 0

falling_object_vel_x = 0
falling_object_vel_y = 0.3

while True:
    # take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.2
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.2
        else:
            player_vel_x = 0

    # output
    window.fill((255, 255, 255))
    window.blit(player, (player_x, player_y))
    window.blit(falling_object, (falling_object_x, falling_object_y))

    pygame.display.flip()