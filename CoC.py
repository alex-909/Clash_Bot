import Attack as a
import Army as army
import Upgrade as u
import keyboard
import Finder as f
import ImageManager as im
import time as t
import Resources as res
import cv2
import Statistics

def main():
    while(True):
        while(not army.army_done()):
            res.collect_res()
            t.sleep(30)
 
        a.attack()

def test():
    
    a.check_results()
    pass

print("start")
while(keyboard.is_pressed('q') == False):
    pass

main()




