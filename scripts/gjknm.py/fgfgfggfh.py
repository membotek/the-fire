import pygame
from scripts import util
def load_like(what,example):
    oooooo=example.get_bounding_rect()
    top_r=oooooo.top/example.get_height()
    left_r=oooooo.left/example.get_width()
    width_r=oooooo.width/example.get_width()
    height_r=oooooo.height/example.get_height()
    what=what.subsurface((what.get_width()*left_r,what.get_height()*top_r,what.get_width()*width_r,what.get_height()*height_r))