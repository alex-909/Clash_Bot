import cv2
import Attack as a
import Upgrade as u
import keyboard
import ImageManager
import Clicker
import time

print("start")
while(keyboard.is_pressed('q') == False):
    pass

a.attack()
time.sleep(6)
u.upgrade()