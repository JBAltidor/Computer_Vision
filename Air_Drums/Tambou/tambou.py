# import the necessary packages
import cv2
import numpy as np
from Design.Design import Design

class Tambou:
    def __init__(self,img,posx,posy,son):
        self.playing=False
        self.posx=posx
        self.posy=posy
        self.img=img
        self.son=son
    def draw(self,img_cap):
        dd=Design()
        dd.addImage(self.posx,self.posy,img_cap,self.img)

        
    def active(self,baguette):
        if ((baguette[0]>= self.posx and baguette[0]<=(self.posx+ self.img.shape[1])) and (baguette[1]>= self.posy  and baguette[1]<=(self.posy+ self.img.shape[0]))):
            return True
        else:
            return False
       
    def play(self):        
        self.son.play()
        self.playing = True



        
   




    