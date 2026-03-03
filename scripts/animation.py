from scripts import util
import pygame
class Animation:
    def __init__(self,path_for_images,scale,time,howmany_images,color=(0,0,0)):
        self.list_of_images=util.slicer(path_for_images,scale,howmany_images,False,color)
        self.reverse_list_of_images=util.slicer(path_for_images,scale,howmany_images,True,color)
        self.timer=time
        self.time=time
        self.now_index_of_image=0
        self.howmany_images=howmany_images
        self.display=pygame.display.get_surface()
    def update(self):
        self.timer-=1
        if self.timer<=0:
            self.now_index_of_image+=1
            if self.now_index_of_image>=self.howmany_images:
                self.now_index_of_image=0
            self.timer=self.time
    def render(self,cords,flip):
        '''
        Docstring for render
        
        :param cords: sorry we can't place in constructor
        '''
        if flip==True:
            self.display.blit(self.reverse_list_of_images[self.now_index_of_image],(cords))
        else:
            self.display.blit(self.list_of_images[self.now_index_of_image],(cords))
    