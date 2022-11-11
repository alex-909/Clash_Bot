from random import random
import Finder as f
import ImageManager as im
import Clicker

import time

desired_gold = 350_000
air_defence_HP = [800,850,900,950,1000,1050,1100,1200,1300,1400,1500,1650,1750]
lightning_damage = [150,180,210,240,270,320,400,480,560,600]
lightning_level = 6
troops = ["barb", "dragon"]
heros = ["king", "queen"]
spells = ["lightning"]


def attack():

    troop_amounts, hero_amounts, spell_amounts = check_army()

    findEnemy()

    #place_army(troop_amounts, hero_amounts, spell_amounts)
    
    destroy_air_defence(7)                                              #
    Clicker.drag_top_left()                                             #
                                                                        #
    place_troops("dragon", 9, 1050, 100, 280, 680)                      #     Diese ganzen Zeilen werden durch die Methode place_army ersetzt
    place_troops("barb", 5, 1050, 100, 280, 680)                        #
    place_troops("king", 1, 1050, 100, 280, 680)                        #
    place_troops("queen", 1, 1050, 100, 280, 680)                       #

    fight_over()
    new_troops()

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
            s = f.read_text(image)
        else:
            s = "0"
        
        amounts.append(s)

    return(amounts)

def check_heros():
    amounts = [] #jeweilige Anzahl an ausgebildeten Truppen

    for i in heros:
        rects = f.find_image(im.get_fullScreenshot(),im.get_image(i),0.7)
        if(len(rects) > 0):
            s = "1"
        else:
            s = "0"
        
        amounts.append(s)

    return(amounts)

def check_spells():

    amounts = [] #jeweilige Anzahl an ausgebildeten Zaubern

    for i in spells:
        rects = f.find_image(im.get_fullScreenshot(),im.get_image(i),0.7)
        if(len(rects) > 0):
            image = im.get_Screenshot(rects[0][0] - 25, rects[0][1] - 50, 90, 38)
            s = f.read_text(image)
        else:
            s = "0"
        
        amounts.append(s)

    return amounts



def findEnemy():
    rects = f.find_image(im.get_image("base"), im.get_image("attackmap"), 0.7)
    Clicker.click(rects)
    time.sleep(0.5)
    rects = f.find_image(im.get_image("base"), im.get_image("findEnemy1"), 0.7)
    Clicker.click(rects)

    while(not checkEnemy()):
        rects = f.find_image(im.get_fullScreenshot(), im.get_image("findEnemy2"), 0.7)
        Clicker.click(rects)
        time.sleep(1)

def checkEnemy():
    rects = []
    while(len(rects) == 0):
        time.sleep(1)
        rects = f.find_image(im.get_image("leftHalf"), im.get_image("enemyGold"), 0.7)
    
    image = im.get_Screenshot(rects[0][0] + 40, rects[0][1]-10, 300, 40)
    gold = f.read_text(image)
    goldNumber = f.text_to_Int(gold) 
    print("gold: " + str(goldNumber))
    return (goldNumber > desired_gold)


def place_army(troop_amounts, hero_amounts, spell_amounts):

    destroy_air_defence(spell_amounts[1])

    Clicker.drag_top_left()

    x = 0
    for i in troops:
        place_troops(i, troop_amounts[x], 1050, 100, 280, 680)
        x = x + 1
    
    x = 0
    for i in heros:
        place_troops(i, hero_amounts[x], 1050, 100, 280, 680)
        x = x + 1


    x = 0
    for i in troops:
        place_troops(i, troop_amounts[x], 1050, 100, 280, 680)
        x = x + 1

def destroy_air_defence(spellamount):
    
    for j in range(12):                                                      #number of air defence levels -1
        rects = f.find_image(im.get_fullScreenshot(), im.get_image("air_defence_" + str(j+1)), 0.7)
        while(not len(rects) == 0 and spellamount > 0):
            
            spells_required = air_defence_HP[j]/lightning_damage[lightning_level-1]
            print("required: "+ str(spells_required))
            print("spells: "+ str(spellamount))
            if spells_required > spellamount:
                place_spell("lightning",spellamount, rects[0][0], rects[0][1])
                spellamount = 0
            else:
                place_spell("lightning",int(spells_required)+1, rects[0][0], rects[0][1])
                spellamount = spellamount- (int(spells_required)+1)

            rects = f.find_image(im.get_fullScreenshot(), im.get_image("air_defence_" + str(j+1)), 0.7)
            
        if spellamount == 0:
            break 
       
def place_troops(troop, amount, x1, y1, x2, y2):
    
    rects = f.find_image(im.get_fullScreenshot(), im.get_image(troop), 0.7)
    if(len(rects) > 0):
        Clicker.click(rects)
        time.sleep(0.2)
        for i in range(amount):
            r = random()
            xPos = (x2-x1)*r + x1
            yPos = (y2-y1)*r + y1
            Clicker.click_xy(xPos, yPos)
            time.sleep(0.2)

def place_spell(spell, amount, x, y):
    
    rects = f.find_image(im.get_fullScreenshot(), im.get_image(spell), 0.5)
    if(len(rects) > 0):
        Clicker.click(rects)
        time.sleep(0.2)
        for i in range(amount):
            Clicker.click_xy(x,y)
            time.sleep(0.2)    
    


def fight_over():
    rects = []
    while(len(rects) == 0):
        time.sleep(5)
        rects = f.find_image(im.get_fullScreenshot(), im.get_image("nach_hause"), 0.7)
    Clicker.click(rects)
    time.sleep(3)

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