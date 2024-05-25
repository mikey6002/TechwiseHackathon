from config import *
import pygame
from pygame.locals import *
import time

pygame.init()

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        pygame.display.set_caption("Breakout")
        self.surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.surface.fill(WHITE)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        print("the up key has been pressed down")
            pygame.display.flip()
            time.sleep(SLEEP_TIME)
        pygame.quit()


clocl = pygame.time.Clock()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


class Paddle: 
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = (screen_width - self.width) // 2
        self.y = (screen_height - self.height) - 30
        self.speed = 5
    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
    
    def move(self, direction):
        if direction == "left" and self.x 

if __name__ == "__main__":
    game = Game()
    game.run()
