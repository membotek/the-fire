from scripts import util, share, setings
import pygame
import math

def render(display):
    # Get dimensions
    W = setings.SCREAN_WIDTH
    H = setings.SCREAN_HEIGHT
    
    # Tile background1 (parallax coefficient 1.5)
    bg1_w = background1.get_width()
    bg1_h = background1.get_height()
    c1 = 1.5
    cam_x1 = share.camera[0] / c1
    cam_y1 = share.camera[1] / c1
    start_x1 = int(math.floor(cam_x1 / bg1_w) * bg1_w - bg1_w)
    start_y1 = int(math.floor(cam_y1 / bg1_h) * bg1_h - bg1_h)
    for x in range(start_x1, int(cam_x1 + W + bg1_w), bg1_w):
        for y in range(start_y1, int(cam_y1 + H + bg1_h), bg1_h):
            display.blit(background1, (x - cam_x1, y - cam_y1))
    
    # Tile background2 (parallax coefficient 1.25)
    bg2_w = background2.get_width()
    bg2_h = background2.get_height()
    c2 = 1.25
    cam_x2 = share.camera[0] / c2
    cam_y2 = share.camera[1] / c2
    start_x2 = int(math.floor(cam_x2 / bg2_w) * bg2_w - bg2_w)
    start_y2 = int(math.floor(cam_y2 / bg2_h) * bg2_h - bg2_h)
    for x in range(start_x2, int(cam_x2 + W + bg2_w), bg2_w):
        for y in range(start_y2, int(cam_y2 + H + bg2_h), bg2_h):
            display.blit(background2, (x - cam_x2, y - cam_y2))
    
    display.blit(image, share.apply_camera((0,setings.SCREAN_HEIGHT-image.get_height())))
def initmap():
    global image,background1,background2
    background1=util.loadimage("Sprites/GothicVania-town-files/GothicVania-town-files/PNG/environment/layers/background.png",4.69,autosize=True)
    background2=util.loadimage("Sprites/GothicVania-town-files/GothicVania-town-files/PNG/environment/layers/middleground.png",4.69,convert_alpha=True,autosize=True)
    image=util.loadimage("blood_city.png",3.8,convert_alpha=True)
    image=image.subsurface(image.get_bounding_rect())