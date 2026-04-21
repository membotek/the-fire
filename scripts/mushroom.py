from scripts import enemy,animation,util,share
import pygame

class Mushroom(enemy.Enemy):
    def __init__(self, x, y, speed=6):
        super().__init__(x, y, speed)
        self.anims={
            "idle":animation.Animation("Sprites/Monsters_Creatures_Fantasy/Mushroom/Idle.png",3.3,8,4,color=(0,0,0)),
            "run":animation.Animation("Sprites/Monsters_Creatures_Fantasy/Mushroom/Run.png",3.3,8,8,color=(0,0,0)),
            "jump":animation.Animation("Sprites/Monsters_Creatures_Fantasy/Mushroom/Idle.png",3.3,8,4,color=(0,0,0))
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
    
    def ai(self):
        None