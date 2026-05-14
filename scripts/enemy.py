from scripts import entity,setings,share,mushroom
import random
import math
class Enemy(entity.Entity):
    def __init__(self,x,y,speed=10):
        super().__init__(x,y,speed)
        self.desciusion_timer=0
        self.motivation="idle"
        self.level_of_seen=math.sqrt(setings.SCREAN_WIDTH**2+setings.SCREAN_HEIGHT**2)
        self.seenmush=[]
        self.goal=None
        self.move_to_goal_ch=False
    def intelligence(self):
        self.desciusion_timer-=1
        if self.desciusion_timer<=0:
            chance=random.randint(0,100)
            if chance>35:
                self.casual()
                self.move_to_goal_ch=False
            else:
                if self.goal==None:
                    self.dettecting(enemys=share.enemys)
                else:
                    self.move_to_goal_ch=True
            self.desciusion_timer=random.randint(90,300)

    def dettecting(self,enemys):
        for enemy in enemys:
            if enemy!=self:
                if isinstance(enemy,mushroom.Mushroom)==True:
                    distance=math.hypot(self.x-enemy.x,self.y-enemy.y)
                    if distance<self.level_of_seen:
                        self.seenmush.append(enemy)
        probs=[]
        for i in self.seenmush:
            distance=math.hypot(self.x-i.x,self.y-i.y)
            probs.append(1/distance)
        if self.seenmush!=[]:
            self.goal=random.choices(self.seenmush,probs)[0]
    def move_to_goal(self):
            self.speed=11
            if self.goal!=None:
                if self.goal.x>self.x:
                    self.move_right=True
                    self.move_left=False
                    self.flip=False
                else:
                    self.move_left=True
                    self.move_right=False
                    self.flip=True
                if abs(self.goal.x-self.x)<10:
                    self.move_left=False
                    self.move_right=False
    def casual(self):
        self.speed=9
        if self.desciusion_timer<=0:
            if self.move_right or self.move_left == True:
                self.motivation="idle"
                self.move_left=False
                self.move_right=False
            else:
                self.motivation="move"
                if random.randint(0,1)==0:
                    self.move_left=True
                    self.move_right=False
                else:
                    self.move_right=True
                    self.move_left=False   
    def update(self):
        self.intelligence()
        super().update()
        if self.move_to_goal_ch==True:
            self.move_to_goal()
        else:
            self.move_to_goal_ch=False
            self.casual()