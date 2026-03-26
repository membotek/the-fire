from scripts import util,animation,setings,project_tile,share
from abc import ABC, abstractmethod
import pygame
class Entity(ABC):
    def __init__(self,speed=10):
        self.x=0
        self.y=0
        self.speed=speed
        self.nowanim="idle"
        self.flip=True
        self.now_attack=None
        self.attack_timers={
            "attack1_timer":0
        }
        self.anims={
            
        }
        self.move_left=False
        self.move_right=False
        self.y_speed=0
        self.g=0.6
        self.air_Ffr=0.98
        self.on_ground=False

    def render(self):
        self.anims[self.nowanim].render((self.x,self.y),self.flip)
        self.get_boundbox()

    def update(self):
        self.y_speed += self.g
        self.y_speed *= self.air_Ffr
        self.y += self.y_speed

        self.on_ground = False
        if self.get_boundbox().bottom >= setings.SCREAN_HEIGHT:
            self.y_speed = 0
            self.y = setings.SCREAN_HEIGHT - self.get_boundbox().height + self.y - self.get_boundbox().y
            self.on_ground = True

        if self.on_ground == False:
            self.action_in_air()
        else:
            if self.now_attack is None:
                if self.move_left:
                    self.x -= self.speed
                    self.nowanim = "run"
                    self.flip = True
                if self.move_right:
                    self.x += self.speed
                    self.nowanim = "run"
                    self.flip = False
                if (self.move_left and self.move_right) or (not self.move_left and not self.move_right):
                    self.nowanim = "idle"

        for key in list(self.attack_timers.keys()):
            if self.attack_timers[key] > 0:
                self.attack_timers[key] -= 1
                if self.now_attack:
                    self.attack(self.now_attack)
                if self.attack_timers[key] <= 0:
                    self.attack_timers[key] = 0
                    self.now_attack = None

        self.anims[self.nowanim].update()

    @abstractmethod
    def jump(self):
        pass

    def action_in_air(self):
        if self.now_attack is None:
            self.nowanim = "jump"
            if self.move_left:
                self.x -= self.speed
                self.flip = True
            if self.move_right:
                self.x += self.speed
                self.flip = False

    def center_of_boundbox(self):
        bb=self.anims[self.nowanim].list_of_images[0].get_rect(topleft=(self.x,self.y))
        centre=bb.center
        return(centre,bb)
    @abstractmethod
    def get_boundbox(self):
        pass
    
    def set_attacktimer(self,time,name_attack):
        self.attack_timers[name_attack+"_timer"]=time

    def attack(self,name_attack):
        self.nowanim=name_attack
    
    def attack1(self):
        if self.on_ground == False or self.now_attack is not None:
            return False

        self.set_attacktimer(
            self.anims["attack1"].time * self.anims["attack1"].howmany_images - 1,
            "attack1"
        )         
        self.now_attack = "attack1"
        self.nowanim = "attack1"
        self.anims["attack1"].reset()