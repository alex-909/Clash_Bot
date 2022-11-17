import Attack as a
import Army as army
import Upgrade as u
import keyboard
import Finder as f
import ImageManager as im
import time as t
import Resources as res
import cv2
import Clicker as c
import Statistics
import pytesseract

def main():
    while(True):
        while(not army.army_done()):
            res.collect_res()
            u.upgrade()
            t.sleep(30)
 
        a.attack()

def test():
    s = res.get_resources()
    print(s)
    pass


print("start")
while(keyboard.is_pressed('q') == False):
    pass

test()
#main()




