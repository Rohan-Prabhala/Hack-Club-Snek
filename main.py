# quick intro: https://www.youtube.com/watch?v=blLLtdv4tvo&t=108s
# repo example: https://github.com/PythonProgramming/pygame-tutorial-series
# primer: https://realpython.com/pygame-a-primer/
# camera: https://www.youtube.com/watch?v=u7LPRqrzry8
# what i can do later: https://youtu.be/8OMghdHP-zs?t=18262
# https://www.youtube.com/watch?v=MYaxPa_eZS0
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# + the docs and tutorials there

# i didnt use some of these lmao

# game thats like snake but you have to gobble up enemies who actively try to either run or fight you + it has a bigger open world

# IM GONNA MAKE SURE MY GAME IS STRUCTURED PROPERLY OKAY?? I have some very minor java experience and unity experience so that should help fr

# IDK WHAT THIS MEANS BUT IM GONNA MAKE EVERYTHING 32 x 32 pixels NO clue how this will work for the background but yk... whatever

import os
import sys

import pygame

import random
import math

import Helper

from CameraGroup import CameraGroup

from InputHandler import InputHandler

from GameSprite import GameSprite
from Entity import Entity, Collision_Type

from Player import Player

PIXEL_UNIT_SIZE = 32

tree_counts = {
    "Trees-1.png": 10,
    "Trees-2.png": 15,
    "Trees-3.png": 5,
}

# Rumors of a Dungeon by human gazpacho is licensed under a Attribution 4.0 International License from Free Music Archive

if getattr(sys, "frozen", False):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Snake Gobble Game")
window = pygame.display.set_mode((640, 360), pygame.SCALED) # AI helped me for this weird line because wtf even is a bit operator and or and xor is all ik (actually this is in unity too with collider restraints)
# pygame.display.set_icon()
assert window is not None

pygame.mixer.music.load(Helper.get_path("music", "human gazpacho - Rumors of a Dungeon.mp3"))
pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)

background_color_map = Helper.load_image(Helper.get_path("imgs", "background", "Background_color_map.png"), 2)
blockable_mask = pygame.mask.from_threshold(background_color_map, pygame.Color(255, 0, 0), pygame.Color(15, 15, 15, 255))

map_center = pygame.Vector2(
    background_color_map.get_width() / 2,
    background_color_map.get_height() / 2
)

player = Player(
    blockable_mask,
    GameSprite("imgs", "sprites", "player", "bad_character_design.png", width=10, height=PIXEL_UNIT_SIZE, scale_factor=2),
    pygame.FRect(100, 100, PIXEL_UNIT_SIZE-2, PIXEL_UNIT_SIZE*2-2),
    # pygame.Vector2(100, 100)
    map_center
)

assert player.sprite is not None

gs = GameSprite(width=PIXEL_UNIT_SIZE, height=PIXEL_UNIT_SIZE)
falling_object_hitbox = gs.rect.inflate(-2, -2)
falling_object_hitbox.center = (100, 100)

falling_object = Entity(
    blockable_mask,
    gs,
    falling_object_hitbox,
    position = pygame.Vector2(random.randint(math.ceil(gs.rect.width), math.ceil(window.width-gs.rect.width)), PIXEL_UNIT_SIZE),
    initial_velocity = pygame.Vector2(0,0),
    collision_type=Collision_Type.GHOST
)

gs2 = GameSprite(width=PIXEL_UNIT_SIZE, height=PIXEL_UNIT_SIZE)
hb = gs2.rect.inflate(-10, -10)
hb.center = (100, 100)

obj = Entity(
    blockable_mask,
    gs2,
    hb,
    position = pygame.Vector2(200, 50),
    initial_velocity = pygame.Vector2(0, 0),
    collision_type=Collision_Type.GHOST
)

debug = True

running = True
game_state = 1

clock = pygame.time.Clock()
delta_time = 0.1

font = pygame.font.SysFont("Arial", 36)

input = InputHandler(window)

entities = [
    player,
    falling_object,
    obj
]

blockable_sprites = pygame.sprite.Group()
ghost_sprites = pygame.sprite.Group() # i made this name up - its just for sprites that the player can pass through

for e in entities:
    if e.sprite is None or isinstance(e, Player):
        continue
    if e.collision_type == Collision_Type.GHOST:   
        ghost_sprites.add(e.sprite)
    elif e.collision_type == Collision_Type.BLOCKABLE:
        blockable_sprites.add(e.sprite)

camera_group = CameraGroup(
    *blockable_sprites.sprites(),
    *ghost_sprites.sprites(),
    player.sprite,
    screen=window
)

for image_name, count in tree_counts.items():
    for _ in range(count):
        tree_sprite = GameSprite(Helper.get_path("imgs", "sprites", "trees", image_name), width=PIXEL_UNIT_SIZE, height=PIXEL_UNIT_SIZE*2, scale_factor=2)
        tree_hitbox = pygame.FRect(0, 0, 20, 30)

        hitbox_shift = pygame.Vector2(0, (tree_sprite.rect.height - tree_hitbox.height)/2)

        tree_mask = pygame.mask.Mask((int(tree_hitbox.width), int(tree_hitbox.height)), fill=True)

        for _ in range(50):
            spawn_pos = pygame.Vector2(
                random.randint(PIXEL_UNIT_SIZE, int(map_center.x*2) - PIXEL_UNIT_SIZE),
                random.randint(PIXEL_UNIT_SIZE*2, int(map_center.y*2) - PIXEL_UNIT_SIZE*2)
            )
            tree_hitbox.center = spawn_pos

            point = (int(tree_hitbox.left), int(tree_hitbox.top))
            invalid_spawn = blockable_mask.overlap(tree_mask, point) is not None

            hits_entity = any(tree_hitbox.colliderect(e.hitbox) for e in entities)

            if not invalid_spawn and not hits_entity:
                tree = Entity(blockable_mask, tree_sprite, tree_hitbox, spawn_pos, pygame.Vector2(0, 0), Collision_Type.BLOCKABLE, hitbox_offset=hitbox_shift)
                entities.append(tree)
                camera_group.add(tree_sprite)
                break

half_w = window.get_size()[0] / 2 
half_h = window.get_size()[1] / 2

while running:
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time)) # some weird tutorial told me to do this

    running = input.update()

    player.update_input(input)

    if game_state == 1:
        for e in entities:
            e.update(delta_time)
    elif game_state == 2:
        pass

    ghost_hits = pygame.sprite.spritecollide(player.sprite, ghost_sprites, dokill=False)
    blockable_hits = pygame.sprite.spritecollide(player.sprite, blockable_sprites, dokill=False)

    for e in ghost_hits:
        if e == falling_object.sprite:
            falling_object.set_position(pygame.Vector2(random.randint(math.ceil(gs.rect.width), math.ceil(window.width-gs.rect.width)), 0))

    if falling_object.position.y >= 600:
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


    player_offset = pygame.Vector2(0, 0)    
    player_offset.x = round(player.position.x - half_w)
    player_offset.y = round(player.position.y - half_h)

    # update visuals
    camera_group.update()

    # render the stuff yk
    camera_group.custom_draw(player_offset, player, debug)

    if debug:
        for e in entities:
            e.draw_debug(window, player_offset)

    pygame.display.flip()

pygame.quit()