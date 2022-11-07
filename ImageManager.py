import cv2
import enum
import pyscreenshot as ImageGrab

root = r"images"

def get_image(name):

    if name == "train":
        path = root + r"\train.png"

    if name == "army_done":
        path = root + r"\army_done.png"

    if name == "escape":
        path = root + r"\escape.png"

    if name == "army":
        path = root + r"\army.png"

    if name == "army_menu":
        path = root + r"\army_menu.png"    

    if name == "confirm_upgrade":
        path = root + r"\confirm_upgrade.png"

    if name == "upgrade_hammer":
        path = root + r"\upgrade_hammer.png"

    if name == "builder":
        path = root + r"\builder.png"

    if name == "nach_hause":
        path = root + r"\nach_hause.png"

    if name == "map":
        path = root + r"\attackmap2.png"

    if name == "dragon":
        path = root + r"\dragon.png"

    if name == "barb":
        path = root + r"\barb.png" 

    if name == "king":
        path = root + r"\king.png"         

    if name == "lightning":
        path = root + r"\lightning.png"   

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

    #buildings
    
    #air defence
    if "air_defence" in name:
        level = get_Level(name)
        path = root + r"\air_defence\air_defence_" + str(level) + ".png"


        
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

def get_Level(imgname):
    last = imgname[len(imgname)-1]
    secondlast = imgname[len(imgname)-2]
    if(not secondlast.isnumeric()):
        secondlast = 0
    return int(last) + int(secondlast) * 10