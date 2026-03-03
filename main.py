import pygame
from scripts import setings,wizard,control
display=pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN)
setings.SCREAN_WIDTH=display.get_width()
setings.SCREAN_HEIGHT=display.get_height()
fps=pygame.time.Clock()
wiz=wizard.Wizard()
while True:
    fps.tick(60)
    display.fill((255,255,255))
    events=pygame.event.get()
    for i in events:
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_ESCAPE:
                exit(0)
            if i.key==control.move_right:
                wiz.move_right=True
            if i.key==control.move_left:
                wiz.move_left=True
            if i.key==control.jump:
                wiz.jump()
        if i.type==pygame.KEYUP:
            if i.key==control.move_right:
                wiz.move_right=False
            if i.key==control.move_left:
                wiz.move_left=False
    wiz.update()
    wiz.render()
    pygame.display.update()