from config import Config
from snake import Snake
from apple import Apple
import pygame


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Snake')
        self.apple = Apple()
        self.snake = Snake()
