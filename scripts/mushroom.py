from scripts import enemy

class Mushroom(enemy.Enemy):
    def __init__(self, speed=6):
        super().__init__(speed)