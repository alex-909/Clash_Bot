
import Attack as a
import Upgrade as u
import keyboard


print("start")
while(keyboard.is_pressed('q') == False):
    pass
while(keyboard.is_pressed('e') == False):
    while(not a.army_done()):
        u.upgrade()

    a.attack()