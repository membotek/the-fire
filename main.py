import pygame
from scripts import setings,wizard,control,samurai,share
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
click=False
project_tiles=[]
share.project_tiles=project_tiles
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
                spawnrect=characters[now_indx_character].get_boundbox()
                spawnx=characters[now_indx_character].x
                spawny=characters[now_indx_character].y
                spawnleft=characters[now_indx_character].move_left
                spawnright=characters[now_indx_character].move_right
                spawnflip=characters[now_indx_character].flip
                spawnanim=characters[now_indx_character].nowanim
                spawny_speed = characters[now_indx_character].y_speed

                now_indx_character+=1
                if now_indx_character>=len(characters):
                    now_indx_character=0
                characters[now_indx_character].x=spawnx
                characters[now_indx_character].y=spawny
                characters[now_indx_character].move_left=spawnleft
                characters[now_indx_character].move_right=spawnright
                characters[now_indx_character].flip=spawnflip
                characters[now_indx_character].nowanim=spawnanim
                characters[now_indx_character].y_speed = spawny_speed
                newbounbox=characters[now_indx_character].get_boundbox()
                deltax = newbounbox.left -characters[now_indx_character].x
                deltay = newbounbox.top - characters[now_indx_character].y
                newbounbox.bottom=spawnrect.bottom
                newbounbox.centerx = spawnrect.centerx
                characters[now_indx_character].y = newbounbox.top-deltay
                characters[now_indx_character].x = newbounbox.left - deltax

            if i.key==control.change_character_left:
                now_indx_character-=1
                if now_indx_character<0:
                    now_indx_character=len(characters)-1
        if i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1:
                click=True
                characters[now_indx_character].attack1()
        elif i.type==pygame.MOUSEBUTTONUP:
            if i.button==1:
                click=False
        if i.type==pygame.KEYUP:
            if i.key==control.move_right:
                characters[now_indx_character].move_right=False
            if i.key==control.move_left:
                characters[now_indx_character].move_left=False
    characters[now_indx_character].update()
    characters[now_indx_character].render()
    for i in project_tiles:
        i.update()
        i.render(display)
    pygame.display.update()
