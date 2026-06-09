from scripts import util, share, animation, setings
import pygame
class ProjectTile:
    def __init__(self,image_path,x,y,w,h,speed_x,speed_y,spawntime,time,scale,howmany_images,color=False,convert_alpha=False,rotate=0,die_on_the_ground=False,damage_multiplier=1,bb=None):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.bb=bb
        self.image_path=image_path
        if image_path is not None:
            self.animation=animation.Animation(image_path,scale,time=time/howmany_images,howmany_images=howmany_images,color=color,convert_alpha=convert_alpha)
        self.sx=speed_x
        self.sy=speed_y
        self.t=time
        self.damage_multiplier=damage_multiplier
        self.spawntime=spawntime
        if rotate!=0 and self.image_path is not None:
            rotated_images = [pygame.transform.rotate(img, rotate) for img in self.animation.list_of_images]
            self.animation.list_of_images = rotated_images
        self.die_on_the_ground=die_on_the_ground
        if image_path is not None:
            self.w,self.h=self.animation.list_of_images[0].get_size()
        else:
            self.w,self.h=w,h
    def update(self):
        self.spawntime-=1
        if self.spawntime<=0:
            self.t-=1
            self.x+=self.sx
            self.y+=self.sy
            if self.t<=0:
                share.project_tiles.remove(self)
        for enemy in share.enemys:
            if self.get_boundbox().colliderect(enemy.get_boundbox()):
                enemy.hp-=10*enemy.sheald*self.damage_multiplier
                enemy.take_hit()
    def render(self,screan):
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),share.apply_camera_rect(self.get_boundbox()),1)
        if self.image_path is not None:
            if self.die_on_the_ground and self.get_boundbox().bottom >= setings.SCREAN_HEIGHT:
                share.project_tiles.remove(self)
            else:
                if self.spawntime<=0:
                    self.animation.render((self.x,self.y),flip=False)
                    self.animation.update()
    def get_boundbox(self):
        if self.bb is not None:
            return self.bb.move(self.x, self.y)
        return pygame.Rect(self.x, self.y, self.w, self.h)