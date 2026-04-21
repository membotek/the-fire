from scripts import util, share
import pygame
class Animation:
    def __init__(self,path_for_images,scale,time,howmany_images,color=False,convert_alpha=False):
        self.list_of_images=util.slicer(path_for_images,scale,howmany_images,False,color,convert_alpha)
        self.reverse_list_of_images=util.slicer(path_for_images,scale,howmany_images,True,color,convert_alpha)
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
        screen_pos = share.apply_camera(cords)
        if flip:
            self.display.blit(self.reverse_list_of_images[self.now_index_of_image], screen_pos)
        else:
            self.display.blit(self.list_of_images[self.now_index_of_image], screen_pos)
    def reset(self):
        self.now_index_of_image=0
    