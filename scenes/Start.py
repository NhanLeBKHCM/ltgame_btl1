import pygame
import sys
from .sceneManager import GameSceneManager
from sprites.Zombie import Zombie
from sprites.Hammer import Hammer
from utils import *
from numpy import random
import numpy as np


class StartScene:
    def __init__(self, display: pygame.Surface, gameSceneManager: GameSceneManager):
        self.display = display
        self.gameSceneManager = gameSceneManager

    def init(self):
        self.textFont = pygame.font.SysFont("monospace", 17, True)
        self.state = "start"

    def start(self, state=None, data=None):
        if data:
            self.data = data
        if state:
            self.state = state

    def end(self):
        pass

    def update(self):
        self.display.fill((0, 0, 0))
        if self.state == "start":
            text = self.textFont.render("Click to start!", 1, (255, 255, 255))
        else:
            text = self.textFont.render(
                "End game! Your score: " + str(self.data["score"]), 1, (255, 255, 255)
            )
        self.display.blit(
            text,
            (
                (SCREEN_WIDTH - text.get_size()[0]) / 2,
                (SCREEN_HEIGHT - text.get_size()[1]) / 2,
            ),
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "start":
                    self.gameSceneManager.setCurrentScene("play")
                else:
                    self.state = "start"
