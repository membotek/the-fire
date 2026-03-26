from scripts import util,animation,setings,project_tile,share,entity
import pygame
class Wizard(entity.Entity):
    def __init__(self):
        super().__init__(speed=10)
        self.anims={
            "idle":animation.Animation("Sprites/EVil Wizard 2/Sprites/Idle.png",2,8,8),
            "run":animation.Animation("Sprites/EVil Wizard 2/Sprites/Run.png",2,8,8),
            "jump":animation.Animation("Sprites/EVil Wizard 2/Sprites/Jump.png",2,8,2),
            "attack1":animation.Animation("Sprites/EVil Wizard 2/Sprites/Attack1.png",2,8,8)
        }


    def jump(self):
        if self.on_ground == False or self.now_attack is not None:
            return False

        self.nowanim = "jump"
        self.y_speed = -22
        self.on_ground = False

    def get_boundbox(self):
        cent,bb=self.center_of_boundbox()
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(cent[0]-bb.width//10,cent[1]-bb.height//20+5,bb.width//4.7,bb.height//4-19),1)
        boundbox=pygame.Rect(cent[0]-bb.width//10,cent[1]-bb.height//20+5,bb.width//4.7,bb.height//4-19)
        return(boundbox)
    
    def attack1(self):
        super().attack1()
        a=project_tile.ProjectTile(None,self.x+10 if self.flip==True else self.x-20+self.center_of_boundbox()[1].width,self.y-10,40,40,0,20,self.attack_timers["attack1_timer"],1)
        b=project_tile.ProjectTile(None,self.x+60 if self.flip==True else self.x-70+self.center_of_boundbox()[1].width,self.y-10,40,40,0,20,self.attack_timers["attack1_timer"],1)
        c=project_tile.ProjectTile(None,self.x+110 if self.flip==True else self.x-120+self.center_of_boundbox()[1].width,self.y-10,40,40,0,20,self.attack_timers["attack1_timer"],1)
        share.project_tiles.extend([a,b,c])