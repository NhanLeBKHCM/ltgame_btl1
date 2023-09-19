import pygame
import sys
from .sceneManager import GameSceneManager
from sprites.Zombie import Zombie
from sprites.Hammer import Hammer
from utils import *
from numpy import random
import numpy as np


class PlayScene:
    def __init__(self, display, gameSceneManager: GameSceneManager):
        self.display = display
        self.gameSceneManager = gameSceneManager

    def init(self):
        self.textFont = pygame.font.SysFont("monospace", 17, True)
        self.bg = pygame.transform.scale(
            pygame.image.load("data\\background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

    def start(self, state=None, data=None):
        self.all_zombie = pygame.sprite.Group()
        zombies = [
            Zombie(
                SCREEN_WIDTH / 3 * 0 + SCREEN_WIDTH / 3 / 2 - 48,
                SCREEN_HEIGHT / 2 * 0 + SCREEN_HEIGHT / 2 / 2 - 48,
            ),
            Zombie(
                SCREEN_WIDTH / 3 * 1 + SCREEN_WIDTH / 3 / 2 - 48,
                SCREEN_HEIGHT / 2 * 0 + SCREEN_HEIGHT / 2 / 2 - 48,
            ),
            Zombie(
                SCREEN_WIDTH / 3 * 2 + SCREEN_WIDTH / 3 / 2 - 48,
                SCREEN_HEIGHT / 2 * 0 + SCREEN_HEIGHT / 2 / 2 - 48,
            ),
            Zombie(
                SCREEN_WIDTH / 3 * 0 + SCREEN_WIDTH / 3 / 2 - 48,
                SCREEN_HEIGHT / 2 * 1 + SCREEN_HEIGHT / 2 / 2 - 48,
            ),
            Zombie(
                SCREEN_WIDTH / 3 * 1 + SCREEN_WIDTH / 3 / 2 - 48,
                SCREEN_HEIGHT / 2 * 1 + SCREEN_HEIGHT / 2 / 2 - 48,
            ),
            Zombie(
                SCREEN_WIDTH / 3 * 2 + SCREEN_WIDTH / 3 / 2 - 48,
                SCREEN_HEIGHT / 2 * 1 + SCREEN_HEIGHT / 2 / 2 - 48,
            ),
        ]
        self.all_zombie.add(zombies)

        self.all_hammer = pygame.sprite.Group()
        self.player = Hammer()
        self.all_hammer.add(self.player)
        pygame.mouse.set_visible(False)
        self.countTime = pygame.time.get_ticks()
        self.score = 0
        self.startTime = pygame.time.get_ticks()

    def end(self):
        pygame.mouse.set_visible(True)

    def update(self):
        self.display.blit(self.bg, (0, 0))
        duringTime = pygame.time.get_ticks() - self.startTime
        if duringTime >= 120000:
            self.gameSceneManager.setCurrentScene("start", "end", {"score": self.score})

        text_score = self.textFont.render(
            "Score: " + str(self.score), 1, (255, 255, 255)
        )

        text_time = self.textFont.render(
            "Time: "
            + (
                str((120 - int(duringTime / 1000)) // 60) + "'"
                if ((120 - int(duringTime / 1000)) // 60) > 0
                else ""
            )
            + (
                str((120 - int(duringTime / 1000)) % 60) + "0"
                if ((120 - int(duringTime / 1000)) % 60) < 10
                else str((120 - int(duringTime / 1000)) % 60)
            )
            + "s",
            1,
            (255, 255, 255),
        )
        self.display.blit(text_score, (500, 40))
        self.display.blit(text_time, (50, 40))
        if pygame.time.get_ticks() - self.countTime >= 3000:
            arr = np.array([0, 1, 2, 3, 4, 5])
            arr = random.permutation(arr)
            for i in arr:
                if self.all_zombie.sprites()[i].state == "hide":
                    self.all_zombie.sprites()[i].idle()
                    break
            self.countTime = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.smash()
                zombie_collide = pygame.sprite.spritecollide(
                    self.player, self.all_zombie, False
                )
                for zombie in zombie_collide:
                    self.score += 1
                    zombie.dead()

        self.all_zombie.draw(self.display)
        self.all_hammer.draw(self.display)
        self.all_zombie.update()
        self.all_hammer.update()
