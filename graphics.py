import pygame
from dataclasses import dataclass

class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (128, 128, 128)
    light_gray = (192, 192, 192)
    dark_gray = (64, 64, 64)
    red = (255, 0, 0)
    blue = (85, 171, 255)
    bg_blue = (64, 84, 128)
    green = (85, 255, 171)
    purple = (255, 64, 255)
    yellow = (255,255,0)
    blue_black = (6, 8, 32)
    light_blue_black = (24, 32, 64)


class Sprite:
    def __init__(self, image, x: int, y: int, rotation: float):
        self.x = x
        self.y = y
        self.ogimage = image
        self.rotation = rotation
        self.last_rotation = rotation
        self.target_rotation = rotation
        self.image = pygame.transform.rotate(self.ogimage, self.rotation)
        self.centered: bool = False

    def draw(self, window):
        if self.rotation != self.last_rotation:
            self.image = pygame.transform.rotate(self.ogimage, self.rotation)
            self.last_rotation = self.rotation
        if self.centered:
            window.blit(self.image, (self.x-self.image.get_width()/2, self.y-self.image.get_height()/2))
        else:
            x_offset = (self.image.get_width()-self.ogimage.get_width())/2
            y_offset = (self.image.get_height()-self.ogimage.get_height())/2
            window.blit(self.image, (self.x-x_offset, self.y-y_offset))

    def set_centered(self, centered):
        self.centered = centered


class Camera:
    def __init__(self, surface, scale, x, y, actor = None):
        self.surface = surface
        self.scale = scale
        self.x = x
        self.y = y
        self.actor = actor

    def get_pos(self, x, y):
        return self.get_x(x), self.get_y(y)
    
    def get_x(self, x):
        if self.actor:
            return (x-self.actor.x-self.actor.width/2)*self.scale+self.surface.get_width()/2
        return (x-self.x)*self.scale+self.surface.get_width()/2
    
    def get_y(self, y):
        if self.actor:
            return (y-self.actor.y-self.actor.height/2)*self.scale+self.surface.get_height()/2
        return (y-self.y)*self.scale+self.surface.get_height()/2




class Drawable:
    def __init__(self, x: int, y: int, width: int, height: int, rotation: float) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation
        self.sprite = None
        self.image = None

    def make_sprite(self, image, camera, centered=False):
        self.image = pygame.transform.smoothscale(image, (round(self.width/camera.scale), round(self.height*camera.scale)))
        self.sprite = Sprite(img, self.x*self.camera.scale, self.y*self.camera.scale, self.rotation)
        self.sprite.set_centered(centered)

    def update_sprite(self):
        self.sprite.x, self.sprite.y = self.camera.get_camera_pos(self.x, self.y)
        self.sprite.width = self.width*self.camera.scale
        self.sprite.height = self.height*self.camera.scale
        self.sprite.rotation = self.rotation

    def draw(self, window, camera):
        self.update_sprite(camera)
        self.sprite.draw(window)

class Tile(Drawable):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height, 0)


    def draw(self, window, camera: Camera):
        pygame.draw.rect(window, Colors.white, (camera.get_x(self.x), camera.get_y(self.y), self.width/camera.scale, self.height/camera.scale), width=int(5/camera.scale))