import os

import pygame

from ships.base import Base


class Enemy(Base):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocity = 1
        self.laser_img = 'enemy_laser.png'
        dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.img = pygame.image.load(os.path.join(dirname, 'assets', 'enemy_ship.png'))
        self.mask = pygame.mask.from_surface(self.img)

    def move(self):
        self.y += self.velocity
