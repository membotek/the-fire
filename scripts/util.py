import pygame
from scripts import setings
pygame.init()
import os
import csv

font = pygame.font.Font(None, 50)

def debug(msg: str):
    surf = setings.surf
    surf.blit(font.render(msg, True, "white"), (20, 100))


# load image and scale(yvelich)

def loadimage(path,scale=1,color=False,convert_alpha=False,autosize=False):
    image=pygame.image.load(path)
    if autosize==True:
        image=autosizze(image)
    else:
        w=image.get_width()
        h=image.get_height()
        image=pygame.transform.scale(image,(w*scale,h*scale))
    if convert_alpha==True:
        image=image.convert_alpha()
    else:
        image=image.convert()
    if color!=False and convert_alpha==False:
        image.set_colorkey((color))
    return(image)

def loadimages(dirpath,scale=1,color=False,convert_alpha=False):
    images=[]
    filenames=os.listdir(dirpath)
    for i in filenames:
        filepath=dirpath+'/'+i
        images.append(loadimage(filepath,scale,color))
    return(images)

def loadbordermapfromcsv(path):
    nomberstr=-1
    nombersto=-1
    border=set()
    f=open(path)
    file=csv.reader(f,delimiter=',')
    for i in file:
        nomberstr+=1
        nombersto=-1
        for g in i:
            nombersto+=1
            if g=='395':
                border.add((nomberstr,nombersto))
    return(border)
def loadenemyfromcsv(path):
    nomberstr=-1
    nombersto=-1
    enemy=[]
    f=open(path)
    file=csv.reader(f,delimiter=',')
    for i in file:
        nomberstr+=1
        nombersto=-1
        for g in i:
            nombersto+=1
            if g=='391':
                enemy.append((nombersto,nomberstr,'spirit'))
            if g=='392':
                enemy.append((nombersto,nomberstr,'raccoon'))
            if g=='390':
                enemy.append((nombersto,nomberstr,'bamboo'))
    return(enemy)
def loadobjfromcsv(path):
    nomberstr=-1
    nombersto=-1
    statues=[]
    f=open(path)
    file=csv.reader(f,delimiter=',')
    for i in file:
        nomberstr+=1
        nombersto=-1
        for g in i:
            nombersto+=1
            if g=='16':
                statues.append((nombersto,nomberstr,''))
    return(statues)
def loadnameimages(path,scale):
    b={}
    for i in os.listdir(path):
        b[i[:-4]]=loadimage(path+'/'+i,scale)
    return(b)
def slise(path,size=64,nomber=(0,0),scale=1):
    image=loadimage(path,scale)
    subimage=image.subsurface([size*nomber[0]*scale,size*nomber[1]*scale,size*scale,size*scale])
    return(subimage)
def slicer(path,scale,how_many_images_in_image,flip,colorkey=False,convert_alpha=False):
    image=loadimage(path,scale,colorkey)
    w=image.get_width()//how_many_images_in_image
    h=image.get_height()
    images=[]
    if flip==False:
        for i in range(0,how_many_images_in_image):
            a=image.subsurface(w*i,0,w,h)
            images.append(a)
    elif flip==True:
        for i in range(0,how_many_images_in_image):
            a=image.subsurface(w*i,0,w,h)
            a=pygame.transform.flip(a,True,False)
            images.append(a)
    
    return(images)
def autosizze(image):
    w=image.get_width()
    h=image.get_height()
    k=max(setings.SCREAN_WIDTH/w,setings.SCREAN_HEIGHT/h)
    print(k)
    image=pygame.transform.scale(image,(w*k,h*k))
    return(image)