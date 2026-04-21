from scripts import util, share
import pygame
class ProjectTile:
    def __init__(self,image_path,x,y,w,h,speed_x,speed_y,time,scale):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.image=pygame.Surface((self.w,self.h)) # util.loadimage(image_path,scale)
        self.sx=speed_x
        self.sy=speed_y
        self.t=time
    def update(self):
        self.t-=1
        self.x+=self.sx
        self.y+=self.sy
        if self.t<=0:
            share.project_tiles.remove(self)
    def render(self,screan):
        screan.blit(self.image, share.apply_camera((self.x, self.y)))