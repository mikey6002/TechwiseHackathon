from config import *
import pygame
from pygame.locals import *
import time

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))






class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        pygame.display.set_caption("Breakout")
        self.surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.surface.fill(WHITE)
        brick = Brick()
        brick.draw()
        ball = Ball(10,10)
        ball.draw()

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

class Walls():
    def __init__(self):
        self.width = WINDOW_WIDTH//BRICKS_PER_ROW

class Ball():
    def __init__(self, x, y):
        self.rad = BALL_RADIUS
        self.x = x - self.rad
        self.y = y
        self.x_speed = BALL_X_VELOCITY
        self. y_speed = BALL_Y_VELOCITY  

    # def move(self):
    #     for i in range(10):
    #         if sef

    def draw(self):
        pygame.draw.circle(surface = screen, color = RED, center = [WINDOW_WIDTH/2, WINDOW_HEIGHT/2], radius = self.rad)

class Brick():
    def __init__(self):
        self.width, self.height = BRICK_WIDTH, BRICK_HEIGHT
        self.col = BRICKS_PER_ROW
        self.row = ROWS_OF_BRICKS
        self.y_offset = BRICK_Y_OFFSET
        self.gutter_width = BRICK_GUTTER_WIDTH
    def draw(self):
        print(self.height)
        pygame.draw.rect(surface = screen, color = BLACK, rect = Rect(self.width, self.height, self.width, self.height))


class Paddle(): 
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WINDOW_HEIGHT - self.width) // 2
        self.y = (WINDOW_WIDTH - self.height) - 30
        self.speed = 5
    def draw(self):
        pygame.draw.rect(surface = screen, color = GREEN, rect = Rect(self.width,self.width,self.width))
    
    # def move(self, direction):
    #     if direction == "left" and self.x 




if __name__ == "__main__":
    game = Game()
    game.run()
