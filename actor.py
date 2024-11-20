from graphics import Camera
from graphics import Colors
import pygame

class Actor:
    def __init__(self, ):
        self.x: float = 0
        self.y: float = 0
        self.xspeed: float = 0
        self.yspeed: float = 0
        self.max_speed: int = 250
        self.acceleration: int = 1500 # Speed/sec (doesn't work bcause dt bruh, actually i think it does nvm)
        self.width: int = 100
        self.height: int = 100
        self.bounded: bool = True
        self.friction: int = 500 # momentum that is lost every second to friction
        self.flat_friction: int = 100 # Momentum lost per second (flat, not in relation to speed)
        self.min_speed: int = 20 # speed at which the actor will stop moving
        self.color: tuple[int, int, int] = Colors.purple

    def draw(self, surface, camera: Camera):
        pygame.draw.rect(surface, self.color, (camera.get_x(self.x), camera.get_y(self.y), self.width, self.height))

    def tick(self, dt):

        vector = pygame.Vector2(self.xspeed, self.yspeed)
        if (vector.magnitude() > self.max_speed):
            vector = vector.normalize()
            self.xspeed = vector[0]*self.max_speed
            self.yspeed = vector[1]*self.max_speed


        #FIXME: dt makes this not work
        if (self.xspeed**2+self.yspeed**2) > self.min_speed:                
            self.x += self.xspeed*dt
            self.y += self.yspeed*dt

            #self.xspeed -= (self.friction)*dt
            #self.yspeed -= (self.friction)*dt
        self.yspeed = 0
        self.xspeed = 0
    

class Player(Actor):
    def __init__(self):
        super().__init__()
        #self.camera = Camera()
        self.color: tuple[int, int, int] = Colors.green



class Enemy(Actor):
    pass

