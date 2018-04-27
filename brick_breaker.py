"""
Brickbreaker game

@author: pruvolo
"""

# By convention ( https://www.python.org/dev/peps/pep-0008/#imports )
# imports are grouped as: 

# 1) standard library
import random
import math
import time

# 2) 3rd party libraries
import pygame
from pygame.locals import *

# 3) Local modules
from simple_model import Model



class PyGameWindowView:
    """ Encodes a view of the BrickBreaker game in a PyGame window """
    
    def __init__(self, screen, model):
        """ Constructs a PyGameWindowView object
            screen: the window to draw the game to
            model: the Brick Breaker game state """
        self.screen = screen
        self.model = model
        
    def draw(self):
        """ Draws the game state to the PyGame window """
        self.screen.fill(pygame.Color(0,0,0))
        for brick in self.model.bricks:
            pygame.draw.rect(self.screen, brick.color, pygame.Rect(brick.x,brick.y,brick.width,brick.height))
        pygame.draw.rect(self.screen, pygame.Color(255,255,255), pygame.Rect(self.model.paddle.x,self.model.paddle.y,self.model.paddle.width,self.model.paddle.height))
        pygame.draw.ellipse(self.screen, pygame.Color(128,128,128),(self.model.ball.x-self.model.ball.r, self.model.ball.y-self.model.ball.r, 2*self.model.ball.r,2*self.model.ball.r))
        pygame.display.update()

class PyGameKeyboardController:
    """ Controls Brick Breaker using the keyboard """
    
    def __init__(self, model):
        """ Constructs a PyGameKeyboardController object
            model: the Brick Breaker game state """
        self.model = model
    
    def handle_pygame_event(self, event):
        """ handles a PyGame key down event
            event: a PyGame event of type KEYDOWN """
        if event.type != KEYDOWN:
            # nothing to do
            return
        if event.key == pygame.K_LEFT:
            self.model.change_paddle_velocity(-1)
        elif event.key == pygame.K_RIGHT:
            self.model.change_paddle_velocity(1)

class PyGameMouseController:
    """ Controls Brick Breaker using the mouse """
    
    def __init__(self, model):
        """ Constructs a PyGameMouseController object
            model: the Brick Breaker game state """
        self.model = model
    
    def handle_pygame_event(self, event):
        """ handles a PyGame key down event
            event: a PyGame event of type KEYDOWN """
        if event.type != MOUSEMOTION:
            # nothing to do
            return
        self.model.paddle.x = event.pos[0]-self.model.paddle.width/2.0

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = Model(size)
    view = PyGameWindowView(screen, model)
    #controller = PyGameMouseController(model)
    controller = PyGameKeyboardController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_pygame_event(event)

        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()
