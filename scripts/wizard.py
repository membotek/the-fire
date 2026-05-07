from scripts import util,animation,setings,project_tile,share,entity
import pygame
class Wizard(entity.Entity):
    def __init__(self):
        super().__init__(speed=10,x=0,y=0)
        self.anims={
            "idle":animation.Animation("Sprites/EVil Wizard 2/Sprites/Idle.png",3,8,8,color=(0,0,0)),
            "run":animation.Animation("Sprites/EVil Wizard 2/Sprites/Run.png",3,8,8,color=(0,0,0)),
            "jump":animation.Animation("Sprites/EVil Wizard 2/Sprites/Jump.png",3,8,2,color=(0,0,0)),
            "attack1":animation.Animation("Sprites/EVil Wizard 2/Sprites/Attack1.png",3,5,8,color=(0,0,0)),
            "attack2":animation.Animation("Sprites/EVil Wizard 2/Sprites/Attack2.png",3,8,8,color=(0,0,0))
        }


    def jump(self):
        if self.on_ground == False or self.now_attack is not None:
            return False

        self.nowanim = "jump"
        self.y_speed = -22
        self.on_ground = False

    def get_boundbox(self):
        cent,bb=self.center_of_boundbox()
        world_rect = pygame.Rect(cent[0]-bb.width//10,cent[1]-bb.height//20+5,bb.width//4.7,bb.height//4-19)
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),share.apply_camera_rect(world_rect),1)
        return(world_rect)
    
    def attack1(self):
        super().attack1()
        a=project_tile.ProjectTile('Sprites/Projecttiles/fireballs/Fireball_68x9.png',self.x+10 if self.flip==True else self.x-20+self.center_of_boundbox()[1].width,self.y-100,40,40,0,12,0,self.attack_timers["attack1_timer"],3,10,color=(0,0,0),convert_alpha=True,rotate=90,die_on_the_ground=True)
        share.project_tiles.extend([a])
    def attack2(self):
        if self.on_ground == False or self.now_attack is not None:
            return False

        self.set_attacktimer(
            self.anims["attack2"].time * self.anims["attack2"].howmany_images - 1,
            "attack2"
        )         
        self.now_attack = "attack2"
        self.nowanim = "attack2"
        self.anims["attack2"].reset()
        a=project_tile.ProjectTile(
            image_path='Sprites/EVil Wizard 2/Sprites/Project_tile1.png',
            x=self.x+10 if self.flip==True else self.x-20+self.center_of_boundbox()[1].width,
            y=self.y+50,
            w=300,
            h=300,
            spawntime=35,
            time=self.attack_timers["attack2_timer"]*3-35,
            speed_x=15 if self.flip==False else -15,
            speed_y=3,
            scale=0.3,
            howmany_images=1
        )
        share.project_tiles.extend([a])