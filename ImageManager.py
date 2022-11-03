import cv2
import enum
import pyscreenshot as ImageGrab

root = r"images"

def get_image(name):
    if name == "map":
        path = root + r"\attackmap.png"

    if name == "dragon":
        path = root + r"\dragon.png"

    if name == "findEnemy1":
        path = root + r"\findEnemy1.png"

    if name == "findEnemy2":
        path = root + r"\findEnemy2.png"    

    if name == "enemyGold":
        path = root + r"\enemyGold.png"           

    if name == "hut":
        path = root + r"\Obj.png"    

    if name == "leftHalf":
       image = get_Screenshot(0,0,925,1000)
       return image
        
    if name == "base":
        return get_fullScreenshot()
        
    return cv2.imread(path)    


def get_fullScreenshot():
    im=ImageGrab.grab()
    im.save(root + r"\temp.png")
    return cv2.imread(root + r"\temp.png")


def get_Screenshot(x,y,w,h):
    im=ImageGrab.grab(bbox=(x, y, x+w, y+h))
    im.save(root + r"\temp.png")
    # im.show()
    return cv2.imread(root + r"\temp.png")