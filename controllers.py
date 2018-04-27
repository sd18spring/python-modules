from pygame.locals import *
import pygame

class KeyboardController:
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


class MouseController:
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
