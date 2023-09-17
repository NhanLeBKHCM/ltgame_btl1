import pygame
import sys
# import time

from utils import *


class Zombie(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.data = {
            "dead": {
                "image_sheets": [
                    pygame.transform.scale(x, (96, 96))
                    for x in load_images("data\\zombie\\images\\Dead")
                ]
            },
            "idle": {
                "image_sheets": [
                    pygame.transform.scale(x, (96, 96))
                    for x in load_images("data\\zombie\\images\\Idle")
                ]
            },
        }
        self.state = "hide"
        self.current_sheet = 0
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.start_time = pygame.time.get_ticks() 

    def idle(self):
        if self.state != "idle":
            self.current_sheet = 0
            self.state = "idle"
            self.image = self.data["idle"]["image_sheets"][int(self.current_sheet)]
            self.rect.size = self.image.get_size()
            # self.start_time = start_time

        if self.current_sheet >= len(self.data["idle"]["image_sheets"]) - 1:
            self.current_sheet = 0
        else:
            self.current_sheet += 0.2
            self.image = self.data["idle"]["image_sheets"][int(self.current_sheet)]
    
    def idle_time(self, start_time):
        self.start_time = start_time

    def dead(self):
        if self.state != "dead":
            self.current_sheet = 0
            self.state = "dead"
            self.image = self.data["dead"]["image_sheets"][int(self.current_sheet)]
            self.rect.size = self.image.get_size()

        if self.current_sheet >= len(self.data["dead"]["image_sheets"]) - 1:
            self.current_sheet = 0
            self.hide()
        else:
            self.current_sheet += 0.1
            self.image = self.data["dead"]["image_sheets"][int(self.current_sheet)]

    def hide(self):
        if self.state != "hide":
            self.current_sheet = 0
            self.state = "hide"
            self.image = pygame.Surface((0, 0))
            self.rect.size = [0, 0]

    def update(self):
        if pygame.time.get_ticks() - self.start_time >= 3000:  # If more than 5 seconds have passed
            self.hide()
        if self.state == "idle":
            self.idle()
            pass
        elif self.state == "dead":
            self.dead()
        elif self.state == "hide":
            self.hide()

