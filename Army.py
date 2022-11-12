import Clicker
import time
import Finder as f
import ImageManager as im

troops = ["barb", "dragon"]
heros = ["king", "queen"]
spells = ["lightning"]

def army_done():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("army"), 0.7)
    Clicker.click(rects)   
    time.sleep(0.1) 
    isdone = f.find_image(im.get_Screenshot(0,0,500,300), im.get_image("army_done"), 0.7)  

    rects = f.find_image(im.get_fullScreenshot(), im.get_image("escape"), 0.7)
    Clicker.click(rects)   

    if len(isdone) == 0:

        return False

    return True    

def check_army():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("army"), 0.8)
    Clicker.click(rects)

    troop_amounts = check_troops()
    hero_amounts = check_heros()
    spell_amounts = check_spells()

    rects = f.find_image(im.get_fullScreenshot(), im.get_image("escape"), 0.7)
    Clicker.click(rects)

    return (troop_amounts, hero_amounts, spell_amounts)

def check_troops():

    amounts = [] #jeweilige Anzahl an ausgebildeten Truppen

    for i in troops:
        rects = f.find_image(im.get_fullScreenshot(),im.get_image(i),0.7)
        if(len(rects) > 0):
            image = im.get_Screenshot(rects[0][0] + 15, rects[0][1] - 38, 90, 38)
            image = f.filter_pixels(image, 255, 255, 255)
            s = f.read_text(image)
            s = s[1:]
            s = f.text_to_Int(s)
        else:
            s = "0"
        
        print(s)
        amounts.append(int(s))

    return(amounts) 

def check_heros():
    amounts = [] #jeweilige Anzahl an ausgebildeten Helden

    for i in heros:
        rects = f.find_image(im.get_fullScreenshot(),im.get_image(i),0.7)
        if(len(rects) > 0):
            s = "1"
        else:
            s = "0"
        
        amounts.append(int(s))

    return(amounts)

def check_spells():

    amounts = [] #jeweilige Anzahl an ausgebildeten Zaubern

    for i in spells:
        rects = f.find_image(im.get_fullScreenshot(), im.get_image(i), 0.7)
        if(len(rects) > 0):
            image = im.get_Screenshot(rects[0][0] +15, rects[0][1] - 45, 90, 42)
            image = f.filter_pixels(image, 255, 255, 255)
            s = f.read_text(image)
            s = s[1:]
            s = f.text_to_Int(s)
        else:
            s = "0"
        
        amounts.append(int(s))

    return amounts

def new_troops():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("army"), 0.7)
    Clicker.click(rects)   
    time.sleep(0.1) 
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("army_menu"), 0.7)
    Clicker.click(rects)
    time.sleep(0.5) 
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("train"), 0.7)
    Clicker.click(rects)
    time.sleep(0.5) 
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("escape"), 0.7)
    Clicker.click(rects)   


