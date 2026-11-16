# quick intro: https://www.youtube.com/watch?v=blLLtdv4tvo&t=108s
# repo example: https://github.com/PythonProgramming/pygame-tutorial-series
# primer: https://realpython.com/pygame-a-primer/
# camera: https://www.youtube.com/watch?v=u7LPRqrzry8
# + the docs and tutorials there

# game thats like snake but you have to gobble up enemies who actively try to either run or fight you + it has a bigger open world

# IM GONNA MAKE SURE MY GAME IS STRUCTURED PROPERLY OKAY?? I have some very minor java experience and unity experience so that should help fr

import pygame
import random
import math

from InputHandler import InputHandler
from GameSprite import GameSprite
from Entity import Entity, Collision_Type

from Player import Player

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Gobble Game")

player_hitbox = pygame.FRect()
player_hitbox.width, player_hitbox.height = 80, 80
player_hitbox.center = (100, 100)
player = Player(GameSprite("imgs/New Piskel-1.png.png", 100, 100), player_hitbox, pygame.Vector2(100, 100))

assert player.sprite is not None

gs = GameSprite(None, 50, 50)

falling_object_hitbox = gs.rect.inflate(-10, -10)
falling_object_hitbox.center = (100, 100)
falling_object = Entity(
    gs,
    falling_object_hitbox,
    position = pygame.Vector2(random.randint(math.ceil(gs.rect.width), math.ceil(window.width-gs.rect.width)), 0),
    initial_velocity = pygame.Vector2(0, 100),
    collision_type=Collision_Type.GHOST
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

blockable_sprites = pygame.sprite.Group()
ghost_sprites = pygame.sprite.Group() # i made this name up - its just for sprites that the player can pass through

all_sprites = pygame.sprite.Group(blockable_sprites, ghost_sprites, player.sprite)

for e in entities:
    if e.sprite is None or isinstance(e, Player):
        continue
    if e.collision_type == Collision_Type.GHOST:   
        ghost_sprites.add(e.sprite)
    elif e.collision_type == Collision_Type.BLOCKABLE:
        blockable_sprites.add(e.sprite)

while running:
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time)) # some weird tutorial told me to do this

    input.update()
    player.update_input(input)

    if game_state == 1:
        for e in entities:
            e.update(delta_time)
    elif game_state == 2:
        pass

    ghost_hits = pygame.sprite.spritecollide(player.sprite, ghost_sprites, dokill=False)
    blockable_hits = pygame.sprite.spritecollide(player.sprite, blockable_sprites, dokill=False)

    for e in ghost_hits:
        if e.
        falling_object.set_position(pygame.Vector2(random.randint(math.ceil(gs.rect.width), math.ceil(window.width-gs.rect.width)), 0))

    if falling_object.current_velocity.y >= 600:
        player.current_velocity = pygame.Vector2(0, 0)
        player.set_position(pygame.Vector2(1000, 1000))

        falling_object.current_velocity = pygame.Vector2(0, 0)
        falling_object.set_position(pygame.Vector2(1000, 1000))

        game_state = 2

    window.fill((255, 255, 255))

    if game_state == 2:
        text_surface = font.render('GAME OVER', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(400,300))
        window.blit(text_surface, text_rect)

    # update visuals
    all_sprites.update()

    # render the stuff yk
    all_sprites.draw(window)

    if debug:
        for e in entities:
            e.draw_debug(window)

    pygame.display.flip()
