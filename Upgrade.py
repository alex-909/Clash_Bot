import Finder as f
import ImageManager as im
import Clicker
import pyscreenshot
import time

def upgrade():

    n = number_of_builders()
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("builder"), 0.7)
    Clicker.click(rects)
    Clicker.drag_top_builder_menu()
    if(n > 1):
        pass
    else:
        upgrade_wall()

def execute_upgrade():

    resources = get_resources() #get_resources funktioniert noch nicht
    gold = resources[1]
    elixir = resources[2]

    rects = f.find_image(im.get_fullScreenshot(), im.get_image("upgrade_hammer"), 0.9)
    if(len(rects) == 2):
    
        if(gold > elixir):
            rects = rects[0]
            Clicker.click(rects)
        else:
            rects = rects[1]
            Clicker.click(rects)
    else:
        Clicker.click(rects)
    time.sleep(0.5)

    Clicker.click_xy(970, 950)



def find_wall():
    # 460 150
    # 900 150
    # height = 60 | 750 -height
    box_x1 = 460
    box_x2 = 900
    box_y1 = 150
    box_y2 = 750
    height = 60
    width = box_x2 - box_x1
    wall_found = False

    while(not wall_found):
        for i in range(30):
            x1 = box_x1
            y1 = 150 + (i*20)
            image = im.get_Screenshot(x1,y1, width, height)
            img = pyscreenshot.grab((x1,y1,width+x1,height+y1))
            s = f.read_text(image)
            if("Mauer" in s):
                wall_found = True
                print("found!")
                Clicker.click(x1 + 20, y1 + 30)
                break
        if(not wall_found):
            Clicker.drag_down_builder_menu()

def number_of_builders():
    rects = f.find_image(im.get_fullScreenshot(), im.get_image("builder"), 0.7)
    image = im.get_Screenshot(rects[0][0]+60, rects[0][1], 110, 50)
    #image = pyscreenshot.grab((rects[0][0]+60, rects[0][1], rects[0][0]+170, rects[0][1] +50))
    s = f.read_text(image)
    print("builders: " + s)
    if(s[0] == "V" or s[0] == "v" or s[0] == "/"):
        return 1
    return int(s[0])


def upgrade_wall():
    find_wall()
    execute_upgrade()

def get_resources():
    rectsG = f.find_image(im.get_fullScreenshot(),im.get_image("gold"),0.8)
    imageG = im.get_Screenshot(rectsG[0][0]-200,rectsG[0][1] + 12,175,32)
    gold = f.read_text(imageG)

    rectsE = f.find_image(im.get_fullScreenshot(),im.get_image("elixir"),0.8)
    imageE = im.get_Screenshot(rectsE[0][0]-200,rectsE[0][1] + 1,175,32)
    elixir = f.read_text(imageE)
    
    resources = [gold,elixir]

    return resources