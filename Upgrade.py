import Finder as f
import ImageManager as im
import Clicker
import pyscreenshot
import time
import Resources as res

def upgrade():

    resources = res.get_resources() #get_resources funktioniert noch nicht

    n = number_of_builders()
    
    open_buildermenu()

    if(n > 1):
        pass
    else:
        upgrade_wall(resources)


def number_of_builders():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("builder"), 0.7)
    image = im.get_Screenshot(rects[0][0]+60, rects[0][1], 110, 50)
    #image = pyscreenshot.grab((rects[0][0]+60, rects[0][1], rects[0][0]+170, rects[0][1] +50))
    s = f.read_text(image)
    print("builders: " + s)
    if(s[0] == "V" or s[0] == "v" or s[0] == "/"):
        return 1
    return int(s[0])

def open_buildermenu():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("builder"), 0.7)
    Clicker.click(rects)
    Clicker.drag_top_builder_menu()

def upgrade_wall(resources):
    find_upgrade("Mauer")
    execute_upgrade(resources)

def find_upgrade(obj):
    # 460 150
    # 900 150
    # height = 60 | 750 -height
    box_x1 = 460
    box_x2 = 900
    box_y1 = 150
    box_y2 = 750
    height = 60
    width = box_x2 - box_x1
    found = False

    while(not found):
        for i in range(30):
            x1 = box_x1
            y1 = 150 + (i*20)
            image = im.get_Screenshot(x1,y1, width, height)
            img = pyscreenshot.grab((x1,y1,width+x1,height+y1))
            s = f.read_text(image)
            if(obj in s):
                found = True
                print("found!")
                Clicker.click_xy(x1 + 20, y1 + 30)
                break
        if(not found):
            Clicker.drag_down_builder_menu()

def execute_upgrade(resources):

    gold = resources[0]
    elixir = resources[1]

    rects = f.find_image(im.get_fullScreenshot(), im.get_image("upgrade_hammer"), 0.9)
    if(len(rects) == 2):
    
        if(gold > elixir):
            rects[0] = rects[0]
            Clicker.click(rects)
        else:
            rects[0] = rects[1]
            Clicker.click(rects)
    else:
        Clicker.click(rects)
    time.sleep(0.5)

    Clicker.click_xy(970, 950)