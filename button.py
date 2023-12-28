import pygame as pg

class Button():
    def __init__(self, x, y, w=64, h=64):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.curr_mouse = pg.mouse.get_pressed()
        self.last_mouse = self.curr_mouse

    def update(self):
        pg.event.get()
        self.curr_mouse = pg.mouse.get_pressed()
        self.last_mouse = self.curr_mouse

    def pressed(self):
        return True if self.curr_mouse[0] and not (self.last_mouse[0]) else False
    
    def released(self):
        return True if self.last_mouse[0] and not (self.curr_mouse[0]) else False