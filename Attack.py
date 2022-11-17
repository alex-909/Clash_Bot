from random import random
import Finder as f
import ImageManager as im
import Clicker
import Army as a
import Statistics
import time
import Resources as res

desired_gold = 200_000
air_defence_HP = [800,850,900,950,1000,1050,1100,1200,1300,1400,1500,1650,1750]
lightning_damage = [150,180,210,240,270,320,400,480,560,600]
lightning_level = 7
troops = ["barb", "dragon"]
heroes = ["king", "queen"]
spells = ["lightning"]


def attack():

    troop_amounts, hero_amounts, spell_amounts = a.check_army()

    findEnemy()

    place_army(troop_amounts, hero_amounts, spell_amounts)

    fight_over()
    check_starbonus
    
    a.new_troops()



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
    image = f.filter_pixels(image, 255, 251, 204)
    gold = f.read_text(image)
    goldNumber = f.text_to_Int(gold) 
    print("gold: " + str(goldNumber))
    return (goldNumber > desired_gold)

def place_army(troop_amounts, hero_amounts, spell_amounts):

    destroy_air_defence(spell_amounts[0])

    Clicker.drag_top_left()

    x = 0
    for i in troops:
        place_troops(i, troop_amounts[x], 1050, 100, 280, 680)
        x = x + 1
    
    x = 0
    for i in heroes:
        place_troops(i, hero_amounts[x], 1050, 100, 280, 680)
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
            elif spells_required.is_integer():
                place_spell("lightning",int(spells_required), rects[0][0], rects[0][1])
                spellamount = spellamount- (int(spells_required))
            else:
                place_spell("lightning",int(spells_required)+1, rects[0][0], rects[0][1])
                spellamount = spellamount- (int(spells_required)+1)

            rects = f.find_image(im.get_fullScreenshot(), im.get_image("air_defence_" + str(j+1)), 0.7)
            
        if spellamount == 0:
            break 
       
def place_troops(troop, amount, x1, y1, x2, y2):
    if(amount == 0):
        return
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
    
    check_results()

    Clicker.click(rects)
    time.sleep(3)

def check_starbonus():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("escape"), 0.7)
    Clicker.click(rects)
    time.sleep(1)    

def check_results():

    #region win
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("win"), 0.8)
    if(len(rects) == 1):
        win = "Win"
    else:
        win = "Loose"
    #endregion

    #region trophies
    #rects = f.find_image(im.get_fullScreenshot(), im.get_image("result_trophie"), 0.8)
    #image = im.get_Screenshot(rects[0][0] - 150 , rects[0][1] - 16, 130, 70)
    #image = f.filter_pixels(image, 255, 255, 255)
    #trophies = f.read_text(image)
    #trophies = f.text_to_Int(trophies)
    trophies = 0
    #endregion

    gold, elixir, dark_elixir = res.get_won_res()

    Statistics.add_attack(win, trophies, gold, elixir, dark_elixir)
