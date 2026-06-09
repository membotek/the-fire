from scripts import enemy,animation,util,share,entity
import pygame
import random
class Idle_state:
    def __init__(self,mushroom):
        self.mushroom=mushroom  
        self.enter()
    def enter(self):
        self.mushroom.nowanim="idle"
        self.wait_time=random.randint(30,180)
        self.mushroom.move_left=False
        self.mushroom.move_right=False
    def update(self):
        self.wait_time-=1
        if self.wait_time<=0:
            if random.choices([True,False],weights=[100-self.mushroom.rage*10,self.mushroom.rage*10])[0]==True:
                self.mushroom.state=Move_state(self.mushroom)
                self.mushroom.rage+=1
            else:
                self.mushroom.state=Detected_state(self.mushroom)
                self.mushroom.rage=0
class Move_state:
    def __init__(self,mushroom):
        self.mushroom=mushroom  
        self.enter()
    def enter(self):
        self.mushroom.nowanim="run"
        if random.randint(0,1)==0:
            self.mushroom.move_left=True
            self.mushroom.move_right=False
        else:
            self.mushroom.move_right=True
            self.mushroom.move_left=False  
        self.wait_time=random.randint(90,360) 
    def update(self):
        self.wait_time-=1
        if self.wait_time<=0:
            self.mushroom.state=Idle_state(self.mushroom)
class Detected_state:
    def __init__(self,mushroom):
        self.mushroom=mushroom  
        self.enter()
    def enter(self):
        self.d_enemys=[]
        self.d_enemys_distance=[]
        bb_serching=pygame.Rect(self.mushroom.x-4000,self.mushroom.y-4000,8000,8000)
        for enemy in share.enemys:
            if enemy!=self.mushroom:
                if bb_serching.colliderect(enemy.get_boundbox()):
                    self.d_enemys.append(enemy)
                    self.d_enemys_distance.append(1/(abs(enemy.x-self.mushroom.x)+1))
        if self.d_enemys!=[]:
            self.mushroom.goal=random.choices(self.d_enemys,weights=self.d_enemys_distance)[0]
            self.mushroom.speed=self.mushroom.speed*1.5
    def update(self):
        self.mushroom.state=Move_to_state(self.mushroom)
class Move_to_state:
    def __init__(self,mushroom):
        self.mushroom=mushroom  
        self.enter()
    def enter(self):
        self.mushroom.nowanim="run"
        if self.mushroom.goal.x>self.mushroom.x:
            self.mushroom.move_right=True
            self.mushroom.move_left=False
            self.mushroom.flip=False
        else:
            self.mushroom.move_left=True
            self.mushroom.move_right=False
            self.mushroom.flip=True
    def update(self):
        if abs(self.mushroom.goal.x-self.mushroom.x)<10:
            self.mushroom.move_left=False
            self.mushroom.move_right=False
class Take_hit_state:
    def __init__(self,mushroom):
        self.mushroom=mushroom  
        self.enter()
    def enter(self):
        self.mushroom.nowanim="take hit"
        self.mushroom.anims["take hit"].reset()
        self.wait_time=self.mushroom.anims["take hit"].time*self.mushroom.anims["take hit"].howmany_images
        print("take hit")
    def update(self):
        self.mushroom.nowanim="take hit"
        self.mushroom.y_speed=0
        self.mushroom.anims["take hit"].update()
        self.wait_time-=1
        if self.wait_time<=0:
            self.mushroom.state=Idle_state(self.mushroom)
class Death_state:
    def __init__(self,mushroom):
        self.mushroom=mushroom  
        self.enter()
    def enter(self):
        self.mushroom.nowanim="death"
        self.mushroom.y_speed=0
        self.wait_time=self.mushroom.anims["death"].time*self.mushroom.anims["death"].howmany_images+35
        print("death")
    def update(self):
        self.wait_time-=1
        self.mushroom.anims["death"].update()
        if self.wait_time<=0:
            share.enemys.remove(self.mushroom)
class Mushroom(enemy.Enemy):
    def __init__(self, x, y, speed=6):
        super().__init__(x, y, speed)
        self.anims={
            "idle":animation.Animation("Sprites/Monsters_Creatures_Fantasy/Mushroom/Idle.png",3.3,8,4,color=(0,0,0)),
            "run":animation.Animation("Sprites/Monsters_Creatures_Fantasy/Mushroom/Run.png",3.3,8,8,color=(0,0,0)),
            "jump":animation.Animation("Sprites/Monsters_Creatures_Fantasy/Mushroom/Idle.png",3.3,8,4,color=(0,0,0)),
            "take hit":animation.Animation("Sprites/Monsters_Creatures_Fantasy/Mushroom/Take Hit.png",3.3,6,4,color=(0,0,0),repit=False),
            "death":animation.Animation("Sprites/Monsters_Creatures_Fantasy/Mushroom/Death.png",3.3,10,4,color=(0,0,0),repit=False)
        }
        self.state=Idle_state(self)
        self.rage=0
        self.sheald=1
    def update(self):
        if self.state.__class__!=Take_hit_state and self.state.__class__!=Death_state:
            entity.Entity.update(self)
        self.state.update()
        

    def take_hit(self):
        if self.hp>0:
            self.state=Take_hit_state(self)
        elif self.hp<=0:
            if self.state.__class__!=Death_state:
                self.state=Death_state(self)
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
    
    def ai(self):
        None