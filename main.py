import pygame
from pygame import gfxdraw
pygame.init()
import random
import math
import time

class Colors:
    white = (255, 255, 255)
    light_gray = (192, 192, 192)
    gray = (128, 128, 128)
    dark_gray = (64, 64, 64)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)


class Main:
    def run(self):
        self.width = 1280
        self.height = 720
        self.fps = 60

        self.window = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption("Placeholder")



        BACKGROUND_COLOR = (Colors.black)
        self.clock = pygame.time.Clock()

        self.delta_time = 1/self.fps

        self.playing = True
        while self.playing:
            self.start = time.time()

            self.handle_events(pygame.event.get())

            self.game_tick(self.delta_time)

            self.game_draw(self.window)

            pygame.display.flip()
            if self.fps > 0:
                self.clock.tick(self.fps)
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

    def game_draw(self, surface):
        surface.fill((0, 0, 0))

    def game_tick(self, delta_time):
        pass


main = Main()
main.run()
