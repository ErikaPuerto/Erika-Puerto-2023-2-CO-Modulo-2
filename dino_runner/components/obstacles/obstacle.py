import pygame
from pygame.sprite import Sprite
import random

from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD


class Obstacle(Sprite):
    def __init__(self, image, obstacle_type):
        self.image = random.choice([LARGE_CACTUS, SMALL_CACTUS, BIRD, BIRD])
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y))