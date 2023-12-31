import pygame
import sys
import scenes.export as scenes
from utils import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameSceneManager = scenes.GameSceneManager(
            "start",
            {"scenes": {}},
        )
        playScene = scenes.PlayScene(self.screen, self.gameSceneManager)
        startScene = scenes.StartScene(self.screen, self.gameSceneManager)
        self.gameSceneManager.scenes = {"play": playScene, "start": startScene}
        self.bg = pygame.transform.scale(
            pygame.image.load("data\\background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

    def run(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            self.gameSceneManager.run()
            pygame.display.update()
            self.clock.tick(FPS)


Game().run()
