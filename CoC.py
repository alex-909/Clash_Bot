import Attack as a
import Upgrade as u
import keyboard
import Finder as f
import ImageManager as im
import time as t


print("start")
while(keyboard.is_pressed('q') == False):
    pass

while(True):
    while(not a.army_done()):
        t.sleep(30)
        pass
    a.attack()






