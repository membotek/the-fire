from scripts import util,animation,setings,wizard
import pygame

class Samurai(wizard.Wizard):
    def __init__(self):
        super().__init__()
        self.anims={
            "idle":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/IDLE.png",3,4,10),
            "run":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/RUN.png",3,4,16),
            "jump":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/RUN.png",3,4,16),
        }
    def action_in_air(self):
        if self.move_left==True:
            self.x+=-self.spead
            self.flip=True
        if self.move_right==True:
            self.x+=self.spead
            self.flip=False
    def jump(self):
        print(self.y_spead)
        None
    def render_boundbox(self):
        cent,bb=self.center_of_boundbox()
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(cent[0]-bb.width//10+(self.move_right-self.move_left)*10,cent[1]-bb.height//20+15,bb.width//4.7,bb.height//4+30),1)
        boundbox=pygame.Rect(cent[0]-bb.width//10+(self.move_right-self.move_left)*10,cent[1]-bb.height//20+15,bb.width//4.7,bb.height//4+30)
        return(boundbox)