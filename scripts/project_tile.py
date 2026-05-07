from scripts import util, share, animation, setings
import pygame
class ProjectTile:
    def __init__(self,image_path,x,y,w,h,speed_x,speed_y,spawntime,time,scale,howmany_images,color=False,convert_alpha=False,rotate=0,die_on_the_ground=False):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.animation=animation.Animation(image_path,scale,time=time/howmany_images,howmany_images=howmany_images,color=color,convert_alpha=convert_alpha)
        self.sx=speed_x
        self.sy=speed_y
        self.t=time
        self.spawntime=spawntime
        if rotate!=0:
            rotated_images = [pygame.transform.rotate(img, rotate) for img in self.animation.list_of_images]
            self.animation.list_of_images = rotated_images
        self.die_on_the_ground=die_on_the_ground
        self.w,self.h=self.animation.list_of_images[0].get_size()
    def update(self):
        self.spawntime-=1
        if self.spawntime<=0:
            self.t-=1
            self.x+=self.sx
            self.y+=self.sy
            if self.t<=0:
                share.project_tiles.remove(self)
    def render(self,screan):
        if self.die_on_the_ground and self.get_boundbox().bottom >= setings.SCREAN_HEIGHT:
            share.project_tiles.remove(self)
        else:
            if self.spawntime<=0:
                self.animation.render((self.x,self.y),flip=False)
                self.animation.update()
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),share.apply_camera_rect(self.get_boundbox()),1)
    def get_boundbox(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)