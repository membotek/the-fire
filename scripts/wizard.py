from scripts import util,animation,setings
class Wizard:
    def __init__(self):
        self.x=0
        self.y=0
        self.spead=10
        self.nowanim="idle"
        self.flip=True
        self.anims={
            "idle":animation.Animation("Sprites/EVil Wizard 2/Sprites/Idle.png",2,8,8),
            "run":animation.Animation("Sprites/EVil Wizard 2/Sprites/Run.png",2,8,8),
            "jump":animation.Animation("Sprites/EVil Wizard 2/Sprites/Jump.png",2,8,2)
        }
        self.move_left=False
        self.move_right=False
        self.y_spead=0
        self.g=0.6
        self.air_Ffr=0.98
        self.on_ground=False

    def render(self):
        self.anims[self.nowanim].render((self.x,self.y),self.flip)

    def update(self):
        self.y_spead+=self.g
        self.y_spead*=self.air_Ffr
        self.y+=self.y_spead

        self.on_ground=False
        if self.y>=setings.SCREAN_HEIGHT-500:
            self.y_spead=0
            self.y=setings.SCREAN_HEIGHT-500
            self.on_ground=True

        if self.on_ground==False:
            self.nowanim="jump"
            if self.move_left==True:
                self.x+=-self.spead
                self.flip=True
            if self.move_right==True:
                self.x+=self.spead
                self.flip=False
        else:
            if self.move_left==True:
                self.x+=-self.spead
                self.nowanim="run"
                self.flip=True
            if self.move_right==True:
                self.x+=self.spead
                self.nowanim="run"
                self.flip=False
            if self.move_left==True and self.move_right==True or self.move_left==False and self.move_right==False:
                self.nowanim="idle"

        self.anims[self.nowanim].update()

    def jump(self):
        if self.on_ground==True:
            self.nowanim="jump"
            self.y_spead=-22