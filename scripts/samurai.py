from scripts import util,animation,setings,entity,share, project_tile
import pygame

class Samurai(entity.Entity):
    def __init__(self):
        super().__init__(x=0,y=0,speed=13)
        self.attack1_projectile_spawned = False
        self.run_attack1_projectile_spawned = False
        self.anims={
            "idle":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/IDLE.png",4,4,10,color=(0,0,0)),
            "run":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/RUN.png",4,4,16,color=(0,0,0)),
            "jump":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/RUN.png",4,4,16,color=(0,0,0)),
            "attack1":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/ATTACK 1.png",4,5,7,color=(0,0,0)),
            "attack2":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/ATTACK 1.png",4,5,7,color=(0,0,0)),
            "run_attack1":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/RUN_ATTACK.png",4,4,3,color=(0,0,0)),
        }
    def update(self):
        super().update()
        if self.now_attack == "attack1" and not self.attack1_projectile_spawned and self.anims["attack1"].now_index_of_image == 4:
            self.spawn_attack_projectile("attack1")
            self.attack1_projectile_spawned = True
        if self.now_attack == "attack1" and not self.run_attack1_projectile_spawned and self.move_left != self.move_right and self.attack_timers.get("run_attack1_timer", 0) == 3:
            self.spawn_attack_projectile("run_attack1")
            self.run_attack1_projectile_spawned = True
        if self.move_left==True or self.move_right==True:
            if self.move_left==True and self.move_right==True:
                self.nowanim="idle"
            else:
                self.nowanim=("run_attack1" if self.now_attack=="attack1" else "run")
    def take_hit(self):
        pass
    def action_in_air(self):
        if self.now_attack is not None:
            return

        if self.move_left==True:
            self.x+=-self.speed
            self.flip=True
        if self.move_right==True:
            self.x+=self.speed
            self.flip=False
    def jump(self):
        pass
    def get_boundbox(self):
        cent,bb = self.center_of_boundbox()
        world_rect = pygame.Rect(cent[0]-bb.width//10+(self.move_right-self.move_left)*10,cent[1]-bb.height//20+15,bb.width//4.7,bb.height//4+38)
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),share.apply_camera_rect(world_rect),1)
        return(world_rect)

    def spawn_attack_projectile(self, attack_name):
        bb = self.get_boundbox()
        projectile_bb = pygame.Rect(0, 0, 142, 142)
        projectile_x = bb.left - projectile_bb.width if self.flip else bb.right
        projectile_y = bb.top
        a=project_tile.ProjectTile(None,projectile_x,projectile_y,40,40,0,0,0,self.attack_timers[attack_name+"_timer"],3,10,color=(0,0,0),convert_alpha=True,rotate=90,bb=projectile_bb,damage_multiplier=0.4)
        share.project_tiles.extend([a])
    
    def attack1(self):
        if self.on_ground == False or self.now_attack is not None:
            return False

        self.attack1_projectile_spawned = False
        self.run_attack1_projectile_spawned = False
        if self.move_left==self.move_right==False:
            self.set_attacktimer(
                self.anims["attack1"].time * self.anims["attack1"].howmany_images - 1,
                "attack1"
            )     
            self.now_attack = "attack1"
            self.nowanim = "attack1"
            self.anims["attack1"].reset()
        else:
            self.set_attacktimer(
                self.anims["run_attack1"].time * self.anims["run_attack1"].howmany_images//2 - 1,
                "run_attack1"
            )         
            self.now_attack = "attack1"
            self.nowanim = "run_attack1"
            self.anims["run_attack1"].reset()