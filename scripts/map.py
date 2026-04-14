from scripts import util
import pygame
def render(display):
    display.blit(background1,(0,0))
    display.blit(background2,(0,0))
    display.blit(image,(0,0))
def initmap():
    global image,background1,background2
    background1=util.loadimage("Sprites/GothicVania-town-files/GothicVania-town-files/PNG/environment/layers/background.png",4.69,autosize=True)
    background2=util.loadimage("Sprites/GothicVania-town-files/GothicVania-town-files/PNG/environment/layers/middleground.png",4.69,convert_alpha=True,autosize=True)
    image=util.loadimage("blood_city.png",1.69,convert_alpha=True,)