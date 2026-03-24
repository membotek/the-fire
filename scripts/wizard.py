from scripts import util,animation,setings
import pygame
class Wizard:
    def __init__(self):
        self.x=0
        self.y=0
        self.spead=10
        self.nowanim="idle"
        self.flip=True
        self.now_attack=None
        self.attack_timers={
            "attack1_timer":0
        }
        self.anims={
            "idle":animation.Animation("Sprites/EVil Wizard 2/Sprites/Idle.png",2,8,8),
            "run":animation.Animation("Sprites/EVil Wizard 2/Sprites/Run.png",2,8,8),
            "jump":animation.Animation("Sprites/EVil Wizard 2/Sprites/Jump.png",2,8,2),
            "attack1":animation.Animation("Sprites/EVil Wizard 2/Sprites/Attack1.png",2,8,8)
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
        self.y_spead += self.g
        self.y_spead *= self.air_Ffr
        self.y += self.y_spead

        self.on_ground = False
        if self.render_boundbox().bottom >= setings.SCREAN_HEIGHT:
            self.y_spead = 0
            self.y = setings.SCREAN_HEIGHT - self.render_boundbox().height + self.y - self.render_boundbox().y
            self.on_ground = True

        if self.on_ground == False:
            self.action_in_air()
        else:
            if self.now_attack is None:
                if self.move_left:
                    self.x -= self.spead
                    self.nowanim = "run"
                    self.flip = True
                if self.move_right:
                    self.x += self.spead
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

    def jump(self):
        if self.on_ground == False or self.now_attack is not None:
            return False

        self.nowanim = "jump"
        self.y_spead = -22
        self.on_ground = False

    def action_in_air(self):
        if self.now_attack is None:
            self.nowanim = "jump"
            if self.move_left:
                self.x -= self.spead
                self.flip = True
            if self.move_right:
                self.x += self.spead
                self.flip = False

    def center_of_boundbox(self):
        bb=self.anims[self.nowanim].list_of_images[0].get_rect(topleft=(self.x,self.y))
        centre=bb.center
        return(centre,bb)
    def render_boundbox(self):
        cent,bb=self.center_of_boundbox()
        pygame.draw.rect(pygame.display.get_surface(),(255,0,0),(cent[0]-bb.width//10,cent[1]-bb.height//20+5,bb.width//4.7,bb.height//4-19),1)
        boundbox=pygame.Rect(cent[0]-bb.width//10,cent[1]-bb.height//20+5,bb.width//4.7,bb.height//4-19)
        return(boundbox)
    
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
