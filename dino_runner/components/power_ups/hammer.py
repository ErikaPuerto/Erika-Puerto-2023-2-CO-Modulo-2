import pygame
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class Hammer(PowerUp):
    X_POS = 80
    Y_POS = 310
    HAMMER_SPEED = 8.5

    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
        #self.image = HAMMER
        #self.hammer_rect = self.image.get_rect()
        #self.hammer_rect.x = self.X_POS
        #self.hammer_rect.y = self.Y_POS
        #self.hammer_mov = False
        #self.hammer_speed = self.HAMMER_SPEED
    
    #def update(self, hammer_speed, user_input):
       # self.image = HAMMER
       