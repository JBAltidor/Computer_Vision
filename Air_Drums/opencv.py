import numpy as np
import cv2
from pyimagesearch.shapedetector import ShapeDetector
import imutils
from Design.Design import Design
from Tambou.tambou import Tambou 
from HandleCollision.HandleCollision import HandleCollision
import simpleaudio as sa

#image1=cv2.imread('test.jpg')
#image2=cv2.imread('tt.png')

#dd=Design()
#image2=dd.resizeImage(200,image2)
#dd.addImage(20,20,image1,image2)
#cv2.imshow('image1',image1)


#define variable
"""dd=Design()

image2=dd.resizeImage(75,image2)
"""
HC=HandleCollision()
dd=Design()

wave_obj1 = sa.WaveObject.from_wave_file("crash.wav")
wave_obj2 = sa.WaveObject.from_wave_file("kick.wav")
wave_obj3 = sa.WaveObject.from_wave_file("ha_hat.wav")
wave_obj4 = sa.WaveObject.from_wave_file("tom_high.wav")
#wave_obj5 = sa.WaveObject.from_wave_file("ha_hat.wav")
wave_obj5 = sa.WaveObject.from_wave_file("Snare.wav")


#fond = cv2.imread('fond2.jpg')
tambou1=cv2.imread('jaune.png')
tambou1=dd.resizeImage(80,80,tambou1)

tambou2=cv2.imread('jaune.png')
tambou2=dd.resizeImage(80,80,tambou2)

tambou3=cv2.imread('rouge.png')
tambou3=dd.resizeImage(80,80,tambou3)

tambou4=cv2.imread('rouge.png')
tambou4=dd.resizeImage(80,80,tambou4)

tambou5=cv2.imread('jaune.png')
tambou5=dd.resizeImage(80,80,tambou5)


cap = cv2.VideoCapture(0)
tanb1 = Tambou(tambou1,50,300,wave_obj3)
tanb2 = Tambou(tambou2,450,300,wave_obj2)
tanb3 = Tambou(tambou3,150,400,wave_obj5)
tanb4 = Tambou(tambou4,360,400,wave_obj4)
tanb5 = Tambou(tambou5,500,160,wave_obj1)

HC.registerObject(tanb1)
HC.registerObject(tanb2)
HC.registerObject(tanb3)
HC.registerObject(tanb4)
HC.registerObject(tanb5)


#lo = np.array([110,50,50])
#hi = np.array([130,255,255])
color_infos = (0,0,255)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)
#cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.resizeWindow("Camera",800,700)
cv2.namedWindow("image2",cv2.WINDOW_NORMAL)



def nothing(x):
    pass

cv2.createTrackbar('H','image2',0,255,nothing)
cv2.createTrackbar('S','image2',53,255,nothing)
cv2.createTrackbar('V','image2',0,255,nothing)
cv2.createTrackbar('H1','image2',91,255,nothing)
cv2.createTrackbar('S1','image2',255,255,nothing)
cv2.createTrackbar('V1','image2',194,255,nothing)

start = False

while(True):
    #open the window in fullscreen
   
   

    #capture ecran
    ret, frame = cap.read()
    #effet miroir camera
    frame = cv2.flip(frame,1)

    #cv2.imshow("selfie",frame)
   
    #changement d'espace colorimetrique pour mieux segmenter la couleur
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #affinement de l'image
    #image = cv2.blur(image,(7,7))
    #filtrage couleur to track avec valeur min et max
    lo=np.array([cv2.getTrackbarPos('H','image2'),cv2.getTrackbarPos('S','image2'),cv2.getTrackbarPos('V','image2')])
    hi=np.array([cv2.getTrackbarPos('H1','image2'),cv2.getTrackbarPos('S1','image2'),cv2.getTrackbarPos('V1','image2')])
    
    mask = cv2.inRange(image,lo,hi)
    #kernel = np.uns((5,5),np.uint8)
    mask = cv2.erode(mask , None, iterations = 4)
    mask = cv2.dilate(mask , None, iterations = 4)
    image3= cv2.bitwise_and(frame,frame, mask = mask) 
   
    #frame = cv2.imread('fond2.jpg')
    tanb1.draw(frame) 
    tanb2.draw(frame)
    tanb3.draw(frame)
    tanb4.draw(frame)
    tanb5.draw(frame)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    
    sd = ShapeDetector()
    for c in cnts:
        #print(c)

        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        
       
        shape = sd.isCircle(c)

        if(shape):
            #M = cv2.moments(c)
            #cX = int((M["m10"] / M["m00"]) )
            #cY = int((M["m01"] / M["m00"]) )

            #c = max(cnts,key=cv2.contourArea)
            ((cX,cY),rayon)= cv2.minEnclosingCircle(c)
            cX = int(cX)
            cY= int(cY)
            if(rayon>15):
                if(start):
                    HC.Handle((cX,cY),cnts)


                cv2.circle(frame,(cX,cY), 5,color_infos,10 )
            
            #img = cv2.imread('test.jpg',1)
    

    
    if cv2.waitKey(1)  == ord('s'):
        start = True

    if cv2.waitKey(1)  == ord('v'):
        break
        

    cv2.imshow('image2',image3)
    cv2.imshow('Camera',frame)


    
    

cap.release()
cv2.destroyAllWindows()

#img = cv2.imread('test.jpg',1)
#cv2.imshow('Image',img)
#cv2.waitKey(0)
#cv2.destroyAllwindows()
