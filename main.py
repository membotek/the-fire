import pygame
from scripts import setings,wizard,control,samurai
display=pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN)
setings.SCREAN_WIDTH=display.get_width()
setings.SCREAN_HEIGHT=display.get_height()
fps=pygame.time.Clock()
wiz=wizard.Wizard()
sam=samurai.Samurai()
characters=[
    wiz,
    sam
]
now_indx_character=0
while True:
    fps.tick(60)
    display.fill((255,255,255))
    events=pygame.event.get()
    for i in events:
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_ESCAPE:
                exit(0)
            if i.key==control.move_right:
                characters[now_indx_character].move_right=True
            if i.key==control.move_left:
                characters[now_indx_character].move_left=True
            if i.key==control.jump:
                characters[now_indx_character].jump()
            if i.key==control.change_character_right:
                now_indx_character+=1
                if now_indx_character>=len(characters):
                    now_indx_character=0
            if i.key==control.change_character_left:
                now_indx_character-=1
                if now_indx_character<0:
                    now_indx_character=len(characters)-1
        if i.type==pygame.KEYUP:
            if i.key==control.move_right:
                characters[now_indx_character].move_right=False
            if i.key==control.move_left:
                characters[now_indx_character].move_left=False
    characters[now_indx_character].update()
    characters[now_indx_character].render()
    pygame.display.update()