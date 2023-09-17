import pygame
import sys
from .sceneManager import GameSceneManager
from sprites.Zombie import Zombie
from sprites.Hammer import Hammer
from utils import *
from numpy import random
import numpy as np

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 30)
class StartScene:
    def __init__(self, display: pygame.Surface, gameSceneManager: GameSceneManager):
        self.display = display
        self.gameSceneManager = gameSceneManager
        self.score = 0;

    def start(self):
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
        pygame.mouse.set_visible(False)
        self.all_hammer = pygame.sprite.Group()
        self.player = Hammer()
        self.all_hammer.add(self.player)
        self.startTime = pygame.time.get_ticks()

    def run(self):
        if pygame.time.get_ticks() - self.startTime >= 1000:
            arr = np.array([0, 1, 2, 3, 4, 5])
            arr = random.permutation(arr)
            for i in arr:
                if self.all_zombie.sprites()[i].state == "hide":
                    self.all_zombie.sprites()[i].idle()
                    self.all_zombie.sprites()[i].idle_time(pygame.time.get_ticks())

                    break
            self.startTime = pygame.time.get_ticks()
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
                    zombie.dead()
                    self.score += 1

         # Render the score text
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))

        # Draw the score onto the screen
        self.display.blit(score_text, (10, 10))

        self.all_zombie.draw(self.display)
        self.all_hammer.draw(self.display)
        self.all_zombie.update()
        self.all_hammer.update()
