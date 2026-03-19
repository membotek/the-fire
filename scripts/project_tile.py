from scripts import util
import pygame
projecttiles=[]
class ProjectTile:
    def __init__(self,image_path,x,y,w,h,spead_x,spead_y,time,scale):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.image=util.loadimage(image_path,scale)
        self.sx=spead_x
        self.sy=spead_y
        self.t=time
    def update(self):
        self.t-=1
        self.x+=self.sx
        self.y+=self.sy
        if self.t<=0:
            projecttiles.remove(self)