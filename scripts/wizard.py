from scripts import util,animation,setings
import pygame
class Wizard:
    def __init__(self):
        self.x=0
        self.y=0
        self.spead=10
        self.nowanim="idle"
        self.flip=True
        self.anims={
            "idle":animation.Animation("Sprites/EVil Wizard 2/Sprites/Idle.png",2,8,8),
            "run":animation.Animation("Sprites/EVil Wizard 2/Sprites/Run.png",2,8,8),
            "jump":animation.Animation("Sprites/EVil Wizard 2/Sprites/Jump.png",2,8,2)
        }
        self.move_left=False
        self.move_right=False
        self.y_spead=0
        self.g=0.6
        self.air_Ffr=0.98
        self.on_ground=False

    def render(self):
        self.anims[self.nowanim].render((self.x,self.y),self.flip)
        self.render_boundbox()

    def update(self):
        self.y_spead+=self.g
        self.y_spead*=self.air_Ffr
        self.y+=self.y_spead

        self.on_ground=False
        if self.render_boundbox().bottom>=setings.SCREAN_HEIGHT:
            self.y_spead=0
            self.y=setings.SCREAN_HEIGHT-self.render_boundbox().height+self.y-self.render_boundbox().y
            self.on_ground=True

        if self.on_ground==False:
            self.action_in_air()
        else:
            if self.move_left==True:
                self.x+=-self.spead
                self.nowanim="run"
                self.flip=True
            if self.move_right==True:
                self.x+=self.spead
                self.nowanim="run"
                self.flip=False
            if self.move_left==True and self.move_right==True or self.move_left==False and self.move_right==False:
                self.nowanim="idle"

        self.anims[self.nowanim].update()

    def jump(self):
        if self.on_ground==True:
            self.nowanim="jump"
            self.y_spead=-22
    
    def action_in_air(self):
        self.nowanim="jump"
        if self.move_left==True:
            self.x+=-self.spead
            self.flip=True
        if self.move_right==True:
            self.x+=self.spead
            self.flip=False
    
    def center_of_boundbox(self):
        bb=self.anims[self.nowanim].list_of_images[0].get_rect(topleft=(self.x,self.y))
        centre=bb.center
        return(centre,bb)
    def render_boundbox(self):
        cent,bb=self.center_of_boundbox()
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(cent[0]-bb.width//10,cent[1]-bb.height//20+5,bb.width//4.7,bb.height//4-19),1)
        boundbox=pygame.Rect(cent[0]-bb.width//10,cent[1]-bb.height//20+5,bb.width//4.7,bb.height//4-19)
        return(boundbox)