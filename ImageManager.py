import cv2
import enum
import pyscreenshot as ImageGrab

root = r"images"

def get_image(name):         

    if name == "leftHalf":
       image = get_Screenshot(0,0,925,1000)
       return image
        
    if name == "base":
        return get_fullScreenshot()

    if name == "escape":
        path = root + r"\escape.png"  

    #resources

    if name == "gold":
        path = root + r"\resources\gold.png"

    if name == "enemyGold":
        path = root + r"\resources\enemyGold.png"

    if name == "collect_gold":
        path = root + r"\resources\collect_gold.png"

    if name == "collect_elixir":
        path = root + r"\resources\collect_elixir.png"

    
    #upgrade

    if name == "builder":
        path = root + r"\upgrade\builder.png"

    if name == "upgrade_hammer":
        path = root + r"\upgrade\upgrade_hammer.png"

    if name == "confirm_upgrade":
        path = root + r"\upgrade\confirm_upgrade.png"


    #army

    if name == "army":
        path = root + r"\army\army.png"

    if name == "army_menu":
        path = root + r"\army\army_menu.png" 

    if name == "train":
        path = root + r"\army\train.png"  

    if name == "army_done":
        path = root + r"\army\army_done.png"



    #attack

    if name == "attackmap":
        path = root + r"\attack\attackmap.png"

    if name == "findEnemy1":
        path = root + r"\attack\findEnemy1.png"

    if name == "findEnemy2":
        path = root + r"\attack\findEnemy2.png"

    if name == "nach_hause":
        path = root + r"\attack\nach_hause.png"  



    #troops

    if name == "king":
        path = root + r"\troops\king.png"

    if name == "queen":
        path = root + r"\troops\queen.png" 

    if name == "dragon":
        path = root + r"\troops\dragon.png"

    if name == "barb":
        path = root + r"\troops\barb.png" 

    if name == "lightning":
        path = root + r"\troops\lightning.png" 

    #buildings
    
    #air defence
    if "air_defence" in name:
        level = get_Level(name)
        path = root + r"\buildings\air_defence\air_defence_" + str(level) + ".png"


        
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