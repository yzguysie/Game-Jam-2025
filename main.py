import pygame
from pygame import gfxdraw
pygame.init()
import random
import math
import time
from graphics import Colors
from graphics import Camera
from actor import Tile
from actor import Player
from actor import Actor
import cProfile


def main() -> None:
    start = time.time()
    last_time = start
    width = 1280
    height = 720
    og_width = width
    og_height = height
    fps_ = 60
    fps = 60
    frames = 0
    font = 'arial'
    font_width = 10
    font = pygame.font.SysFont(font, font_width)
    fullscreen = False
    window = pygame.display.set_mode([width, height], pygame.RESIZABLE)
    pygame.display.set_caption("Placeholder")



    BACKGROUND_COLOR = (Colors.black)
    clock = pygame.time.Clock()

    delta_time = 1/fps

    playing = True

    player_default_image = pygame.image.load("resources/images/placeholder.png")
    player = Player(0, 0, 100, 100, image=player_default_image)
    enemy = Actor(0, 0, 100, 100, image=player_default_image)
    tiles: list[Tile] = []
    numtiles = 20
    tilescenterx = 0
    tilescentery = 0
    tilesize = 150
    for i in range(numtiles):
        x = (i*tilesize)-(tilesize*numtiles/2)
        for j in range(numtiles):
            y = (j*tilesize)-(tilesize*numtiles/2)
            tiles.append(Tile(x, y, tilesize, tilesize))



    camera = Camera(window, 1, -1, -1, actor=player)
    while playing:
        delta_time = time.time()-start
        start = time.time()

        #handle_events(pygame.event.get())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    break

                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    else:
                        window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.yspeed -= player.max_speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.yspeed += player.max_speed

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.xspeed -= player.max_speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.xspeed += player.max_speed

        if keys[pygame.K_g]:
            camera.scale += .01
        
        if keys[pygame.K_h]:
            camera.scale -= .01
        


        #game_tick(delta_time)
        player.tick(delta_time)

        #game_draw(window, camera)

        window.fill((0, 0, 0))
        for tile in tiles:
            tile.draw(camera)
        enemy.draw(camera)
        player.draw(camera)

        text = font.render(f"Fps: {fps_}", True, Colors.green)
        window.blit(text, (0, 0))


        pygame.display.flip()
        if fps > 0:
            clock.tick(fps)
            pass
        delta_time = time.time()-start
        if frames % int(fps/2) == 0:
            fps_ = round(int(fps/2)/(time.time()-last_time))
            last_time = time.time()
        frames += 1

    pygame.quit()

def handle_events(self, events) -> None:
    pass
                
def game_draw(self, surface, camera) -> None:
    pass


def game_tick(self, delta_time) -> None:
    pass

#cProfile.run('main()', sort='cumtime')

main()
