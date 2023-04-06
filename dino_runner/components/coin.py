import pygame
import random
from dino_runner.utils.constants import SCREEN_WIDTH, COIN

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = COIN
        self.coin_rect = self.image.get_rect()
        self.coin_rect.x = SCREEN_WIDTH
        self.coin_rect.y = random.randint(125, 180)
        self.speed = 5