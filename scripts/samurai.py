from scripts import util,animation,setings,wizard

class Samurai(wizard.Wizard):
    def __init__(self):
        super().__init__()
        self.anims={
            "idle":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/IDLE.png",3,4,10),
            "run":animation.Animation("Sprites/FREE_Samurai 2D Pixel Art v1.2/Sprites/RUN.png",3,4,16),
        }
    def action_in_air(self):
        if self.move_left==True:
            self.x+=-self.spead
            self.flip=True
        if self.move_right==True:
            self.x+=self.spead
            self.flip=False
    def jump(self):
        None