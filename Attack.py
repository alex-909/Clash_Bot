from random import random
import Finder as f
import pyautogui
import ImageManager as im
import cv2
import Clicker

import time

desired_gold = 300_000
air_defence_HP = [800,850,900,950,1000,1050,1100,1200,1300,1400,1500,1650,1750]
lightning_damage = [150,180,210,240,270,320,400,480,560,600]
lightning_level = 5

def attack():
    findEnemy()
    while(not checkEnemy()):
        rects = f.find_image(im.get_fullScreenshot(), im.get_image("findEnemy2"), 0.7)
        Clicker.click(rects[0][0], rects[0][1])
        time.sleep(1)
    destroy_air_defence(7)
    Clicker.drag_top_left()
    place_troops("dragon", 9, 1050, 100, 280, 680)
    place_troops("barb", 5, 1050, 100, 280, 680)
    place_troops("king", 1, 1050, 100, 280, 680)
    fight_over()
    new_troops()


def fight_over():
    rects = []
    while(len(rects) == 0):
        time.sleep(5)
        rects = f.find_image(im.get_fullScreenshot(), im.get_image("nach_hause"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])
    time.sleep(3)



def findEnemy():
    rects = f.find_image(im.get_image("base"), im.get_image("map"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])
    time.sleep(0.5)
    rects = f.find_image(im.get_image("base"), im.get_image("findEnemy1"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])


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
       



def place_troops(troop, number, x1, y1, x2, y2):
    
    rects = f.find_image(im.get_fullScreenshot(), im.get_image(troop), 0.7)
    Clicker.click(rects[0][0], rects[0][1])

    for i in range(number):
        r = random()
        xPos = (x2-x1)*r + x1
        yPos = (y2-y1)*r + y1
        Clicker.click(xPos, yPos)
        time.sleep(0.319283712893)

def place_spell(spell, amount, x, y):
    
    rects = f.find_image(im.get_fullScreenshot(), im.get_image(spell), 0.7)
    Clicker.click(rects[0][0], rects[0][1])
    time.sleep(0.2)
    for i in range(amount):
        Clicker.click(x,y)
        time.sleep(0.2)
    

def new_troops():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("army"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])   
    time.sleep(0.1) 
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("army_menu"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])
    time.sleep(0.5) 
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("train"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])
    time.sleep(0.5) 
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("escape"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])   

def army_done():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("army"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])   
    time.sleep(0.1) 
    isdone = f.find_image(im.get_Screenshot(0,0,500,300), im.get_image("army_done"), 0.7)  

    rects = f.find_image(im.get_fullScreenshot(), im.get_image("escape"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])   

    if len(isdone) == 0:

        return False

    return True     
    