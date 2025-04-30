from graphics import Camera
from graphics import Colors
from graphics import Drawable
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, image = None, rotation: float = 0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if image:
            self.image = image
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill(Colors.purple)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, camera: Camera):
        self.rect.center = camera.get_pos(self.x, self.y)
        self.update()
        #FIXME: Using reference to uninitiated sprite i think so there will be nothing drawn? probably
        pygame.sprite.Sprite.draw(self, camera.surface)



    #def draw(self, camera: Camera):
    #    pygame.draw.rect(camera.surface, Colors.white, (camera.get_x(self.x), camera.get_y(self.y), self.width/camera.scale, self.height/camera.scale), width=int(5/camera.scale))


class Actor(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, width: int, height: int, image = None, rotation: float = 0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if image:
            self.image = image
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill(Colors.purple)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


        self.xspeed: float = 0
        self.yspeed: float = 0
        self.max_speed: int = 250
        self.acceleration: int = 1500 # Speed/sec (doesn't work bcause dt bruh, actually i think it does nvm)
        self.bounded: bool = True # Not used
        self.friction: int = 500 # momentum that is lost every second to friction

    def draw(self, camera: Camera):
        self.rect.center = camera.get_pos(self.x, self.y)
        self.update()
        super().draw(camera.surface)

    def tick(self, dt):

        vector = pygame.Vector2(self.xspeed, self.yspeed)
        if (vector.magnitude() > self.max_speed):
            vector = vector.normalize()
            self.xspeed = vector[0]*self.max_speed
            self.yspeed = vector[1]*self.max_speed


        #FIXME: dt makes this not work
        self.x += self.xspeed*dt
        self.y += self.yspeed*dt

            #self.xspeed -= (self.friction)*dt
            #self.yspeed -= (self.friction)*dt
        self.yspeed = 0
        self.xspeed = 0
    

class Player(Actor):
    def __init__(self, x: float, y: float, width: int, height: int, image: pygame.image = None, rotation: float = 0):
        super().__init__(x, y, width, height, image, rotation)


class Enemy(Actor):
    def __init__(self, x: float, y: float, width: int, height: int, image: pygame.image = None, rotation: float = 0):
        super().__init__(x, y, width, height, image, rotation)

