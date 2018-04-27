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
from pygame_window_view import View


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
    view = View(screen, model)
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
