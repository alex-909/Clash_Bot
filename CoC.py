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

def main():
    while(True):
        while(not army.army_done()):
            res.collect_res()
            u.upgrade()
            t.sleep(30)
 
        a.attack()

def test():
    c.drag_top_right()
    res.collect_res()
    u.upgrade()
    pass


print("start")
while(keyboard.is_pressed('q') == False):
    pass

#test()
main()




