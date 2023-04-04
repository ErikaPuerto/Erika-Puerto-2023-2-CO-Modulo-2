import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD

obstacle = True

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        obstacle = Bird and Cactus(SMALL_CACTUS, LARGE_CACTUS) 
        return obstacle
    
    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)
            return obstacle
    
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("Collision")
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)