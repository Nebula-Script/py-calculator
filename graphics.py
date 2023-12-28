import pygame as pg

class Graphics():

    def __init__(self):

        self.width  = 400
        self.height = 576
        self.screen = pg.Surface((self.width, self.height))