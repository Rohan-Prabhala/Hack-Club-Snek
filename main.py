# quick intro: https://www.youtube.com/watch?v=blLLtdv4tvo&t=108s
# repo example: https://github.com/PythonProgramming/pygame-tutorial-series
# primer: https://realpython.com/pygame-a-primer/
# camera: https://www.youtube.com/watch?v=u7LPRqrzry8
# + the docs and tutorials there

# game thats like snake but you have to gobble up enemies who actively try to either run or fight you + it has a bigger open world

# IM GONNA MAKE SURE MY GAME IS STRUCTURED PROPERLY OKAY?? I have some very minor java experience and unity experience so that should help fr

import pygame
import random

from InputHandler import InputHandler
from GameSprite import GameSprite
from Entity import Entity

from Player import Player

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Gobble Game")

player_hitbox = pygame.FRect()
player_hitbox.width, player_hitbox.height = 80, 80
player_hitbox.center = (100, 100)
player = Player(GameSprite("imgs/New Piskel-1.png.png", 100, 100), player_hitbox, pygame.Vector2(100, 100))

gs = GameSprite(None, 50, 50)

falling_object_hitbox = gs.rect.inflate(-10, -10)
falling_object_hitbox.center = (100, 100)
falling_object = Entity(
    gs,
    falling_object_hitbox,
    position = pygame.Vector2(random.randint(50, window.width-50), 0),
    initial_velocity = pygame.Vector2(0, 100)
)

debug = True

game_state = 1

running = True

clock = pygame.time.Clock()

delta_time = 0.1

font = pygame.font.SysFont("Arial", 36)

input = InputHandler()

entities = [
    player,
    falling_object
]

all_sprites = pygame.sprite.Group()

for e in entities:
    if e.sprite is not None:
        all_sprites.add(e.sprite)

while running:
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time)) # some weird tutorial told me to do this

    # take input
    input.update()

    player.update_input (input)

    if player.sprite is not None:
        hits = pygame.sprite.spritecollide(player.sprite, all_sprites, dokill=False)

        for e in hits:
            if isinstance(e, Entity) and not isinstance(e, Player):
                falling_object_y = 0
                falling_object_x = random.randint(0, window.width-50)

    if falling_object.current_velocity.y >= 600:
        player.current_velocity = pygame.Vector2(0, 0)
        player.position = pygame.Vector2(1000, 1000)

        falling_object.current_velocity = pygame.Vector2(0, 0)
        falling_object.position = pygame.Vector2(1000, 1000)

        game_state = 2

    # update entities

    window.fill((255, 255, 255))

    if game_state == 2:
        text_surface = font.render('GAME OVER', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(400,300))
        window.blit(text_surface, text_rect)

    if game_state == 1:
        for e in entities:
            e.update(delta_time)
    elif game_state == 2:
        pass

    # update visuals
    all_sprites.update()

    # render the stuff yk
    all_sprites.draw(window)

    if debug:
        for e in entities:
            e.draw_debug(window)

    pygame.display.flip()
