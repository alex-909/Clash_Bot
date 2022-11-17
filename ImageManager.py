import cv2
import pyscreenshot as ImageGrab

root = r"images"

def get_image(name):         

    if name == "leftHalf":
       image = get_Screenshot(0,0,925,1080)
       return image
        
    if name == "base":
        return get_fullScreenshot()

    if name == "escape":
        path = root + r"\escape.png"  

    #region resources

    if name == "gold":
        path = root + r"\resources\gold.png"

    if name == "elixir":
        path = root + r"\resources\elixir.png"

    if name == "enemyGold":
        path = root + r"\resources\enemyGold.png"

    if name == "collect_gold":
        path = root + r"\resources\collect_gold.png"

    if name == "collect_elixir":
        path = root + r"\resources\collect_elixir.png"

    if name == "collect_darkelixir":
        path = root + r"\resources\collect_darkelixir.png"

    #endregion
    
    #region upgrade

    if name == "builder":
        path = root + r"\upgrade\builder.png"

    if name == "upgrade_hammer":
        path = root + r"\upgrade\upgrade_hammer.png"

    if name == "confirm_upgrade":
        path = root + r"\upgrade\confirm_upgrade.png"

    if name == "upgrade_elixir":
        path = root + r"\upgrade\elixir.png"
    
    if name == "upgrade_gold":
        path = root + r"\upgrade\gold.png"

    #endregion

    #region army

    if name == "army":
        path = root + r"\army\army.png"

    if name == "army_menu":
        path = root + r"\army\army_menu.png" 

    if name == "train":
        path = root + r"\army\train.png"  

    if name == "army_done":
        path = root + r"\army\army_done.png"

    #endregion

    #region attack

    if name == "attackmap":
        path = root + r"\attack\attackmap.png"

    if name == "findEnemy1":
        path = root + r"\attack\findEnemy1.png"

    if name == "findEnemy2":
        path = root + r"\attack\findEnemy2.png"

    if name == "nach_hause":
        path = root + r"\attack\nach_hause.png"  

    #region attack_results
    
    if name == "result_gold":
        path = root + r"\attack\results\gold.png"

    if name == "result_elixir":
        path = root + r"\attack\results\elixir.png"

    if name == "result_dark_elixir":
        path = root + r"\attack\results\dark_elixir.png"

    if name == "result_trophie":
        path = root + r"\attack\results\trophie.png"

    if name == "win":
        path = root + r"\attack\results\win.png"

    #endregion

    #endregion

    #region troops

    if name == "king":
        path = root + r"\troops\king.png"

    if name == "queen":
        path = root + r"\troops\queen.png" 

    if name == "barb":
        path = root + r"\troops\barb.png" 

    if name == "archer":
        path = root + r"\troops\archer.png"

    if name == "giant":
        path = root + r"\troops\giant.png" 

    if name == "goblin":
        path = root + r"\troops\goblin.png" 

    if name == "wallbreaker":
        path = root + r"\troops\wallbreaker.png" 

    if name == "baloon":
        path = root + r"\troops\baloon.png" 

    if name == "wizard":
        path = root + r"\troops\wizard.png" 

    if name == "healer":
        path = root + r"\troops\healer.png" 

    if name == "dragon":
        path = root + r"\troops\dragon.png"

    if name == "pekka":
        path = root + r"\troops\pekka.png"

    if name == "minion":
        path = root + r"\troops\minion.png"

    if name == "hogrider":
        path = root + r"\troops\hogrider.png"

    if name == "valkyre":
        path = root + r"\troops\valkyre.png"

    if name == "golem":
        path = root + r"\troops\golem.png"

    #endregion

    #region spells

    if name == "lightning":
        path = root + r"\spells\lightning.png" 

    #endregion

    #region buildings
    
    if "air_defence" in name:
        level = get_Level(name)
        path = root + r"\buildings\air_defence\air_defence_" + str(level) + ".png"

    #endregion
    
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

def resize(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent * 1.3 / 100)
    dim = (int(width), height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized
