import pygame

camera = [0, 0]

def apply_camera(cords,coefection_of_moving=1):
    return ((cords[0] - camera[0])/coefection_of_moving, (cords[1] - camera[1])/coefection_of_moving)

def apply_camera_rect(rect):
    return pygame.Rect(rect.left - camera[0], rect.top - camera[1], rect.width, rect.height)
