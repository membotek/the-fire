from scripts import util
import pygame
def render(display):
    display.blit(background1,(0,0))
    display.blit(background2,(0,0))
    display.blit(image,(0,0))
def initmap():
    global image,background1,background2
    background1=util.loadimage("blood_city.png",1.69)
    background2=util.loadimage("blood_city.png",1.69)
    image=util.loadimage("blood_city.png",1.69)