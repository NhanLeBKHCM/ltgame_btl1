import pygame
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
C_BLACK = (0, 0, 0)


def load_images(dir_path: str):
    sheets = []
    print(sorted(os.listdir(dir_path), key=len))
    for file_name in sorted(os.listdir(dir_path), key=len):
        sheets.append(pygame.image.load(dir_path + "\\" + file_name))
    return sheets
