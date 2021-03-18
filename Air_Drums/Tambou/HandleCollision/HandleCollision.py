

class HandleCollision:
    def __init__(self):
        self.objects=[]
    
    def registerObject(self,tamb):
        self.objects.insert(0,tamb)

    def Handle(self,position):
        for ob in self.objects:
            if(ob.active(position)):
                print('play sound ')