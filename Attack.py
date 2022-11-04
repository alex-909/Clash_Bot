from random import random
import Finder as f
import pyautogui
import ImageManager as im
import cv2
import Clicker

import time

desired_gold = 300_000

def attack():
    findEnemy()
    while(not checkEnemy()):
        rects = f.find_image(im.get_fullScreenshot(), im.get_image("findEnemy2"), 0.7)
        Clicker.click(rects[0][0], rects[0][1])
        time.sleep(1)
    analyze()
    Clicker.drag_top_left()
    place_troops("dragon", 9, 1050, 100, 280, 680)
    fight_over()


def fight_over():
    rects = []
    while(len(rects) == 0):
        time.sleep(5)
        rects = f.find_image(im.get_fullScreenshot(), im.get_image("nach_hause"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])



def findEnemy():
    rects = f.find_image(im.get_image("base"), im.get_image("map"), 0.7)
    Clicker.click(rects[0][0], rects[0][1])

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


def analyze():
    pass


def place_troops(troop, number, x1, y1, x2, y2):
    
    rects = f.find_image(im.get_fullScreenshot(), im.get_image(troop), 0.7)
    Clicker.click(rects[0][0], rects[0][1])

    for i in range(number):
        r = random()
        xPos = (x2-x1)*r + x1
        yPos = (y2-y1)*r + y1
        Clicker.click(xPos, yPos)
        time.sleep(0.319283712893)

