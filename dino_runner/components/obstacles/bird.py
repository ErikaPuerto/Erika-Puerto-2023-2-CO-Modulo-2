import random 
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    BIRD_HEIGHTS = [170, 220, 280]
    
    def __init__(self, image):
        super().__init__(image)
        self.bird_rect = self.image.get_rect()
        
        self.bird_rect.y = random.choice(self.BIRD_HEIGHTS)
        self.step_index = 0

    def draw(self, screen):
        if self.step_index >= 10:
            self.step_index = 0
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]           
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.step_index += 1
    