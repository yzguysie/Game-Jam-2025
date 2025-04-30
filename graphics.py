import pygame
from dataclasses import dataclass


class Colors:
    white: tuple[int, int, int] = (255, 255, 255)
    black: tuple[int, int, int] = (0, 0, 0)
    gray: tuple[int, int, int] = (128, 128, 128)
    light_gray: tuple[int, int, int] = (192, 192, 192)
    dark_gray: tuple[int, int, int] = (64, 64, 64)
    red: tuple[int, int, int] = (255, 0, 0)
    blue: tuple[int, int, int] = (85, 171, 255)
    bg_blue: tuple[int, int, int] = (64, 84, 128)
    green: tuple[int, int, int] = (85, 255, 171)
    purple: tuple[int, int, int] = (255, 64, 255)
    yellow: tuple[int, int, int] = (255,255,0)
    blue_black: tuple[int, int, int] = (6, 8, 32)
    light_blue_black: tuple[int, int, int] = (24, 32, 64)


class Camera:
    def __init__(self, surface: pygame.Surface, scale: float, x: float, y: float, actor = None) -> None:
        self.surface: pygame.Surface = surface
        self.scale: float = scale
        self.x: float = x
        self.y: float = y
        self.actor = actor

    def get_pos(self, x, y) -> tuple[float, float]:
        return self.get_x(x), self.get_y(y)
    
    def get_x(self, x) -> float:
        if self.actor:
            return (x-self.actor.x)*self.scale+self.surface.get_width()/2
        return (x-self.x)*self.scale+self.surface.get_width()/2
    
    def get_y(self, y) -> float:
        if self.actor:
            return (y-self.actor.y)*self.scale+self.surface.get_height()/2
        return (y-self.y)*self.scale+self.surface.get_height()/2
    
    def get_screen_pos(self, x, y) -> tuple[float, float]:
        return self.get_screen_x(x), self.get_screen_y(y)
    
    def get_screen_x(self, x) -> float:
        if self.actor:
            return (x-self.surface.get_width()/2)/self.scale+(self.actor.x+self.actor.width/2)
        return (x-self.surface.get_width()/2)/self.scale+self.x
    
    def get_screen_y(self, y) -> float:
        if self.actor:
            return (y-self.surface.get_height()/2)/self.scale+(self.actor.y+self.actor.height/2)
        return (y-self.surface.get_height()/2)/self.scale+self.y


class Sprite:
    def __init__(self, image: pygame.image, x: float, y: float, width: float, height: float, rotation: float = 0) -> None:
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height
        self.source_image: pygame.image = image
        self.rotation: float = rotation
        self.last_rotation: float = rotation
        self.target_rotation: float = rotation
        self.image: pygame.image = self.source_image
        if self.source_image.get_width() != self.width or self.source_image.get_height() != self.height:
            try:
                self.image = pygame.transform.smoothscale(self.source_image, (self.width, self.height))
            except:
                self.image = pygame.transform.scale(self.source_image, (self.width, self.height))

            #(Exception e):

        if self.rotation != 0:
            self.image = pygame.transform.rotate(self.source_image, self.rotation)
        self.centered: bool = False

    def draw(self, camera: Camera) -> None:
        if self.centered:
            camera.surface.blit(self.image, (self.x-self.image.get_width()/2, self.y-self.image.get_height()/2))
        else:
            x_offset = (self.image.get_width()-self.source_image.get_width())/2
            y_offset = (self.image.get_height()-self.source_image.get_height())/2
            camera.surface.blit(self.image, (self.x-x_offset, self.y-y_offset))
        #camera.surface.blit(self.image, (100, 100))
        #print(self.image.get_width())
    def set_centered(self, centered) -> None:
        self.centered = centered

    def update_image(self) -> None:
        if self.rotation != self.last_rotation:
            self.image = pygame.transform.rotate(self.ogimage, self.rotation)
        self.last_rotation = self.rotation
        if self.image.get_width() == self.width and self.image.get_height() == self.height:
            return
        if self.source_image.get_width() != self.width or self.source_image.get_height() != self.height:
            try:
                self.image = pygame.transform.smoothscale(self.source_image, (self.width, self.height))
            except:
                self.image = pygame.transform.scale(self.source_image, (self.width, self.height))


class Drawable:
    def __init__(self, x: float, y: float, width: int, height: int, image: pygame.image = None, rotation: float = 0) -> None:
        self.x: float = x
        self.y: float = y
        self.width: int = width
        self.height: int = height
        self.rotation: float = rotation
        self.image: pygame.image = image
        self.sprite: Sprite = None
        if self.image:
            self.create_sprite()
            

    def create_sprite(self, centered=True) -> None:
        self.sprite = Sprite(self.image, self.x, self.y, self.width, self.height, self.rotation)
        self.sprite.set_centered(centered)

    def update_sprite(self, camera: Camera):
        self.sprite.x, self.sprite.y = camera.get_pos(self.x, self.y)
        self.sprite.width = self.width*camera.scale
        self.sprite.height = self.height*camera.scale
        self.sprite.rotation = self.rotation
        self.sprite.update_image()

    def draw(self, camera):
        if self.sprite:
            self.update_sprite(camera)
            self.sprite.draw(camera)

