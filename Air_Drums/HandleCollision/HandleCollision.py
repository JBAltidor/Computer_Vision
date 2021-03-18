import cv2

class HandleCollision:
    def __init__(self):
        self.objects=[]
        self.lastPlay=0
    
    def registerObject(self,tamb):
        self.objects.insert(0,tamb)

    def tambou_active(self,cnts,i):
        for c in cnts:        
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]) )
            cY = int((M["m01"] / M["m00"]) )
            if(self.objects[i].active((cX,cY))):
                return True
        return False
            
    def Handle(self,position,list_point):
        for i,ob in enumerate(self.objects):
            if(not self.tambou_active(list_point,i)):
                self.objects[i].playing=False
            
        for i,ob in enumerate(self.objects):
            if(ob.active(position)):
                if(not ob.playing):
                    ob.play()
                  
                    
    def inObject(self,position):
        for i,ob in enumerate(self.objects):
            if(ob.active(position)):
                return True
        return False

