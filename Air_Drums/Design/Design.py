import cv2

class Design:
    def __init__(self):
        pass
    def addImage(self,posx,posy,image,imageAjout):
        image[posy:posy+imageAjout.shape[0], posx:posx+imageAjout.shape[1]] = imageAjout

    def resizeImage(self,width,height,src):
        #width = int(src.shape[1] * scale_percent / 100)
        #height = int(src.shape[0] * scale_percent / 100)

        largeur = width
        hauteur = height
        # dsize
        dsize = (largeur, hauteur)

        # resize image
        output = cv2.resize(src, dsize)
        return output
