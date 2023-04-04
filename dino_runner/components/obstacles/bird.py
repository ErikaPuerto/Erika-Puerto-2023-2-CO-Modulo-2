import random 
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):

    def __init__(self, image):
        super().__init__(image)
        self.bird_rect = self.image.get_rect()
        self.bird_rect.y = random.randrange(270, 320)
        self.step_index = 0

    def draw (self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]           
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0

        

