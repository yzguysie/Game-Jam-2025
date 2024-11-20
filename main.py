import pygame
from pygame import gfxdraw
pygame.init()
import random
import math
import time
from graphics import Colors
from graphics import Camera
from graphics import Tile
from actor import Player
from actor import Actor




class Main:
    def run(self):
        self.width = 1280
        self.height = 720
        self.og_width = self.width
        self.og_height = self.height

        self.fps = 60
        self.fullscreen = False
        self.window = pygame.display.set_mode([self.width, self.height], pygame.RESIZABLE)
        pygame.display.set_caption("Placeholder")



        BACKGROUND_COLOR = (Colors.black)
        self.clock = pygame.time.Clock()

        self.delta_time = 1/self.fps

        self.playing = True

        self.player = Player()
        self.enemy = Actor()
        self.enemy.x = 0
        self.enemy.y = 0
        self.tiles: list[Tile] = []
        numtiles = 20
        tilescenterx = 0
        tilescentery = 0
        tilesize = 150
        for i in range(numtiles):
            x = (i*tilesize)-(tilesize*numtiles/2)
            for j in range(numtiles):
                y = (j*tilesize)-(tilesize*numtiles/2)
                self.tiles.append(Tile(x, y, tilesize, tilesize))



        self.camera = Camera(self.window, 1, -1, -1, actor=self.player)

        while self.playing:

            self.start = time.time()

            self.handle_events(pygame.event.get())

            self.game_tick(self.delta_time)

            self.game_draw(self.window, self.camera)

            pygame.display.flip()
            if self.fps > 0:
                #self.clock.tick(self.fps)
                pass
            self.delta_time = time.time()-self.start

        pygame.quit()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.playing = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    break

                if event.key == pygame.K_F11:
                    self.fullscreen = not self.fullscreen
                    self.window.set_fullsreen

        keys = pygame.key.get_pressed()



        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.xspeed += self.player.max_speed

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.xspeed -= self.player.max_speed
        
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.yspeed += self.player.max_speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.yspeed -= self.player.max_speed
                
    def game_draw(self, surface, camera):
        surface.fill((0, 0, 0))
        for tile in self.tiles:
            tile.draw(surface, camera)
        self.enemy.draw(surface, camera)
        self.player.draw(surface, camera)


    def game_tick(self, delta_time):
        self.player.tick(delta_time)


main = Main()
main.run()
