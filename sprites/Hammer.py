import pygame
from utils import *


class Hammer(pygame.sprite.Sprite):
    animate = {
        "smash": {
            "frames": [
                pygame.transform.rotate(
                    pygame.transform.scale(
                        pygame.image.load(
                            "data\\hammer\\images\\Smash\\TombStone (2).png"
                        ),
                        (48, 48),
                    ),
                    i,
                )
                for i in range(0, 90, 10)
            ]
        }
    }

    def __init__(self):
        super().__init__()
        self.state = "no_work"
        self.current_frame = 0
        self.image = self.animate["smash"]["frames"][self.current_frame]
        self.rect = self.image.get_rect()

    def smash(self):
        if self.state != "smashing":
            pygame.mixer.Channel(1).play(
                pygame.mixer.Sound("data\\hammer\\sounds\\table-smash.mp3")
            )
            self.state = "smashing"

        else:
            if self.current_frame >= len(self.animate["smash"]["frames"]) - 1:
                self.current_frame = 0
                self.state = "no_work"
                self.image = self.animate["smash"]["frames"][int(self.current_frame)]

            else:
                self.current_frame += 1
                self.image = self.animate["smash"]["frames"][int(self.current_frame)]

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        if self.state == "smashing":
            self.smash()
